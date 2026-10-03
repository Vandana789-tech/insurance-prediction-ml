import streamlit as st
import requests

API_URL="http://127.0.0.1:8000/predict"
st.title("Insurance premimum category predictor")

st.markdown("enter your details in below: ")

age=st.number_input("age",min_value=1,max_value=119,value=30)
weight=st.number_input("weight",min_value=1,max_value=119,value=56)
height=st.number_input("height",min_value=0.5,max_value=2.5,value=2.0)
income_lpa=st.number_input("income_lpa",min_value=1,value=10)
smoker=st.selectbox("Are you a smoker ",options=[True,False])
city=st.text_input("city",value="Mumbai")
occupation = st.selectbox(
    "Occupation",
    [
        "retired",
        "freelancer",
        "student",
        "government_job",
        "business_owner",
        "unemployed",
        "private_job"
    ]
)

if st.button("predict premium category"):
    input_data={
        "age":age,
        "weight":weight,
        "height":height,
        "income_lpa":income_lpa,
        "smoker":smoker,
        "city":city,
        "occupation":occupation
    }

    try:
        response=requests.post(API_URL,json=input_data)
        if response.status_code==200:
            result=response.json()
            st.success(f"predicted insurance premium categary : **{result['predicted_category']}**")
        else:
            st.error(f"API Error: {response.status_code}-{response.text}")

    except requests.exceptions.ConnectionError:
        st.error("could not connect to the FastAPI server, Make sure its running on the port 8000.")