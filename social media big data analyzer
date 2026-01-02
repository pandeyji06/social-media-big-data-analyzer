pip install streamlit pandas snscrape praw wordcloud matplotlib nltk scikit-learn
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import nltk
from sklearn.feature_extraction.text import CountVectorizer
import snscrape.modules.twitter as sntwitter
import praw

nltk.download('stopwords')
from nltk.corpus import stopwords

stop_words = stopwords.words('english')
st.set_page_config(page_title="Social Media Big Data Analyzer", layout="wide")
st.title("📊 Social Media Big Data Analyzer")
tab1, tab2, tab3 = st.tabs(["Facebook", "Reddit", "Twitter"])
def generate_wordcloud(text_data):
    vectorizer = CountVectorizer(stop_words=stop_words, max_features=5000)
    X = vectorizer.fit_transform(text_data)

    word_freq = X.sum(axis=0).A1
    words = vectorizer.get_feature_names_out()

    freq_dict = dict(zip(words, word_freq))

    wc = WordCloud(
        width=800,
        height=400,
        background_color='white'
    ).generate_from_frequencies(freq_dict)

    plt.figure(figsize=(12,6))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
    st.pyplot(plt)
with tab3:
    st.subheader("🐦 Twitter Analyzer")

    topic = st.text_input("Enter Topic / Hashtag", key="twitter_topic")
    limit = st.slider("Number of Tweets", 500, 5000, 1000)

    if st.button("Analyze Twitter"):
        tweets = []

        for i, tweet in enumerate(
            sntwitter.TwitterSearchScraper(topic).get_items()
        ):
            if i >= limit:
                break
            tweets.append(tweet.content)

        st.success(f"Fetched {len(tweets)} tweets")
        generate_wordcloud(tweets)
with tab2:
    st.subheader("👽 Reddit Analyzer")

    topic = st.text_input("Enter Topic", key="reddit_topic")
    limit = st.slider("Number of Posts", 500, 5000, 1000)

    if st.button("Analyze Reddit"):
        reddit = praw.Reddit(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
            user_agent="BigDataAnalyzer"
        )

        posts = []
        for submission in reddit.subreddit("all").search(topic, limit=limit):
            posts.append(submission.title + " " + submission.selftext)

        st.success(f"Fetched {len(posts)} posts")
        generate_wordcloud(posts)
with tab1:
    st.subheader("📘 Facebook Analyzer")

    topic = st.text_input("Enter Topic", key="fb_topic")
    limit = st.slider("Number of Posts", 500, 5000, 1000)

    if st.button("Analyze Facebook"):
        # Simulated / dataset-based (accepted academically)
        data = [f"{topic} discussion post {i}" for i in range(limit)]

        st.warning("Facebook data is simulated due to API restrictions")
        generate_wordcloud(data)
streamlit run app.py
