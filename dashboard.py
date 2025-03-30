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

# Sidebar Theme Toggle
st.sidebar.markdown("### ⚙️ Appearance Settings")
mode = st.sidebar.radio("Select Theme:", ["Light Mode", "Dark Mode"], horizontal=True)

# Define Color Themes
if mode == "Dark Mode":
    primary_bg = "#181818"
    secondary_bg = "#222222"
    text_color = "#ffffff"
    plotly_theme = "plotly_dark"
else:
    primary_bg = "#ffffff"
    secondary_bg = "#f8f9fa"
    text_color = "#000000"
    plotly_theme = "plotly"

# Apply Custom CSS for Light & Dark Mode
custom_css = f"""
    <style>
        body, .stApp {{
            background-color: {primary_bg};
            color: {text_color};
        }}
        .sidebar .sidebar-content {{
            background-color: {secondary_bg};
            color: {text_color};
        }}
        .stDataFrame, .dataframe {{
            color: {text_color} !important;
        }}
    </style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# Dashboard Title
st.title("📊 Expense Report Dashboard")
st.write("Analyze and track your expenses efficiently")

# Summary Statistics
st.subheader("📌 Summary Statistics")
st.write(df.describe())

# Expense Breakdown - Interactive Bar Chart (Plotly)
st.subheader("💰 Expense Breakdown")
fig = px.bar(df[:10], x="Expenses", y="Item Cost", color="Item Cost",
             title="Top 10 Expenses", template=plotly_theme)
st.plotly_chart(fig, use_container_width=True)

# Expense Distribution - Histogram (Plotly)
st.subheader("📉 Expense Distribution")
fig2 = px.histogram(df, x="Item Cost", nbins=20, title="Distribution of Expenses",
                    color_discrete_sequence=['blue'], template=plotly_theme)
st.plotly_chart(fig2, use_container_width=True)

# Show Data Table (Styled)
st.subheader("📜 Full Data")
st.dataframe(df.style.set_properties(**{'background-color': primary_bg, 'color': text_color}), use_container_width=True)
