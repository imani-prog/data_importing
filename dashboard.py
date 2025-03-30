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

# Apply Theme Based on User Selection
st.sidebar.markdown("### Appearance Settings")
mode = st.sidebar.radio("Select Theme:", ["Light Mode", "Dark Mode"], horizontal=True)

# Custom CSS for Dark and Light Mode
if mode == "Dark Mode":
    dark_mode_style = """
        <style>
            body { background-color: #181818; color: #ffffff; }
            .stApp { background-color: #181818; color: #ffffff; }
            .sidebar .sidebar-content { background-color: #222222; color: #ffffff; }
            .stDataFrame { color: #ffffff !important; }
        </style>
    """
    st.markdown(dark_mode_style, unsafe_allow_html=True)
else:
    light_mode_style = """
        <style>
            body { background-color: #ffffff; color: #000000; }
            .stApp { background-color: #ffffff; color: #000000; }
        </style>
    """
    st.markdown(light_mode_style, unsafe_allow_html=True)

# Dashboard Title
st.title("📊 Expense Report Dashboard")
st.write("Analyze and track your expenses efficiently")

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
