import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

# Navigation bar
nav = st.sidebar.radio("Navigation", ["About", "Predict"])

# Load the insurance dataset
df = pd.read_csv("insurance.csv")

if nav == "About":
    st.title("Health Insurance Premium Predictor")
    st.write("This application predicts health insurance premiums based on user input.")
    st.write("""
        ### Features:
        - Age
        - Gender
        - BMI
        - Number of children
        - Smoking status
        - Region
    """)

# Encode the insurance data for data analysis
df.replace({"sex": {"male": 0, "female": 1}}, inplace=True)
df.replace({"smoker": {"yes": 1, "no": 0}}, inplace=True)
df.replace({"region": {"southeast": 0, "southwest": 1, "northeast": 2, "northwest": 3}}, inplace=True)

# Store the features into a variable called "x"
x = df.drop(columns=["charges"], axis=1)

# The target variable "y" is charges
y = df["charges"]

# Use a pipeline to scale the features and apply RandomForestRegressor
model = make_pipeline(StandardScaler(), RandomForestRegressor())

# Fit the model
model.fit(x, y)

# Evaluate the model using cross-validation
scores = cross_val_score(model, x, y, cv=5, scoring='r2')
st.sidebar.write("Model R2 Score: ", scores.mean())

if nav == "Predict":
    st.title("Enter the details")

    # User inputs
    age = st.number_input("Age", step=1, min_value=0)
    sex = st.radio("Gender", ("Male", "Female"))
    s = 0 if sex == "Male" else 1
    bmi = st.number_input("BMI", min_value=0.0)
    children = st.number_input("Children", step=1, min_value=0)
    smoke = st.radio("Do you smoke?", ("Yes", "No"))
    sm = 1 if smoke == "Yes" else 0
    region = st.radio("Region", ("Southeast", "Southwest", "Northeast", "Northwest"))
    r = {"Southeast": 0, "Southwest": 1, "Northeast": 2, "Northwest": 3}[region]

    # Prediction
    if st.button("Predict"):
        try:
            result = model.predict([[age, s, bmi, children, sm, r]])
            st.success(f"The predicted insurance premium is ${result[0]:.2f}")
        except Exception as e:
            st.error(f"An error occurred: {e}")
