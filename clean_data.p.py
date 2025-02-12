import pandas as pd

# ✅ Load extracted data
file_path = "C:/Users/hp/Desktop/big data/extracted_data.xlsx"
df = pd.read_excel(file_path, engine="openpyxl")

# ✅ Print column names for debugging
print("📌 Column Names:", df.columns)

# ✅ Ensure correct column names (update if needed)
expected_columns = ['InvoiceDate', 'Price', 'Customer ID', 'Country']
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')  # Convert to lowercase & remove spaces
print("✅ Standardized Columns:", df.columns)

# ✅ Verify corrected names
if 'invoicedate' not in df.columns or 'customer_id' not in df.columns:
    raise KeyError(f"⚠️ Column names mismatch! Available columns: {df.columns}")

# ✅ Handle missing values (drop rows with missing InvoiceDate & Customer ID)
df.dropna(subset=['invoicedate', 'customer_id'], inplace=True)

# ✅ Remove duplicate rows
df.drop_duplicates(inplace=True)

# ✅ Convert InvoiceDate to datetime
df['invoicedate'] = pd.to_datetime(df['invoicedate'], errors='coerce')

# ✅ Ensure numeric fields are correct
df['price'] = pd.to_numeric(df['price'], errors='coerce')

# ✅ Save cleaned data
cleaned_file_path = "C:/Users/hp/Desktop/big data/cleaned_data.xlsx"
df.to_excel(cleaned_file_path, index=False, engine="openpyxl")

print(f"✅ Data cleaning complete! Cleaned file saved as: {cleaned_file_path}")
print(df.head())  # Show cleaned data
