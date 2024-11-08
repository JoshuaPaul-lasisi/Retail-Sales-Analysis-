import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from prophet import Prophet
from prophet.plot import plot_plotly

# Load data
@st.cache_data
def load_data(filepath):
    data = pd.read_csv(filepath)
    data['Date'] = pd.to_datetime(data['Date'])
    return data

# Load and preprocess data
data = load_data('../data/processed/cleaned_sales_data.csv')
st.title("Retail Sales Analysis Dashboard")
st.write("This dashboard provides insights into sales trends, categories, and seasonal patterns.")

# Sidebar filters
st.sidebar.header("Filters")
category_filter = st.sidebar.multiselect("Select Categories", data['Category'].unique())
date_range = st.sidebar.date_input("Select Date Range", [])

# Filter data based on user input
filtered_data = data.copy()
if category_filter:
    filtered_data = filtered_data[filtered_data['Category'].isin(category_filter)]
if date_range:
    start_date, end_date = date_range
    filtered_data = filtered_data[(filtered_data['Date'] >= start_date) & (filtered_data['Date'] <= end_date)]

# Visualizations
st.subheader("Sales Over Time")
sales_time_series = filtered_data.groupby('Date')['Amount'].sum().reset_index()
fig = px.line(sales_time_series, x='Date', y='Amount', title='Sales Over Time')
st.plotly_chart(fig)

st.subheader("Sales by Category")
category_sales = filtered_data.groupby('Category')['Amount'].sum().sort_values()
fig = px.bar(category_sales, x=category_sales.index, y='Amount', title='Sales by Category')
st.plotly_chart(fig)

st.subheader("Monthly Sales Trend")
filtered_data['Month'] = filtered_data['Date'].dt.to_period('M')
filtered_data['Month'] = filtered_data['Month'].dt.to_timestamp()
monthly_sales = filtered_data.groupby('Month')['Amount'].sum().reset_index()
fig = px.line(monthly_sales, x='Month', y='Amount', title='Monthly Sales Trend')
st.plotly_chart(fig)

# Forecasting with Prophet
st.subheader("Sales Forecast")
sales_time_series.columns = ['ds', 'y']
model = Prophet()
model.fit(sales_time_series)
future = model.make_future_dataframe(periods=90)  # 90 days into the future
forecast = model.predict(future)
fig = plot_plotly(model, forecast)
st.plotly_chart(fig)

# External Data Integration (Optional)
# Google Trends data example
# Uncomment and adjust the path if you have a Google Trends CSV file
# trends_data = pd.read_csv("path_to_your_google_trends_data.csv")
# fig = px.line(trends_data, x='Date', y='Interest', title='Google Trends Data')
# st.plotly_chart(fig)
# https://serpapi.com/search?engine=google_trends&q=Coffee&geo=NG
