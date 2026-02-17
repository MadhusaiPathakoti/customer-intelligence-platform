import pandas as pd
from config.db_config import get_engine

def get_top_customers():
    conn = get_engine().connect()
    query = """
        SELECT c.name, SUM(o.total_amount) revenue
        FROM customers c
        JOIN orders o ON c.customer_id=o.customer_id
        GROUP BY c.name
        ORDER BY revenue DESC
        LIMIT 10;
    """
    return pd.read_sql(query, conn)

def get_monthly_revenue():
    conn = get_engine().connect()
    query = """
        SELECT DATE_FORMAT(order_date, '%Y-%m') month,
        SUM(total_amount) revenue
        FROM orders
        GROUP BY month;
    """
    return pd.read_sql(query, conn)