# Functions for sentiment analysis and topic modeling

import pandas as pd
from textblob import TextBlob
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer

def analyze_sentiment(df: pd.DataFrame, column: str = "headline"):
    """
    Perform sentiment analysis on the headlines.
    Args:
        df (pd.DataFrame): The input data.
        column (str): The column containing the headlines.
    Returns:
        pd.DataFrame: The input data with sentiment analysis results.
    """
    if column not in df.columns:
        raise KeyError(f"'{column}' column not found in the dataset.")
    
    def get_sentiment(text: str):
        blob = TextBlob(text)
        return blob.sentiment.polarity, blob.sentiment.subjectivity
    
    df[['sentiment_polarity', 'sentiment_subjectivity']] = df[column].apply(lambda x: pd.Series(get_sentiment(x)))
    
    df['sentiment'] = df['sentiment_polarity'].apply(
        lambda x: 'Positive' if x > 0 else ('Negative' if x < 0 else 'Neutral')
    )
    
    return df[['headline', 'sentiment_polarity', 'sentiment_subjectivity', 'sentiment']]


def analyze_topics(df: pd.DataFrame, column: str = "headline", n_topics: int = 5):
    """
    Perform topic modeling on the headlines using KMeans clustering.
    Args:
        df (pd.DataFrame): The input data.
        column (str): The column containing the headlines.
        n_topics (int): Number of topics to extract.
    Returns:
        pd.DataFrame: DataFrame with topic assignments for each headline.
    """
    if column not in df.columns:
        raise KeyError(f"'{column}' column not found in the dataset.")
    
    tfidf_vectorizer = TfidfVectorizer(stop_words='english')
    
    tfidf_matrix = tfidf_vectorizer.fit_transform(df[column])
    
    kmeans = KMeans(n_clusters=n_topics, random_state=42)
    df['topic'] = kmeans.fit_predict(tfidf_matrix)
    
    return df[['headline', 'topic']]
