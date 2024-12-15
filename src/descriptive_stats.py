 # Functions for descriptive statistics
 
import pandas as pd

def compute_headline_stats(data: pd.DataFrame) -> pd.DataFrame:
    """Compute headline statistics for data
 
    Args:
        data (pd.DataFrame): _data description_
 
    Returns:
        pd.DataFrame: _data description_
    """
    data['headline_length'] = data['Headline'].apply(len)
    return data['headline_length'].describe()


def count_articles_per_publisher(data: pd.DataFrame) -> pd.DataFrame:
    """Count articles per publisher
 
    Args:
        data (pd.DataFrame): _data description_
 
    Returns:
        pd.DataFrame: _data description_
    """
    return data['Publisher'].value_counts()