import pandas as pd
import matplotlib.pyplot as plt
#import seaborn as sns
from sqlalchemy import create_engine

# Database connection details
db_name = "bigdata_db"
db_user = "bigdata_user"
db_password = "123"
db_host = "localhost"
db_port = "5432"

# Create a PostgreSQL connection
engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')

# Define table name
table_name = "onlineretail_data"

# Load data from PostgreSQL
df = pd.read_sql(f"SELECT * FROM {table_name}", engine)

# Visualization: Sales Trend Over Time
if 'InvoiceDate' in df.columns and 'UnitPrice' in df.columns and 'Quantity' in df.columns:
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    df['Sales'] = df['UnitPrice'] * df['Quantity']
    sales_trend = df.groupby(df['InvoiceDate'].dt.date)['Sales'].sum()

    plt.figure(figsize=(12, 6))
    sns.lineplot(x=sales_trend.index, y=sales_trend.values)
    plt.title("Sales Trend Over Time")
    plt.xlabel("Date")
    plt.ylabel("Total Sales")
    plt.xticks(rotation=45)
    plt.show()

print("Visualization completed.")
