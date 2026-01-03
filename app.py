# starting streamlit
import streamlit as st # App making framework
import pandas as pd # data handling
import numpy as np # numerical operations/ computations
st.title("Car Dashboard Application")
st.write("This is a simple car dashboard application using Streamlit.") 
# text handling
st.text("This application allows users to explore car data and visualize various aspects of it.")
st.header("Car Data Overview")
st.subheader("Sample Car Data")
st.markdown("Below is a sample of car data including features like MPG, Cylinders, Horsepower, and Weight.")
st.success("Data loaded successfully!")
st.text_input("Enter your name:", "Type here...")
st.number_input("Enter your age:", min_value=0, max_value=100, value=25)
st.text_area("Describe your favorite car:", "Type here...")
st.date_input("Select a date:")
st.time_input("Select a time:")
st.file_uploader("Upload a car data file:")
# Display data
st.write("Here is a sample dataframe:")
st.write(range(0,10))
# Read data
data = pd.read_csv(r'customer_churn_dataset.csv')  # Assuming a CSV file 
st.write(data.head())
st.table(data.head(5))
st.bar_chart(data['monthly_charges'].value_counts())
st.line_chart(data['contract'].value_counts())
# description
st.write("Data Description:")
st.write(data.describe())
#Sidebar
st.sidebar.title("Car Dashboard Sidebar")
st.sidebar.write("Use the sidebar to navigate through different sections of the dashboard.")
st.sidebar.number_input("Enter your number", 0,50)
st.sidebar.text_area("Area of text")
st.sidebar.radio("Choose a Gender",["Male", "Female"])
st.sidebar.checkbox("Check me out")
st.sidebar.selectbox("Choose a Gender",["Male", "Female"])  
st.sidebar.multiselect("Choose a Gender", ["Male","Female"])
# Adding button
st.button("Send")
st.success("Done")
column1, column2, column3 = st.columns(3)
column1.metric("Temperature","70 °F","1.2 °F",delta_color="normal",border=True)
column2.metric("Wind", "9 mph","-8%", delta_color="inverse",border=True)
column3.metric("Humidity", "86%","4%", delta_color="off",border=True)
st.sidebar.radio("Navigation",["Home", "About","Contact"])
