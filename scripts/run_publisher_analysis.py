# Automates publisher-related analysis

import os
import sys
import pandas as pd

# Dynamically add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.publisher_analysis import publisher_analysis

def main():
    df = pd.read_csv('data/raw_analyst_ratings.csv')
    
    publisher_counts, publisher_news_type, domain_counts = publisher_analysis(df)

    print(publisher_counts.head())
    print(publisher_news_type.head())
    print(domain_counts.head())

if __name__ == "__main__":
    main()
