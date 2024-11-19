# README_CN.md

## 电力停机分析

**注意：输入的 CSV 数据假定为每小时记录一次。**

本项目用于从时间序列数据集中分析发电机停机时间。项目通过 Pixi（一个基于 Rust 的 Python 包管理器）进行管理。

### 目录结构

- `power_shutdown_analysis/`
  - `src/`
    - `main.py`: 主脚本，用于执行分析。
    - `utils.py`: 分析停机时段的实用工具函数。
  - `power_data.yaml`: 配置文件，包含列名、数据路径和时间戳格式。
  - `pyproject.toml`: Pixi 的项目配置文件。

### 前置条件

- Python 3.x
- Pandas 库
- PyYAML 库
- Pixi 包管理器

### 设置

1. **安装 Pixi**:
   要安装 Pixi，请使用以下命令：

   ```sh
   curl -sSL https://install.pixi.rs | sh
   ```

2. **克隆仓库**：

   ```sh
   git clone git@github.com:zhujinxuan/shutdown-time-csv.git
   cd power_shutdown_analysis
   ```

3. **使用 Pixi 安装依赖**：

   ```sh
   pixi install
   ```

### 配置

编辑 `power_data.yaml` 以指定正确的设置：

- `timestamp_column`：CSV 中时间戳列的名称。
- `power_column`：电力生成列的名称。
- `timestamp_format`：时间戳的格式。
- `data_path`：CSV 输入文件的路径（例如：`D:\lqtest\power-time.csv`）。
- `output_path`：输出 CSV 文件的路径（例如：`D:\lqtest\shutdown_report.csv`）。

示例配置（`power_data.yaml`）：

```yaml
timestamp_column: 'timestamp'
power_column: 'power'
timestamp_format: '%Y-%m-%d_%H:%M'
data_path: 'D:\lqtest\power-time.csv'
output_path: 'D:\lqtest\shutdown_report.csv'
```

### 运行程序

使用 Pixi 运行主脚本：

```sh
pixi run python src/main.py projects/power_data.yaml
```

这将分析电力数据，生成一个包含每次停机的开始时间和持续时间的 CSV 文件，并将结果打印到控制台。

### 输出

脚本将在指定的输出路径生成一个发电机停机时段的 CSV 报告。该 CSV 文件包含：

- `timestamp`：停机的开始时间。
- `shutdown_hours`：停机的持续时间（小时）。

### 许可证

本项目使用 MIT 许可证授权。
