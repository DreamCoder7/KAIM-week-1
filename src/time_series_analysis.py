# Functions for time series analysis

import pandas as pd

def analyze_publication_frequency(data: pd.DataFrame) -> pd.DataFrame:
    """Analyze publication frequency

    Args:
        data (pd.DataFrame): _data description_

    Returns:
        pd.DataFrame: _data description_
    """
    return data.groupby("Date").size()


def analyze_publishing_times(data: pd.DataFrame) -> pd.DataFrame:
    """Analyze publishing times

    Args:
        data (pd.DataFrame): _data description_

    Returns:
        pd.DataFrame: _data description_
    """
    data["hour"]= data["Date"].dt.hour
    return data["hour"].value_counts().sort_values()