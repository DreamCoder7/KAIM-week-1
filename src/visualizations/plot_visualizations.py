
import matplotlib.pyplot as plt

def plot_price_and_indicators(df):
    plt.figure(figsize=(14, 8))
    plt.plot(df['Close'], label='Stock Price', color='black')
    plt.plot(df['SMA_50'], label='50-day SMA', color='blue', linestyle='--')
    plt.plot(df['SMA_200'], label='200-day SMA', color='red', linestyle='--')
    plt.plot(df['EMA_50'], label='50-day EMA', color='green', linestyle='-.')
    plt.plot(df['EMA_200'], label='200-day EMA', color='orange', linestyle='-.')
    plt.title('Stock Price and Moving Averages')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()

def plot_rsi(df):
    # Plot RSI
    plt.figure(figsize=(14, 6))
    plt.plot(df['RSI'], label='RSI (14)', color='purple')
    plt.axhline(70, linestyle='--', color='red', label='Overbought (70)')
    plt.axhline(30, linestyle='--', color='green', label='Oversold (30)')
    plt.title('RSI (Relative Strength Index)')
    plt.xlabel('Date')
    plt.ylabel('RSI')
    plt.legend()
    plt.show()

def plot_macd(df):
    plt.figure(figsize=(14, 6))
    plt.plot(df['MACD'], label='MACD', color='blue')
    plt.plot(df['MACD_signal'], label='MACD Signal', color='red')
    plt.bar(df.index, df['MACD_hist'], label='MACD Histogram', color='green')
    plt.title('MACD (Moving Average Convergence Divergence)')
    plt.xlabel('Date')
    plt.ylabel('MACD')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    from src.data_preprocessing.load_data import load_data
    from src.technical_indicators.calculate_indicators import calculate_indicators
    df = load_data('data/yfinance_data/AAPL_historical_data.csv')
    df = calculate_indicators(df)
    plot_price_and_indicators(df)
    plot_rsi(df)
    plot_macd(df)
