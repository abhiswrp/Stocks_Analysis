import pandas as pd
import yfinance as yf
from datetime import datetime
from openpyxl import Workbook

# Step 1: Load the stocks and their weightages
def load_stock_data(csv_file):
    return pd.read_csv(csv_file)

# Step 2: Fetch stock data from Yahoo Finance
def fetch_stock_data(stock, start_date, end_date):
    try:
        data = yf.download(stock, start=start_date, end=end_date)
        return data[['Close']]  # Extracting closing prices
    except Exception as e:
        print(f"Error fetching data for {stock}: {e}")
        return None

# Step 3: Calculate investment and number of shares
def calculate_shares(stock_data, weightage, investment):
    stock_data['Investment'] = weightage * investment
    stock_data['Shares'] = stock_data['Investment'] / stock_data['Close']
    return stock_data

# Step 4: Main function to process all stocks
def process_stocks(csv_file, start_date, end_date, investment):
    stocks_data = load_stock_data(csv_file)
    results = []
    
    for _, row in stocks_data.iterrows():
        stock = row['stock']
        weightage = row['weightage']
        
        print(f"Processing stock: {stock}")
        stock_data = fetch_stock_data(stock, start_date, end_date)
        
        if stock_data is not None:
            stock_data = calculate_shares(stock_data, weightage, investment)
            stock_data['Stock'] = stock  # Add stock name for reference
            results.append(stock_data)
    
    # Combine all results into a single DataFrame
    final_data = pd.concat(results)
    return final_data

# Step 5: Write results to an Excel file
def write_to_excel(data, output_file):
    data.to_excel(output_file, index=False)
    print(f"Results written to {output_file}")

# User Inputs
if __name__ == "__main__":
    csv_file = "stocks.csv"
    start_date = input("Enter the start date (YYYY-MM-DD): ")
    end_date = input("Enter the end date (YYYY-MM-DD): ")
    investment = float(input("Enter the investment amount: "))
    
    result_data = process_stocks(csv_file, start_date, end_date, investment)
    output_file = "output/investment_results.xlsx"
    write_to_excel(result_data, output_file)
