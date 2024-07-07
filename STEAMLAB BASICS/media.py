from PIL import Image
import streamlit as st

st.subheader('Image Display using Strealilt')
image = Image.open('./image/india_won.jpeg')
st.image(image, caption='India 2024 world cup image', use_column_width=True)

st.subheader('Video Play using Strealmit')

video = open('./image/sample.mp4','rb')
video_bytes = video.read()
st.video(video_bytes)
