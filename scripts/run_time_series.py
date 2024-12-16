# Automates time-series analysis


import os
import sys
import pandas as pd

# Dynamically add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.time_series_analysis import preprocess_data, aggregate_by_interval, detect_spikes, plot_publication_frequency, plot_spikes, analyze_publishing_times,decompose_time_series

# Main Function to Execute the Analysis
def main():
    df = pd.read_csv('data/raw_analyst_ratings.csv')

    df = preprocess_data(df)

    # Aggregate by time intervals (Daily, Weekly, Monthly)
    df_daily = aggregate_by_interval(df, 'D')
    df_weekly = aggregate_by_interval(df, 'W')
    df_monthly = aggregate_by_interval(df, 'M')

    # Detect spikes in publication frequency (Optional)
    df_daily_spikes = detect_spikes(df_daily)
    df_weekly_spikes = detect_spikes(df_weekly)
    df_monthly_spikes = detect_spikes(df_monthly)

    # Plot the publication frequency
    plot_publication_frequency(df_daily, title="Daily Publication Frequency")
    plot_publication_frequency(df_weekly, title="Weekly Publication Frequency")
    plot_publication_frequency(df_monthly, title="Monthly Publication Frequency")

    # Plot spikes in the publication frequency
    plot_spikes(df_daily_spikes, title="Spikes in Daily Publication Frequency")
    plot_spikes(df_weekly_spikes, title="Spikes in Weekly Publication Frequency")
    plot_spikes(df_monthly_spikes, title="Spikes in Monthly Publication Frequency")

    # Analyze publishing times (hourly analysis)
    analyze_publishing_times(df)

    # Optional: Decompose the time series (monthly data is recommended)
    decompose_time_series(df_monthly)

# Run the analysis
if __name__ == '__main__':
    main()
