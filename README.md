# Sales-Summary-SQLite-Database-Project

A simple Python project that demonstrates how to work with SQLite databases, run SQL queries, and create basic visualizations using pandas and matplotlib.

## Overview

This project creates a small SQLite database with sales data and generates a basic sales summary with visualizations.

## Features

- Creates SQLite database with sample sales data
- Runs SQL queries to summarize sales by product
- Displays results using pandas DataFrames
- Generates bar chart visualization of revenue by product
- Saves chart as PNG file

## Requirements

```
python >= 3.6
pandas
matplotlib
sqlite3 (built into Python)
```

## Installation

1. Clone this repository:
```bash
git clone <your-repo-url>
cd sales-summary-sqlite
```

2. Install required packages:
```bash
pip install pandas matplotlib
```

## Usage

Run the main script:
```bash
python sales_summary.py
```

This will:
1. Create `sales_data.db` SQLite database
2. Insert sample sales data
3. Display sales summary table
4. Generate and save `sales_chart.png`

## Database Schema

The `sales` table contains:
- `id`: Primary key (auto-increment)
- `product`: Product name
- `quantity`: Quantity sold
- `price`: Unit price
- `sale_date`: Date of sale
- `customer_id`: Customer identifier

## Sample Output

The script generates a summary showing:
- Total quantity sold per product
- Total revenue per product
- Bar chart visualization

## Files

- `sales_summary.py`: Main Python script
- `sales_data.db`: SQLite database (created when script runs)
- `sales_chart.png`: Generated bar chart

## Learning Objectives

- Basic SQLite database operations
- SQL GROUP BY queries
- Pandas DataFrame manipulation
- Matplotlib bar chart creation
- File I/O operations

## License

MIT License
