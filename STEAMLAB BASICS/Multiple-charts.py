import streamlit as st
import pandas as pd
import numpy as np

st.header("This is a Multiple Charts Lab")
st.subheader("This is a Line Chart")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)
st.line_chart(chart_data)

st.subheader("This is a Area Chart")
st.area_chart(chart_data)

st.subheader("This is a Bar Chart")
st.bar_chart(chart_data)

st.write("This is a Scatter Chart")
st.scatter_chart(chart_data)

st.write("This is above chart is made from below dataframe")
st.dataframe(chart_data)

#Lets try to plot PYPLOT
st.subheader("This is a Pyplot Chart")
import matplotlib.pyplot as plt
arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)
st.pyplot(fig)

