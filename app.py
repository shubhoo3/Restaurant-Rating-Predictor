import streamlit as st
import numpy as np
from sklearn.preprocessing import StandardScaler
import joblib

st.set_page_config(layout= "wide")

scaler = joblib.load("Scaler.pkl")

st.title("Restaurant Rating Prediction App")



st.caption("This app helps you to predict a restaurants review class")

st.divider()

averageCost = st.number_input("Please enter estimated average cost of two", min_value=50, max_value=999999, value=1000, step=200)

tableBooking = st.selectbox("Is Restaurant has table booking?", ["Yes", "No"])

onlineDelivery = st.selectbox("Is Restaurant has online booking", ["Yes", "No"])

priceRange = st.selectbox("From 1 to 5 rate the price range", [1, 2, 3, 4, 5])

predictButton = st.button("Review Predict!")

st.divider()

model = joblib.load("model.pkl")

bookingStatus = 1 if tableBooking == "Yes" else 0

deliveryStatus = 1 if onlineDelivery == "Yes" else 0

values = [[averageCost, bookingStatus, deliveryStatus, priceRange]]
X_values = np.array(values)

X = scaler.transform(X_values)

if predictButton:
    prediction = model.predict(X)

    st.write(prediction)

