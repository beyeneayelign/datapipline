import pandas as pd

# ✅ Define file path
file_path = "C:/Users/hp/Desktop/big data/onlineretail.xlsx"

# ✅ Load the dataset
df = pd.read_excel(file_path, engine="openpyxl")

# ✅ Print column names to verify
print("📌 Column Names:", df.columns)

# ✅ Select relevant columns (update based on your file)
columns_to_extract = ["InvoiceDate", "Price", "Customer ID", "Country"]

# ✅ Convert column names to lowercase with underscores
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# ✅ Extract only required columns
extracted_df = df[["invoicedate", "price", "customer_id", "country"]]

# ✅ Save extracted data
extracted_file_path = "C:/Users/hp/Desktop/big data/extracted_data.xlsx"
extracted_df.to_excel(extracted_file_path, index=False, engine="openpyxl")

print(f"✅ Data extraction complete! Extracted file saved as: {extracted_file_path}")
print(extracted_df.head())  # Show first few rows
