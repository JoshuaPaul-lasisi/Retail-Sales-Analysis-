# Import necessary libraries
import pandas as pd
import numpy as np
import os

def load_data(filepath):
    """
    Load the sales data from a CSV file and perform initial data checks.
    """
    # Load data with specified dtype and low_memory option
    data = pd.read_csv(filepath, low_memory=False, dtype={'ship-postal-code': str})
    
    # Explicitly parse dates
    data['Date'] = pd.to_datetime(data['Date'], errors='coerce')
    
    # Drop unnecessary column
    data.drop(columns='Unnamed: 22', inplace=True, errors='ignore')
    
    return data

def clean_data(data):
    """
    Clean the sales data by handling zero quantities, missing values, and irrelevant columns.
    """
    # Filter out rows where Qty is zero
    data = data[data['Qty'] != 0]
    
    # Drop irrelevant columns
    data.drop(columns='fulfilled-by', inplace=True, errors='ignore')
    
    # Drop rows with missing values in specified columns
    data.dropna(subset=['currency', 'Amount'], inplace=True)
    data.dropna(subset=['ship-city', 'ship-state', 'ship-postal-code', 'ship-country'], inplace=True)
    
    # Use .loc[] to avoid SettingWithCopyWarning
    data.loc[:, 'promotion-ids'] = data['promotion-ids'].fillna('No Promotion')
    
    return data

def main(filepath):
    """
    Main function to execute the retail sales analysis pipeline.
    """
    data = load_data(filepath)
    cleaned_data = clean_data(data)
    
    # Save cleaned data to ../data/processed folder
    processed_folder = '../data/processed'
    os.makedirs(processed_folder, exist_ok=True)  # Ensure the folder exists
    cleaned_data.to_csv(f'{processed_folder}/cleaned_sales_data.csv', index=False)
    print(f'Cleaned data saved to {processed_folder}/cleaned_sales_data.csv')

if __name__ == "__main__":
    filepath = '../data/raw/Amazon Sale Report.csv'
    main(filepath)