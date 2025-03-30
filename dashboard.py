import streamlit as st
import pandas as pd
import plotly.express as px

# Load Data
df = pd.read_excel("Improved_Expenses_Report.xlsx")

# Set Page Configuration
st.set_page_config(
    page_title="Expense Report Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Dashboard Title
st.title("📊 Expense Report Dashboard")
st.write("Analyze and track your expenses efficiently")

# Summary Statistics
st.subheader("📌 Summary Statistics")
st.write(df.describe())

# Expense Breakdown - Interactive Bar Chart (Plotly)
st.subheader("💰 Expense Breakdown")
fig = px.bar(df[:10], x="Expenses", y="Item Cost", color="Item Cost", title="Top 10 Expenses")
st.plotly_chart(fig, use_container_width=True)

# Expense Distribution - Histogram (Plotly)
st.subheader("📉 Expense Distribution")
fig2 = px.histogram(df, x="Item Cost", nbins=20, title="Distribution of Expenses", color_discrete_sequence=['blue'])
st.plotly_chart(fig2, use_container_width=True)

# Show Data Table
st.subheader("📜 Full Data")
st.dataframe(df, use_container_width=True)
