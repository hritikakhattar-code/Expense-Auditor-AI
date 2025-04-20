
import streamlit as st
import pandas as pd
import os

# ✅ Set page config FIRST (must be first Streamlit call)
st.set_page_config(page_title="Expense Auditor")

# ✅ Streamlit app title and description
st.title("AI-Powered Expense Report Auditor")
st.write("Upload your expense CSV and review flagged anomalies below.")

# File uploader for CSV file
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(uploaded_file)
    
    # Show the dataframe preview
    st.subheader("Preview of Uploaded Data")
    st.write(df.head())
    
    # --- Add your analysis or processing code below ---
    
    # Example: Anomaly detection (simple)
    st.subheader("Flagged Anomalies")
    anomalies = df[df['Amount'] > 5000]  # Example: Flag expenses over 5000
    st.write(anomalies)

    # --- Any additional processing and visualization logic can go here ---
    
    # Example: Plotting
    st.subheader("Expense Distribution")
    st.bar_chart(df['Amount'])

    # --- You can also add other Streamlit widgets like filters, charts, etc. ---
else:
    st.write("Please upload a CSV file to begin.")
