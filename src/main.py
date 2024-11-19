import argparse
import pandas as pd
import yaml
from utils import analyze_shutdowns
from typing import Dict

def read_yaml_config(file_path: str) -> Dict[str, str]:
    """
    Reads a YAML configuration file.

    Args:
        file_path (str): The path to the YAML config file.

    Returns:
        dict: A dictionary containing configuration values.
    """
    with open(file_path, 'r') as file:
        config = yaml.safe_load(file)
    return config

def main() -> None:
    """
    Main function to analyze generator shutdown durations from time-series data.
    """
    # Read the config file path from the command line
    parser = argparse.ArgumentParser(description='Analyze generator shutdown durations from time-series data.')
    parser.add_argument('config_path', type=str, help='Path to the YAML config file')
    args = parser.parse_args()

    # Read YAML configuration
    config = read_yaml_config(args.config_path)
    
    # Load data file
    df = pd.read_csv(config['data_path'])

    # Analyze shutdown periods
    shutdown_data = analyze_shutdowns(df, config)

    # Convert the shutdown data to a DataFrame
    shutdown_df = pd.DataFrame(shutdown_data)

    # Write the results to the output path specified in the config
    output_path = config['output_path']
    shutdown_df.to_csv(output_path, index=False)

    # Print the start time and duration of each consecutive shutdown
    for item in shutdown_data:
        print(f"Timestamp: {item['timestamp']}, Shutdown Hours: {item['shutdown_hours']}")

if __name__ == "__main__":
    main()
