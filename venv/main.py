import pandas as pd

def process_stocks(file_path, start_date, end_date, investment):
    # Load CSV file
    try:
        data = pd.read_csv(file_path)
        print("Columns in CSV:", data.columns)
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return None

    # Check required columns
    required_columns = ['Ticker', 'Date', 'Price']
    for column in required_columns:
        if column not in data.columns:
            print(f"Error: Missing required column '{column}' in the CSV file.")
            return None

    # Filter by date range
    data['Date'] = pd.to_datetime(data['Date'])
    filtered_data = data[(data['Date'] >= start_date) & (data['Date'] <= end_date)]

    if filtered_data.empty:
        print("No data found for the specified date range.")
        return None

    # Simple analysis: Calculate total investment distribution
    filtered_data['Investment'] = investment / len(filtered_data)
    filtered_data['Shares'] = filtered_data['Investment'] / filtered_data['Price']
    
    return filtered_data[['Ticker', 'Date', 'Price', 'Investment', 'Shares']]

# Main logic
if __name__ == "__main__":
    csv_file = "data/stocks_data.csv"
    start_date = input("Enter the start date (YYYY-MM-DD): ")
    end_date = input("Enter the end date (YYYY-MM-DD): ")
    investment = float(input("Enter the investment amount: "))

    try:
        start_date = pd.to_datetime(start_date)
        end_date = pd.to_datetime(end_date)
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        exit(1)

    result_data = process_stocks(csv_file, start_date, end_date, investment)

    if result_data is not None:
        print("\nProcessed Data:\n", result_data)
        result_data.to_csv("processed_stocks.csv", index=False)
        print("\nProcessed data saved to 'processed_stocks.csv'.")
