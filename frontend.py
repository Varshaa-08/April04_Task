# frontend.py (Streamlit UI)
import streamlit as st
import requests

st.title("User Data Form")

username = st.text_input("Enter your username:")
age = st.number_input("Enter your age:", min_value=1, step=1)

if st.button("Submit"):
    response = requests.post("http://localhost:8000/submit/", json={"username": username, "age": age})
    if response.status_code == 200:
        st.success("Data submitted successfully!")
    else:
        st.error("Error submitting data")

st.subheader("Submitted Data")
data = requests.get("http://localhost:8000/data/").json()
st.table(data)
