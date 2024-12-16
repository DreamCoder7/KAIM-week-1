
import pandas as pd

def load_news(file_path):
    """
    Load news data from a CSV file.
    
    :param file_path: Path to the CSV file containing news data
    :return: pandas DataFrame containing the news data
    """
    df = pd.read_csv(file_path, parse_dates=True, index_col='Date')
    
    # Ensure the data contains the necessary columns
    if 'Headline' not in df.columns:
        raise ValueError("News data must contain a 'Headline' column")
    
    return df

if __name__ == "__main__":
    news_df = load_news('data/NVDA_historical_data.csv')
    print(news_df.head())
