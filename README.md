# Retail Sales Analysis Dashboard

This project provides an interactive **Retail Sales Analysis Dashboard** built using **Streamlit**. The dashboard allows users to explore sales data trends, view category-wise sales, analyze monthly patterns, and forecast future sales. It also integrates **Google Trends** data to enrich the analysis with external data insights.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Data Requirements](#data-requirements)
- [Future Enhancements](#future-enhancements)
- [License](#license)

## Project Overview

The **Retail Sales Analysis Dashboard** aims to provide insights into sales patterns, including:

- Sales over time for selected categories
- Monthly trends
- Sales forecasting for future planning

The dashboard also integrates with Google Trends data, adding an extra layer of insights by showing interest levels in retail sales over time.

## Features

1. **Sales Analysis**: View and analyze sales over time with filters for date range and category.
2. **Category-wise Sales**: Visualize sales by categories using interactive bar charts.
3. **Monthly Sales Trends**: Explore sales patterns across different months.
4. **Sales Forecasting**: Predict future sales trends using Facebook’s Prophet model.
5. **External Data Integration**: Import Google Trends data to track interest in "Retail Sales".

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/your-username/retail-sales-analysis-dashboard.git
    cd retail-sales-analysis-dashboard
    ```

2. **Install the required packages**:

    ```bash
    pip install -r requirements.txt
    ```

3. **Additional Setup**:
   - **Prophet** installation might require extra dependencies based on your system. Follow the setup guide [here](https://facebook.github.io/prophet/docs/installation.html) if issues arise.
   - Make sure **Google Trends data** is accessible by setting up **pytrends**.

## Usage

1. **Run the Streamlit App**:

   ```bash
   streamlit run app.py
    ```

2. **Upload Data**:
- Upload a CSV file with the following columns: Date, Category, and Amount.
- If needed, adjust paths in sales_dashboard.py for direct loading of Google Trends data.

3. **Explore the Dashboard**:

- Use filters to refine data by category and date.
- Analyze sales visualizations and monthly trends.
- View future sales forecasts.
- Track Google Trends interest in retail sales.

## Google Trends Integration

In sales_dashboard.py, the app uses pytrends to fetch Google Trends data. You can specify keywords and timeframe for interest tracking.
```bash
# Set up pytrends
from pytrends.request import TrendReq
pytrends = TrendReq(hl='en-US', tz=360)
kw_list = ["Retail Sales"]
pytrends.build_payload(kw_list, timeframe='today 5-y', geo='US')
```

## File Structure

```bash
├── data
│   └── processed
│       └── cleaned_sales_data.csv   # cleaned dataset
│   └── raw
│       └── Amazon Sale Report.csv
├── notebooks
│   └── notebook.ipynb
├── src
│   └── app.py                # Main Streamlit app
│   └── preprocesing.py
│   └── sales_dashboard.py    # Dashboard with Google Trends integration
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

## Data Requirements
Ensure your uploaded data file has the following structure:

Date: Date of the transaction (YYYY-MM-DD format).
Category: Sales category, e.g., Electronics, Furniture, etc.
Amount: Transaction amount.

## Future Enhancements
- Additional Forecasting Models: Implement other models like ARIMA to compare forecast accuracy.
- Expanded Google Trends: Allow users to select custom keywords for trends data.
- Interactive Filtering: Further refine filters to add more flexibility.
