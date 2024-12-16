
from textblob import TextBlob

def analyze_sentiment(news_df):
    """
    Analyze sentiment of news headlines and assign a polarity score.
    
    :param news_df: DataFrame containing news headlines
    :return: DataFrame with an additional 'Sentiment' column
    """
    news_df['Sentiment'] = news_df['Headline'].apply(lambda x: TextBlob(x).sentiment.polarity)
    return news_df

if __name__ == "__main__":
    from src.data_preprocessing.load_news import load_news
    news_df = load_news('path/to/your/news_data.csv')
    news_df = analyze_sentiment(news_df)
    print(news_df.head())
