import streamlit as st
import requests
import pandas as pd

st.title("User Data Form")

# Input fields
username = st.text_input("Enter your username:", "")
age = st.number_input("Enter your age:", min_value=1, step=1)

if st.button("Submit"):
    try:
        response = requests.post("http://backend-service:8000/submit/", json={"username": username, "age": age})
        if response.status_code == 200:
            st.success("Data submitted successfully")
        else:
            st.error("Error submitting data")
    except Exception as e:
        st.error(f"Error: {e}")

st.subheader("Submitted Data")

try:
    data_response = requests.get("http://backend-service:8000/data/")
    if data_response.status_code == 200:
        data = data_response.json().get("data", [])
        
        # Convert to DataFrame for better table display
        df = pd.DataFrame(data)
        if not df.empty:
            st.table(df)
        else:
            st.write("No data available.")
    else:
        st.error("Failed to load data")
except Exception as e:
    st.error(f"Error: {e}")

