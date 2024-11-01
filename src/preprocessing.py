# Import necessary libraries
import pandas as pd
import numpy as np

def load_data(filepath):
    """
    Load the sales data from a CSV file and perform initial data checks.
    """
    data = pd.read_csv(filepath)
    data['Date'] = pd.to_datetime(data['Date'])
    data['ship-postal-code'] = data['ship-postal-code'].astype(object)
    data.drop(columns='Unnamed: 22', inplace=True)
    return data

def clean_data(data):
    """
    Clean the sales data by handling zero quantities, missing values, and irrelevant columns.
    """
    data = data[data['Qty'] != 0]
    data.drop(columns='fulfilled-by', axis=1, inplace=True)
    data.dropna(subset=['currency', 'Amount'], inplace=True)
    data.dropna(subset=['ship-city', 'ship-state', 'ship-postal-code', 'ship-country'], inplace=True)
    data['promotion-ids'].fillna('No Promotion', inplace=True)
    return data

def main(filepath):
    """
    Main function to execute the retail sales analysis pipeline.
    """
    data = load_data(filepath)
    data = clean_data(data)

if __name__ == "__main__":
    filepath = '../data/raw/Amazon Sale Report.csv'
    main(filepath)