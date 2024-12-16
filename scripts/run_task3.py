import os
import sys

# Dynamically add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.data_preprocessing.load_data import load_data
from src.data_preprocessing.load_news import load_news
from src.correlation_analysis.analyze_correlation import calculate_daily_returns, aggregate_sentiment, merge_data, calculate_correlation

def run_task_3(stock_file, news_file):
    # Load stock and news data
    stock_df = load_data(stock_file)
    news_df = load_news(news_file)
    
    # Calculate daily returns for stock data
    stock_df = calculate_daily_returns(stock_df)
    
    # Aggregate sentiment data by day
    daily_sentiment = aggregate_sentiment(news_df)
    
    # Merge stock data and sentiment data
    merged_df = merge_data(stock_df, daily_sentiment)
    
    # Perform correlation analysis
    correlation, p_value = calculate_correlation(merged_df)
    
    # Output results
    print(f"Pearson correlation between news sentiment and stock returns: {correlation}")
    print(f"P-value: {p_value}")

if __name__ == "__main__":
    stock_file = 'data/MSFT_historical_data.csv'
    news_file = 'data/TSLA_historical_data.csv'
    
    run_task_3(stock_file, news_file)
