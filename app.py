import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("model.pkl")

st.title("🔐 Network Intrusion Detection System")

st.write("Enter session details to check if activity is malicious")

# User Inputs
session_duration = st.number_input("Session Duration", min_value=1)
bytes_sent = st.number_input("Bytes Sent", min_value=0)
bytes_received = st.number_input("Bytes Received", min_value=0)
failed_logins = st.number_input("Failed Logins", min_value=0)
country_risk_score = st.slider("Country Risk Score", 1, 100)
is_vpn = st.selectbox("VPN Used", [0, 1])

# Predict Button
if st.button("Check Activity"):

    # Create dataframe
    input_data = pd.DataFrame({
        'session_duration': [session_duration],
        'bytes_sent': [bytes_sent],
        'bytes_received': [bytes_received],
        'failed_logins': [failed_logins],
        'country_risk_score': [country_risk_score],
        'is_vpn': [is_vpn]
    })

    # Prediction
    prediction = model.predict(input_data)
    prob = model.predict_proba(input_data)

    # Output
    if prediction[0] == 1:
        st.error("⚠️ Malicious Activity Detected")
    else:
        st.success("✅ Safe Session")

    st.write(f"Confidence: {round(max(prob[0]) * 100, 2)}%")