import streamlit as st
import pandas as pd
import numpy as np
import pickle 

# Load the model
model = pickle.load(open('models.pkl', 'rb'))

# App header
st.header("Calories Burner Tracking App")

# User inputs
gender = st.selectbox("Gender: ", ("Male", "Female"))
age = st.number_input("Age: ", min_value=0, step=1)
height = st.number_input("Height (in cm): ", min_value=0.0)
weight = st.number_input("Weight (in kg): ", min_value=0.0)
duration = st.number_input("Workout Duration (in minutes): ", min_value=0.0)
heart_rate = st.number_input("Heart Rate (in bpm): ", min_value=0, step=1)
body_temperature = st.number_input("Body Temperature (in °C): ", min_value=0.0)

# Convert gender to numerical value
g = 0 if gender == "Male" else 1

# Prepare input data for prediction
input_data = pd.DataFrame(
    columns=['Gender','Age','Height','Weight','Duration','Heart_Rate','Body_Temp'], 
    data=np.array([g, age, height, weight, duration, heart_rate, body_temperature]).reshape(1, 7)
)

# Prediction
if st.button("Predict"):
    try:
        prediction = model.predict(input_data)
        st.success(f"Calories Burned is: {prediction[0]:.2f} kcal")
    except Exception as e:
        st.error(f"Error in prediction: {e}")
