
import pandas as pd
import scipy.stats as stats

def calculate_daily_returns(stock_df):
    """
    Calculate daily returns based on the percentage change in the closing price.
    
    :param stock_df: DataFrame containing stock data with 'Close' column
    :return: DataFrame with a new 'Daily_Return' column
    """
    stock_df['Daily_Return'] = stock_df['Close'].pct_change() * 100
    return stock_df

def aggregate_sentiment(news_df):
    """
    Aggregate sentiment scores by date, calculating the mean sentiment for each day.
    
    :param news_df: DataFrame containing news sentiment scores
    :return: Series with the average sentiment for each day
    """
    news_df['Date'] = news_df.index.date
    daily_sentiment = news_df.groupby('Date')['Sentiment'].mean()
    return daily_sentiment

def merge_data(stock_df, daily_sentiment):
    """
    Merge stock data and daily sentiment data based on the date.
    
    :param stock_df: DataFrame containing stock data
    :param daily_sentiment: Series containing daily sentiment scores
    :return: Merged DataFrame with stock returns and sentiment data
    """
    stock_df['Date'] = stock_df.index.date
    merged_df = pd.merge(stock_df, daily_sentiment, left_on='Date', right_index=True, how='inner')
    return merged_df

def calculate_correlation(merged_df):
    """
    Calculate Pearson correlation between sentiment and stock returns.
    
    :param merged_df: DataFrame with stock returns and sentiment data
    :return: Pearson correlation coefficient and p-value
    """
    correlation, p_value = stats.pearsonr(merged_df['Sentiment'], merged_df['Daily_Return'])
    return correlation, p_value

if __name__ == "__main__":
    from src.data_preprocessing.load_data import load_data
    from src.data_preprocessing.load_news import load_news

    stock_df = load_data('data/AMZN_historical_data.csv')
    news_df = load_news('data/MSFT_historical_data.csv')
    
    stock_df = calculate_daily_returns(stock_df)
    
    daily_sentiment = aggregate_sentiment(news_df)
    
    merged_df = merge_data(stock_df, daily_sentiment)
    
    correlation, p_value = calculate_correlation(merged_df)
    print(f"Pearson correlation: {correlation}")
    print(f"P-value: {p_value}")
