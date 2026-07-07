import streamlit as st
import joblib



# Load model
model = joblib.load('Our LinearRegression Model.pkl')

# Page title
st.set_page_config(
    page_title="House Value Predictor",
    page_icon="🏠"
)

st.title("🏠 House Value Predictor")

# User input
median_income = st.number_input(
    "Enter Median Income",
    min_value=0.0,
    step=0.1
)

# Predict button
if st.button("Predict House Value"):
    prediction = model.predict([[median_income]])

    st.success(
        f"Predicted House Value: ${prediction[0]:,.2f}"
    )




