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

def convert_df(df):
    return df.to_csv().encode('utf-8')
df1 = pd.read_csv('./data/addresses.csv')
csv = convert_df(df1)

st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='addresses.csv',
    mime='text/csv'
)

st.subheader("Checkbox")
agree = st.checkbox(
    "I agree to T&C"
)
if agree:
    st.write("Thanks to Agreeing our T and C!")

st.subheader("Radio Button")

qns = st.radio("What is your favorite Color",
               ("Red","Blue","Green","Yellow"))
if qns == "Red":
    st.write("You selected Red")
elif qns == "Blue":
    st.write("You selected Blue")
elif qns == "Green":
    st.write("You selected Green")
elif qns == "Yellow":
    st.write("You selected Yellow")
else:
    st.write("Select a valid color")

st.subheader("Select box")

option = st.selectbox("What is your favorite Color",
                      ("Red","Blue","Green","Yellow"))
st.write("You selected",option)

st.subheader("How Old are You?")
age = st.slider("Select your age",1,100)
st.write("I am ",age," years old")

st.subheader("Text Input")

name = st.text_input("Enter your name")
st.write("Your name is ",name)

st.subheader("Number Input")

year_of_birth = st.number_input("Year of Birth")
st.write("Your year is ",year_of_birth)

import datetime

dob = st.date_input(
                    "Enter your Birthday",
                    datetime.date(2000,1,1)
)
st.write("Your Date of birth is ",dob)