
import os
import sys

# Dynamically add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from src.data_preprocessing.load_data import load_data
from src.technical_indicators.calculate_indicators import calculate_indicators
from src.visualizations.plot_visualizations import plot_price_and_indicators, plot_rsi, plot_macd

def main():
    # Load the stock price data
    df = load_data('data/yfinance_data/AAPL_historical_data.csv')
    
    # Calculate technical indicators
    df = calculate_indicators(df)
    
    # Plot visualizations
    plot_price_and_indicators(df)
    plot_rsi(df)
    plot_macd(df)

if __name__ == "__main__":
    main()
