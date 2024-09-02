import streamlit as st
import pandas as pd
import numpy as np

# Title of the app
st.title('Simple Streamlit App')

# Text input
name = st.text_input('Enter your name')

# Display greeting
st.write(f'Hello, {name}!')

# Slider input
number = st.slider('Pick a number', 0, 100, 50)

# Display chosen number
st.write(f'You selected: {number}')

# Generate random data
data = np.random.randn(100) * number
df = pd.DataFrame(data, columns=['Values'])

# Line chart
st.line_chart(df)

# Show data table
st.dataframe(df)
