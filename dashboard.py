import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load Data
df = pd.read_excel("Improved_Expenses_Report.xlsx")

# Streamlit App
st.title("📊 Expense Report Dashboard")

# Summary
st.write("### Summary Statistics")
st.write(df.describe())

# Bar Chart
st.write("### Expense Breakdown")
fig, ax = plt.subplots()
ax.bar(df["Expenses"][:10], df["Item Cost"][:10], color="skyblue")
plt.xticks(rotation=45)
st.pyplot(fig)

# Show Data
st.write("### Full Data")
st.dataframe(df)
