import streamlit as st
import pandas as pd
import numpy as np

st.header("This is a INPUT Widget")

st.subheader("This is a Simple Input Button")
if st.button("Say hello"):
    st.write("Hey hello there")
else:
    st.write("Goodbye")

st.subheader("This is a Download Button")

text= "Here is text to download"
st.download_button("Download text",text)

with open("./image/india_won.jpeg","rb") as file:
    btn = st.download_button(
        label="India 2024 world cup image",
        data=file,
        file_name="india_won.jpeg",
        mime="image/jpeg"
    )



