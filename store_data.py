import pandas as pd
import psycopg2
from sqlalchemy import create_engine
import os

# Database connection details
db_name = "bigdata_db"  # Database name
db_user = "bigdata_user"  # PostgreSQL username
db_password = "123"  # PostgreSQL password (make sure it's correct)
db_host = "localhost"  # Running locally
db_port = "5432"  # Default PostgreSQL port

# ✅ Check if the file exists
cleaned_file_path = "C:/Users/hp/Desktop/big data/onlineretail.xlsx"  # Update with the correct path
if not os.path.exists(cleaned_file_path):
    raise FileNotFoundError(f"File not found: {cleaned_file_path}")

# ✅ Read CSV or Excel file based on extension
if cleaned_file_path.endswith(".csv"):
    df = pd.read_csv(cleaned_file_path)
elif cleaned_file_path.endswith(".xlsx"):
    df = pd.read_excel(cleaned_file_path)
else:
    raise ValueError("Unsupported file format. Please provide a .csv or .xlsx file.")

# ✅ Create a PostgreSQL connection
try:
    engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')
except Exception as e:
    print("Database connection error:", e)
    exit()

# ✅ Correct the table name (change this to your actual table name)
table_name = "onlineretail_data"  # Example: Change this to your correct table name

# ✅ Store data in PostgreSQL
try:
    df.to_sql(table_name, engine, if_exists='replace', index=False)
    print(f"✅ Data successfully stored in PostgreSQL table: {table_name}")
except Exception as e:
    print("❌ Error storing data:", e)
