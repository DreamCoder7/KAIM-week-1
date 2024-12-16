# Automates sentiment & topic modeling

import sys
import os

# Dynamically add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from src.data_loader import load_data
from src.text_analysis import analyze_sentiment, analyze_topics

def main():
    data_path = "data/raw_analyst_ratings.csv"
    df = load_data(data_path)
    
    # Perform Sentiment Analysis
    df_with_sentiment = analyze_sentiment(df)
    print("Sentiment Analysis:\n", df_with_sentiment[['headline', 'sentiment']].head())
    
    # Perform Topic Modeling
    df_with_topics = analyze_topics(df)
    print("Topic Modeling:\n", df_with_topics.head())

if __name__ == "__main__":
    main()
