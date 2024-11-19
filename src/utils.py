import pandas as pd
from datetime import timedelta
from typing import List, Dict

def analyze_shutdowns(df: pd.DataFrame, config: Dict[str, str]) -> List[Dict[str, object]]:
    """
    Analyzes shutdown periods of a generator from time-series data.

    Args:
        df (pd.DataFrame): The data frame containing time-series power data.
        config (dict): A dictionary containing configuration values for timestamp column, power column, and timestamp format.

    Returns:
        List[Dict[str, object]]: A list of dictionaries containing shutdown start timestamps and the duration in hours.
    """
    # Read column names and timestamp format from the configuration
    timestamp_column = config['timestamp_column']
    power_column = config['power_column']
    timestamp_format = config['timestamp_format']

    # Parse timestamps
    df[timestamp_column] = pd.to_datetime(df[timestamp_column], format=timestamp_format)
    df = df.sort_values(by=timestamp_column)

    shutdown_data = []
    shutdown_start = None
    shutdown_count = 0

    # Iterate through each row to find shutdown start and end points
    for i in range(len(df)):
        power = df.iloc[i][power_column]
        timestamp = df.iloc[i][timestamp_column]
        if power == 0:
            if shutdown_start is None:
                shutdown_start = timestamp
            shutdown_count += 1
        else:
            if shutdown_start is not None:
                shutdown_hours = shutdown_count
                shutdown_data.append({
                    'timestamp': shutdown_start,
                    'shutdown_hours': shutdown_hours
                })
                shutdown_start = None
                shutdown_count = 0

    # Handle the last shutdown period if it ended at the end of the dataset
    if shutdown_start is not None:
        shutdown_hours = shutdown_count
        shutdown_data.append({
            'timestamp': shutdown_start,
            'shutdown_hours': shutdown_hours
        })

    return shutdown_data
