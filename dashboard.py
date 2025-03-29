import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
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

# Custom CSS for Light/Dark Mode Toggle
st.markdown(
    """
    <style>
        body { font-family: 'Arial', sans-serif; }
        .title { text-align: center; font-size: 36px; font-weight: bold; }
        .subtitle { text-align: center; font-size: 20px; color: #888; }
        .stApp { background-color: var(--background-color); color: var(--text-color); }
        .light { --background-color: #ffffff; --text-color: #000000; }
        .dark { --background-color: #181818; --text-color: #ffffff; }
    </style>
    """,
    unsafe_allow_html=True
)

# Light/Dark Mode Toggle
mode = st.sidebar.radio("Select Theme:", ["Light Mode", "Dark Mode"])
if mode == "Dark Mode":
    st.markdown('<body class="dark">', unsafe_allow_html=True)
else:
    st.markdown('<body class="light">', unsafe_allow_html=True)

# Title
st.markdown('<p class="title">📊 Expense Report Dashboard</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Analyze and track your expenses efficiently</p>', unsafe_allow_html=True)

# Summary Statistics
st.subheader("Summary Statistics")
st.write(df.describe())

# Expense Breakdown - Interactive Bar Chart
st.subheader("Expense Breakdown")
fig = px.bar(df[:10], x="Expenses", y="Item Cost", color="Item Cost", title="Top 10 Expenses")
st.plotly_chart(fig, use_container_width=True)

# Expense Distribution - Histogram
st.subheader("Expense Distribution")
fig2 = px.histogram(df, x="Item Cost", nbins=20, title="Distribution of Expenses", color_discrete_sequence=['blue'])
st.plotly_chart(fig2, use_container_width=True)

# Show Data Table
st.subheader("Full Data")
st.dataframe(df, use_container_width=True)
