import streamlit as st
import requests
import json

st.title("Clara Agent Generator")

transcript = st.text_area("Paste transcript")

account_id = st.text_input("Account ID")

if st.button("Generate Agent"):

    data = {
        "account_id": account_id,
        "transcript": transcript
    }

    response = requests.post(
        "http://127.0.0.1:8001/process-demo",
        json=data
    )

    result = response.json()

    st.subheader("V1 Agent")
    st.json(result["v1_agent"])

    st.subheader("V2 Agent")
    st.json(result["v2_agent"])