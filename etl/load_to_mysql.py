import pandas as pd
from sqlalchemy import text
from config.db_config import get_engine

engine = get_engine()

file_path = "../data/ecommerce_data.xlsx"


def table_has_data(table_name):
    """Check if table already has rows"""
    with engine.connect() as conn:
        result = conn.execute(text(f"SELECT COUNT(*) FROM {table_name}"))
        count = result.scalar()
        return count > 0


def load_table(sheet_name, table_name):
    """Load Excel sheet to MySQL only if table empty"""

    if table_has_data(table_name):
        print(f"⏭ Skipping {table_name} — data already exists")
        return

    df = pd.read_excel(file_path, sheet_name=sheet_name)
    df.to_sql(table_name, engine, if_exists="append", index=False)
    print(f"✅ Loaded data into {table_name}")


# Run ETL
load_table("customers", "customers")
load_table("products", "products")
load_table("orders", "orders")
load_table("order_items", "order_items")

print("\n🎯 ETL process completed")
