import streamlit as st

st.title("💳 Credit Card Fraud Detection")

st.write("App is running successfully 🚀")

amount = st.number_input("Enter Transaction Amount")

if st.button("Predict"):
    if amount > 1000:
        st.error("🚨 Fraud Detected")
    else:
        st.success("✅ Normal Transaction")