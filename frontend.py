import streamlit as st
import requests

# Streamlit UI
st.title("User Data Form")

username = st.text_input("Enter your username:", "")
age = st.number_input("Enter your age:", min_value=1, step=1)

if st.button("Submit"):
    try:
        response = requests.post("http://localhost:8000/submit/", json={"username": username, "age": age})
        if response.status_code == 200:
            st.success("Data submitted successfully")
        else:
            st.error("Error submitting data")
    except Exception as e:
        st.error(f"Error: {e}")

st.subheader("Submitted Data")

try:
    data_response = requests.get("http://localhost:8000/data/")
    if data_response.status_code == 200:
        data = data_response.json().get("data", [])
        st.table(data)
    else:
        st.error("Failed to load data")
except Exception as e:
    st.error(f"Error: {e}")
