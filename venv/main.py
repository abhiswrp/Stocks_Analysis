# import pandas as pd
# def process_stocks(file_path, investment):
#     try:
#         data = pd.read_csv(file_path)
#         print("Columns in CSV:", data.columns)
#     except FileNotFoundError:
#         print(f"Error: The file {file_path} was not found.")
#         return None
#     if 'Ticker' not in data.columns or 'Weightage' not in data.columns:
#         print("Error: Required columns (Ticker, Weightage) are missing.")
#         return None
#     total_weightage = data['Weightage'].sum()
#     if total_weightage == 0:
#         print("Error: Total weightage is zero, cannot distribute investment.")
#         return None
#     data['Investment'] = (data['Weightage'] / total_weightage) * investment
#     data['Shares'] = data['Investment']
#     return data[['Ticker', 'Weightage', 'Investment', 'Shares']]

# if __name__ == "__main__":
#     csv_file = "data/stocks_data.csv"
#     investment = float(input("Enter the investment amount: "))
#     result_data = process_stocks(csv_file, investment)
#     if result_data is not None:
#         print("\nProcessed Data:\n", result_data)
#         result_data.to_csv("processed_stocks.csv", index=False)
#         print("\nProcessed data saved to 'processed_stocks.csv'.")



# import pandas as pd
# import os

# def process_stocks(file_path, investment, start_date, end_date):
#     # Load CSV file
#     try:
#         data = pd.read_csv(file_path)
#         print("Columns in CSV:", data.columns)
#     except FileNotFoundError:
#         print(f"Error: The file {file_path} was not found.")
#         return None

#     # Check for required columns
#     if 'Ticker' not in data.columns or 'Weightage' not in data.columns:
#         print("Error: Required columns (Ticker, Weightage) are missing.")
#         return None

#     # Calculate total weightage
#     total_weightage = data['Weightage'].sum()

#     if total_weightage == 0:
#         print("Error: Total weightage is zero, cannot distribute investment.")
#         return None

#     # Distribute the investment based on weightage
#     data['Investment'] = (data['Weightage'] / total_weightage) * investment
#     data['Shares'] = data['Investment']  # Assuming no price data, shares = investment (for demonstration)

#     # Add From Date and To Date columns
#     data['From Date'] = start_date
#     data['To Date'] = end_date

#     # Prepare final result with selected columns
#     result_data = data[['Ticker', 'Weightage', 'From Date', 'To Date']]

#     return result_data

# # Main logic
# if __name__ == "__main__":
#     # Define the file paths
#     csv_file = "data/stocks_data.csv"
#     output_folder = "output"
    
#     # Ensure output folder exists
#     os.makedirs(output_folder, exist_ok=True)
    
#     # Get input from user
#     investment = float(input("Enter the investment amount: "))
#     start_date = input("Enter the start date (YYYY-MM-DD): ")
#     end_date = input("Enter the end date (YYYY-MM-DD): ")

#     # Process the data
#     result_data = process_stocks(csv_file, investment, start_date, end_date)

#     # Save the results to an Excel file
#     if result_data is not None:
#         output_file = os.path.join(output_folder, "investment_results.xlsx")
#         result_data.to_excel(output_file, index=False)
#         print(f"\nProcessed data saved to '{output_file}'.")



# import pandas as pd

# def process_stocks(file_path, start_date, end_date, investment):
#     # Load CSV file
#     try:
#         data = pd.read_csv(file_path)
#         print("Columns in CSV:", data.columns)
#     except FileNotFoundError:
#         print(f"Error: The file {file_path} was not found.")
#         return None

#     # Check required columns: Ticker, Weightage
#     required_columns = ['Ticker', 'Weightage']
#     for column in required_columns:
#         if column not in data.columns:
#             print(f"Error: Missing required column '{column}' in the CSV file.")
#             return None

#     # Calculate investment per ticker based on weightage
#     data['Investment'] = data['Weightage'] / 100 * investment

#     # Store results in a new DataFrame
#     analysis_data = []

#     for _, row in data.iterrows():
#         ticker = row['Ticker']
#         weightage = row['Weightage']
#         investment_for_ticker = row['Investment']

#         # Assuming start_date and end_date are the same for each ticker in the analysis
#         analysis_data.append({
#             'Ticker': ticker,
#             'Weightage': weightage,
#             'From Date': start_date,
#             'To Date': end_date,
#             'Investment for Ticker': investment_for_ticker,
#         })

#     # Convert analysis data into a DataFrame
#     analysis_df = pd.DataFrame(analysis_data)

#     return analysis_df

# # Main logic
# if __name__ == "__main__":
#     csv_file = "data/stocks_data.csv"
#     start_date = input("Enter the start date (YYYY-MM-DD): ")
#     end_date = input("Enter the end date (YYYY-MM-DD): ")
#     investment = float(input("Enter the investment amount: "))

#     try:
#         start_date = pd.to_datetime(start_date)
#         end_date = pd.to_datetime(end_date)
#     except ValueError:
#         print("Invalid date format. Please use YYYY-MM-DD.")
#         exit(1)

#     result_data = process_stocks(csv_file, start_date, end_date, investment)

#     if result_data is not None:
#         print("\nProcessed Data:\n", result_data)

#         # Save to Excel in the output folder
#         output_path = "output/investment_results.xlsx"
#         result_data.to_excel(output_path, index=False)
#         print(f"\nProcessed data saved to '{output_path}'.")



import pandas as pd
def process_stocks(file_path, start_date, end_date, investment):
    try:
        data = pd.read_csv(file_path)
        print("Columns in CSV:", data.columns)
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return None
    required_columns = ['Ticker', 'Weightage']
    for column in required_columns:
        if column not in data.columns:
            print(f"Error: Missing required column '{column}' in the CSV file.")
            return None
    data['Investment'] = data['Weightage'] / 100 * investment
    analysis_data = []
    for _, row in data.iterrows():
        ticker = row['Ticker']
        weightage = row['Weightage']
        investment_for_ticker = row['Investment']
        analysis_data.append({
            'Ticker': ticker,
            'Weightage': weightage,
            'From Date': start_date,
            'To Date': end_date,
            'Investment for Ticker': investment_for_ticker,
        })
    analysis_df = pd.DataFrame(analysis_data)
    analysis_df.rename(columns={'From Date': str(start_date.date()), 'To Date': str(end_date.date())}, inplace=True)
    return analysis_df

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
        output_path = "output/investment_results.xlsx"
        result_data.to_excel(output_path, index=False)
        print(f"\nProcessed data saved to '{output_path}'.")
