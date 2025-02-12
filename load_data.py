import pandas as pd
import os

# ✅ Use the correct file path
file_path = "C:/Users/hp/Desktop/big data/onlineretail.xlsx"

# ✅ Check if the file exists before loading
if not os.path.exists(file_path):
    raise FileNotFoundError(f"❌ File not found: {file_path}")

# ✅ Load the Excel file (NOT CSV!)
df = pd.read_excel(file_path, engine='openpyxl')

# ✅ Display the first few rows
print("✅ File loaded successfully!")
print(df.head())
