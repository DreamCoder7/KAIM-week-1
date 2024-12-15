# Load and preprocess data

import pandas as pd

def load_data(file_path: str) -> pd.DataFrame:
    """Load data from file_path

    Args:
        file_path (str): _file description_

    Returns:
        pd.DataFrame: _data description_
    """
    data = pd.read_csv(file_path)
    data["Date"] = pd.to_datetime(data["Date"], errors="coerce")
    return data