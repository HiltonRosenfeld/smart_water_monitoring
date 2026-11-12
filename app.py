import streamlit as st
import pandas as pd
import numpy as np

# 1. App Configuration & Title
st.set_page_config(page_title="Water Meter Monitoring App", page_icon="🚀")
st.title("🚀 Welcome to the Water Meter Monitoring App!")
st.write("Monitor and analyze your water meter data interactively.")

# 2. Sidebar Navigation / Settings
st.sidebar.header("Settings")
user_name = st.sidebar.text_input("Enter the customer name", "default_customer")

# 3. Interactive Greeting Section
st.header(f"Hello, {user_name}!")
st.write("Adjust the interactive elements below to see the stats update in real-time.")
st.write("Added Telemetry feature for real-time water meter monitoring.")

# 4. Interactive Widget: Slider & Dynamic Calculations
st.subheader("🔢 Dynamic Calculation")
number = st.slider("Select a value:", min_value=1, max_value=100, value=25)
st.write(f"The square of **{number}** is **{number ** 2}**.")

# 5. Data Generation & Visualization
st.subheader("📊 Interactive Chart")
chart_data = pd.DataFrame(
    np.random.randn(number, 2),
    columns=['Data Series A', 'Data Series B']
)
st.line_chart(chart_data)
