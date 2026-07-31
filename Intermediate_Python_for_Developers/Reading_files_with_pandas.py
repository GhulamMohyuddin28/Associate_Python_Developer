# Import pandas
import pandas as pd

# Read in sales.csv
sales_df = pd.read_csv("sales.csv")

# Display the DataFrame info
print("--- DataFrame Info ---")
print(sales_df.info())
