# README.md

## Power Shutdown Analysis

**Note: The input CSV data is assumed to be recorded hourly.**

This project analyzes power generator shutdown times from a time-series data set. The project is managed using Pixi, a Rust-based Python package manager.

### Directory Structure

- `power_shutdown_analysis/`
  - `src/`
    - `main.py`: Main script to execute the analysis.
    - `utils.py`: Utility functions for analyzing shutdown periods.
  - `power_data.yaml`: Configuration file containing column names, data path, and timestamp format.
  - `pyproject.toml`: Project configuration file for Pixi.

### Prerequisites

- Python 3.x
- Pandas library
- PyYAML library
- Pixi package manager

### Setup

1. **Install Pixi**:
   To install Pixi, use the following command:

   ```sh
   curl -sSL https://install.pixi.rs | sh
   ```

2. **Clone the repository**:

   ```sh
   git clone git@github.com:zhujinxuan/shutdown-time-csv.git
   cd power_shutdown_analysis
   ```

3. **Install dependencies** using Pixi:

   ```sh
   pixi install
   ```

### Configuration

Edit `power_data.yaml` to specify the correct settings:

- `timestamp_column`: Name of the timestamp column in the CSV.
- `power_column`: Name of the power generation column.
- `timestamp_format`: Format of the timestamps.
- `data_path`: Path to the CSV input file (e.g., `D:\lqtest\power-time.csv`).
- `output_path`: Path to the output CSV file (e.g., `D:\lqtest\shutdown_report.csv`).

Example configuration (`power_data.yaml`):

```yaml
timestamp_column: 'timestamp'
power_column: 'power'
timestamp_format: '%Y-%m-%d_%H:%M'
data_path: 'D:\lqtest\power-time.csv'
output_path: 'D:\lqtest\shutdown_report.csv'
```

### Running the Program

Use Pixi to run the main script:

```sh
pixi run python src/main.py projects/power_data.yaml
```

This will analyze the power data, generate a CSV file containing the start and duration of each shutdown, and print the results to the console.

### Output

The script will generate a CSV report of the power generator shutdown periods at the specified output path. The CSV will contain:

- `timestamp`: The start time of the shutdown.
- `shutdown_hours`: The duration of the shutdown in hours.

### License

This project is licensed under the MIT License.
