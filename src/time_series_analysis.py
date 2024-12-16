# Functions for time series analysis
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Preprocess the Data
def preprocess_data(df):
    """
    Convert the 'date' column to datetime and drop rows with invalid dates.
    """
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df = df.dropna(subset=['date'])
    return df

# Step 2: Aggregate the Data by Time Intervals
def aggregate_by_interval(df, interval='D'):
    """
    Aggregates the data by a specified time interval (Daily, Weekly, Monthly).
    
    Parameters:
    - df: DataFrame containing the news articles
    - interval: Aggregation interval ('D' for daily, 'W' for weekly, 'M' for monthly)
    
    Returns:
    - DataFrame: Grouped by the specified interval with publication counts
    """
    if interval == 'D':
        df_grouped = df.groupby(df['date'].dt.date).size()
    elif interval == 'W':
        df_grouped = df.groupby(df['date'].dt.to_period('W')).size()
        df_grouped = df_grouped.reset_index()
        df_grouped['date'] = df_grouped['date'].dt.start_time  
    elif interval == 'M':
        df_grouped = df.groupby(df['date'].dt.to_period('M')).size()
        df_grouped = df_grouped.reset_index()
        df_grouped['date'] = df_grouped['date'].dt.start_time  
    
    if isinstance(df_grouped, pd.Series):
        df_grouped = df_grouped.reset_index(name='publication_count')
        df_grouped.rename(columns={'index': 'date'}, inplace=True)
    
    return df_grouped




# Step 3: Detect Spikes in Publication Frequency
def detect_spikes(df, threshold=1.5, window=7):
    """
    Detects spikes in publication frequency based on a rolling average.
    
    Parameters:
    - df: DataFrame containing the publication counts
    - threshold: Factor to detect spikes (e.g., 1.5 means spikes greater than 1.5x the moving average)
    - window: Size of the rolling window (in days)
    
    Returns:
    - DataFrame: Original DataFrame with spike information
    """
    df['rolling_avg'] = df['publication_count'].rolling(window=window).mean()
    
    df['spike'] = df['publication_count'] > (df['rolling_avg'] * threshold)
    return df

# Step 4: Plot the Publication Frequency
def plot_publication_frequency(df, title='Publication Frequency'):
    """
    Plots the publication frequency based on the provided DataFrame.
    
    Parameters:
    - df: DataFrame containing publication frequency data
    - title: Title of the plot
    """
    plt.figure(figsize=(10, 6))
    sns.lineplot(x='date', y='publication_count', data=df)
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Number of Articles Published')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Step 5: Plot Spikes in Publication Frequency
def plot_spikes(df, title='Spikes in Publication Frequency'):
    """
    Plots the publication frequency and highlights the detected spikes.
    
    Parameters:
    - df: DataFrame containing publication frequency data with spike information
    - title: Title of the plot
    """
    plt.figure(figsize=(10, 6))
    sns.lineplot(x='date', y='publication_count', data=df, label='Publication Count')
    sns.lineplot(x='date', y='rolling_avg', data=df, label='Rolling Average', linestyle='--')
    plt.scatter(df[df['spike']]['date'], df[df['spike']]['publication_count'], color='red', label='Spikes')
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Number of Articles Published')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Step 6: Analyze Publishing Times (Hourly Analysis)
def analyze_publishing_times(df):
    """
    Analyzes the time of day when publications occur.
    
    Parameters:
    - df: DataFrame containing the publication data with a 'date' column
    
    Returns:
    - DataFrame: Publication counts by hour of the day
    """
    df['hour'] = df['date'].dt.hour
    publication_by_hour = df.groupby('hour').size().reset_index(name='publication_count')
    
    plt.figure(figsize=(10, 6))
    sns.barplot(x='hour', y='publication_count', data=publication_by_hour, palette="viridis")
    plt.title("Publication Frequency by Hour of the Day")
    plt.xlabel('Hour of the Day')
    plt.ylabel('Number of Articles Published')
    plt.tight_layout()
    plt.show()

# Step 7: Time Series Decomposition
def decompose_time_series(df, period=12):
    """
    Decomposes the time series data into trend, seasonal, and residual components.
    
    Parameters:
    - df: DataFrame containing the publication count data (should be monthly or similar)
    - period: Number of periods in a full cycle (e.g., 12 for monthly data)
    """
    from statsmodels.tsa.seasonal import seasonal_decompose
    decomposition = seasonal_decompose(df['publication_count'], model='additive', period=period)
    
    plt.figure(figsize=(10, 6))
    decomposition.plot()
    plt.tight_layout()
    plt.show()
