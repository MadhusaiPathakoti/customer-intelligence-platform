import streamlit as st
from services.analytics_service import get_top_customers, get_monthly_revenue

st.title("Customer Intelligence Platform")

st.header("Top Customers")
customers = get_top_customers()
st.dataframe(customers)

st.header("Monthly Revenue")
revenue = get_monthly_revenue()
st.bar_chart(revenue.set_index("month"))
