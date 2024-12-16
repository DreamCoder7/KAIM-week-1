
import talib
import pandas as pd

def calculate_indicators(df):
    # Calculate Simple Moving Averages (SMA)
    df['SMA_50'] = talib.SMA(df['Close'], timeperiod=50)
    df['SMA_200'] = talib.SMA(df['Close'], timeperiod=200)
    
    # Calculate Exponential Moving Averages (EMA)
    df['EMA_50'] = talib.EMA(df['Close'], timeperiod=50)
    df['EMA_200'] = talib.EMA(df['Close'], timeperiod=200)
    
    # Calculate the Relative Strength Index (RSI)
    df['RSI'] = talib.RSI(df['Close'], timeperiod=14)
    
    # Calculate the MACD (Moving Average Convergence Divergence)
    df['MACD'], df['MACD_signal'], df['MACD_hist'] = talib.MACD(df['Close'], fastperiod=12, slowperiod=26, signalperiod=9)

    return df

if __name__ == "__main__":
    from src.data_preprocessing.load_data import load_data
    df = load_data('data/yfinance_data/AAPL_historical_data.csv')
    df = calculate_indicators(df)
    print(df.tail())
