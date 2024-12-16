# Automates descriptive statistics tasks

import pandas as pd
import sys
import os

# Dynamically add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.descriptive_stats import(
    calculate_headline_stats,
    count_articles_per_publisher,
    analyze_publication_trends
)

from src.data_loader import load_data

def main():
    data_path = "data/raw_analyst_ratings.csv"
    df = load_data(data_path)
    
    # Headline length statistics
    headline_stats = df["headline_stats"] = calculate_headline_stats(df)    
    print("Headline Length Statistics:\n", headline_stats)
    
    # Articles per publisher
    articles_per_publisher = df["articles_per_publisher"] = count_articles_per_publisher(df)
    print("Articles per Publisher:\n", articles_per_publisher)
    
    # Publication Trends
    publication_trends = df["publication_trends"] = analyze_publication_trends(df)
    print("Publication Trends:\n", publication_trends)
    
if __name__ == "__main__":
    main()