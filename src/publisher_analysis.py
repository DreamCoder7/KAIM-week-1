# Functions for publisher-related analysis

import pandas as pd

def identify_top_publishers(data: pd.DataFrame, top_n=10) -> pd.DataFrame:
    """Identify top publishers

    Args:
        data (pd.DataFrame): _data description_
        top_n (int, optional): _description. Defaults to 10.

    Returns:
        pd.DataFrame: _data description_
    """
    return data["Publisher"].value_counts().head(top_n)

def analyze_publisher_domains(data: pd.DataFrame) -> pd.DataFrame:
    """Analyze publisher domains

    Args:
        data (pd.DataFrame): _data description_

    Returns:
        pd.DataFrame: _data description_
    """
    data["domain"] = data["Publisher"].apply(lambda x: x.split('@')[-1] if '@' in x else 'Unknown')
    return data["domain"].value_counts()
