import streamlit as st
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import nltk
from sklearn.feature_extraction.text import CountVectorizer
import praw

# Download stopwords
nltk.download("stopwords", quiet=True)
from nltk.corpus import stopwords

STOP_WORDS = stopwords.words("english")

# ---------------- APP CONFIG ----------------
st.set_page_config(
    page_title="Social Media Big Data Analyzer",
    layout="wide"
)

st.title("📊 Social Media Big Data Analyzer")
st.write("Trending topic analysis using Word Cloud")

# ---------------- WORD CLOUD FUNCTION ----------------
def generate_wordcloud(text_data):
    if not text_data:
        st.error("No data found.")
        return

    vectorizer = CountVectorizer(
        stop_words=STOP_WORDS,
        max_features=5000
    )

    X = vectorizer.fit_transform(text_data)
    words = vectorizer.get_feature_names_out()
    counts = X.sum(axis=0).A1

    freq_dict = dict(zip(words, counts))

    wc = WordCloud(
        width=800,
        height=400,
        background_color="white"
    ).generate_from_frequencies(freq_dict)

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.imshow(wc, interpolation="bilinear")
    ax.axis("off")
    st.pyplot(fig)

# ---------------- TABS ----------------
tab_fb, tab_reddit, tab_twitter = st.tabs(
    ["📘 Facebook", "👽 Reddit", "🐦 Twitter"]
)

# ---------------- FACEBOOK TAB ----------------
with tab_fb:
    st.subheader("Facebook Analyzer")
    st.info("Facebook API is restricted. Using simulated public post data.")

    topic = st.text_input("Enter Topic", key="fb_topic")
    limit = st.slider("Number of Posts", 500, 5000, 1000, key="fb_limit")

    if st.button("Generate Facebook Word Cloud"):
        data = [f"{topic} facebook post {i}" for i in range(limit)]
        generate_wordcloud(data)

# ---------------- REDDIT TAB ----------------
with tab_reddit:
    st.subheader("Reddit Analyzer")

    topic = st.text_input("Enter Topic", key="reddit_topic")
    limit = st.slider("Number of Posts", 500, 5000, 1000, key="reddit_limit")

    if st.button("Generate Reddit Word Cloud"):
        reddit = praw.Reddit(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
            user_agent="SocialMediaBigDataAnalyzer"
        )

        posts = []
        for submission in reddit.subreddit("all").search(topic, limit=limit):
            posts.append(submission.title + " " + submission.selftext)

        st.success(f"Fetched {len(posts)} Reddit posts")
        generate_wordcloud(posts)

# ---------------- TWITTER TAB ----------------
with tab_twitter:
    st.subheader("Twitter Analyzer")
    st.warning("Twitter scraping is simulated due to Python 3.13 limitations.")

    topic = st.text_input("Enter Topic or Hashtag", key="twitter_topic")
    limit = st.slider("Number of Tweets", 500, 5000, 1000, key="twitter_limit")

    if st.button("Generate Twitter Word Cloud"):
        tweets = [f"{topic} twitter tweet {i}" for i in range(limit)]
        generate_wordcloud(tweets)
