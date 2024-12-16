
import pandas as pd

def load_data(file_path):
    df = pd.read_csv(file_path, parse_dates=True, index_col='Date')
    
    expected_columns = ['Open', 'High', 'Low', 'Close', 'Volume']
    if not all(col in df.columns for col in expected_columns):
        raise ValueError(f"Data must contain the following columns: {expected_columns}")
    
    return df

if __name__ == "__main__":
    df = load_data('data/TSLA_historical_data.csv')
    print(df.head())
