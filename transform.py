import pandas as pd
import os

# ✅ Define file paths
input_file = "C:/Users/hp/Desktop/big data/onlineretail.xlsx"
output_file = "C:/Users/hp/Desktop/big data/transformed_data.xlsx"

# ✅ Check if file exists before proceeding
if not os.path.exists(input_file):
    raise FileNotFoundError(f"❌ File not found: {input_file}")

# ✅ Load the dataset (fixing missing engine issue)
df = pd.read_excel(input_file, engine='openpyxl')

# ✅ Standardize column names (lowercase, remove spaces)
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# ✅ Handle missing values (drop rows where InvoiceDate, Price, Customer ID, or Country is missing)
df.dropna(subset=['invoicedate', 'price', 'customer_id', 'country'], inplace=True)

# ✅ Convert InvoiceDate to datetime format
df['invoicedate'] = pd.to_datetime(df['invoicedate'], errors='coerce')

# ✅ Ensure Price is numeric
df['price'] = pd.to_numeric(df['price'], errors='coerce')

# ✅ Remove negative prices
df = df[df['price'] > 0]

# ✅ Save transformed data
df.to_excel(output_file, index=False, engine='openpyxl')

print(f"✅ Transformation complete! Data saved to: {output_file}")
print(df.head())  # Display first few rows
