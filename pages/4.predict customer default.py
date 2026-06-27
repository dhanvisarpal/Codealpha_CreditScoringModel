import joblib
import streamlit as st
import pandas as pd

model= joblib.load("models/random_forest_model.pkl")
st.success("Model loaded successfully")

st.info("""
Enter the customer's financial and repayment details below.
The Random Forest model will estimate the probability of
default on the next credit card payment.
""")

# Customer Information

with st.expander("Customer Information"):
 limit_bal = st.number_input(
    "Credit Limit (LIMIT_BAL)",
    min_value=0,
    value=50000
)

 sex = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

 education = st.selectbox(
    "Education Level",
    [
        "Graduate School",
        "University",
        "High School",
        "Others"
    ]
)

 marriage = st.selectbox(
    "Marriage Status",
    [
        "Married",
        "Single",
        "Others"
    ]
)

 age = st.number_input(
    "Age",
    min_value=18,
    max_value=100,
    value=30
)

# Convert text to model values

 sex = 1 if sex == "Male" else 2

 education_map = {
    "Graduate School": 1,
    "University": 2,
    "High School": 3,
    "Others": 4
}

 education = education_map[education]

 marriage_map = {
    "Married": 1,
    "Single": 2,
    "Others": 3
}

 marriage = marriage_map[marriage]

with st.expander("Repayment History"):
 st.subheader("Repayment History")

 pay_0 = st.number_input("PAY_0 (Recent Repayment Status)", value=0)

 pay_2 = st.number_input("PAY_2", value=0)

 pay_3 = st.number_input("PAY_3", value=0)

 pay_4 = st.number_input("PAY_4", value=0)

 pay_5 = st.number_input("PAY_5", value=0)

 pay_6 = st.number_input("PAY_6", value=0)

with st.expander(" Bill Amounts"):
 st.subheader("Bill Amounts")

 bill_amt1 = st.number_input("BILL_AMT1", value=0)

 bill_amt2 = st.number_input("BILL_AMT2", value=0)

 bill_amt3 = st.number_input("BILL_AMT3", value=0)

 bill_amt4 = st.number_input("BILL_AMT4", value=0)

 bill_amt5 = st.number_input("BILL_AMT5", value=0)

 bill_amt6 = st.number_input("BILL_AMT6", value=0)

with st.expander("Payment Amounts"):
 st.subheader("Payment Amounts")

 pay_amt1 = st.number_input("PAY_AMT1", value=0)

 pay_amt2 = st.number_input("PAY_AMT2", value=0)

 pay_amt3 = st.number_input("PAY_AMT3", value=0)

 pay_amt4 = st.number_input("PAY_AMT4", value=0)

 pay_amt5 = st.number_input("PAY_AMT5", value=0)

 pay_amt6 = st.number_input("PAY_AMT6", value=0)

if st.button("Predict"):

    input_data = pd.DataFrame([{
        "LIMIT_BAL": limit_bal,
        "SEX": sex,
        "EDUCATION": education,
        "MARRIAGE": marriage,
        "AGE": age,
        "PAY_0": pay_0,
        "PAY_2": pay_2,
        "PAY_3": pay_3,
        "PAY_4": pay_4,
        "PAY_5": pay_5,
        "PAY_6": pay_6,
        "BILL_AMT1": bill_amt1,
        "BILL_AMT2": bill_amt2,
        "BILL_AMT3": bill_amt3,
        "BILL_AMT4": bill_amt4,
        "BILL_AMT5": bill_amt5,
        "BILL_AMT6": bill_amt6,
        "PAY_AMT1": pay_amt1,
        "PAY_AMT2": pay_amt2,
        "PAY_AMT3": pay_amt3,
        "PAY_AMT4": pay_amt4,
        "PAY_AMT5": pay_amt5,
        "PAY_AMT6": pay_amt6
    }])

    prediction = model.predict(input_data)[0]

    probability = model.predict_proba(input_data)[0][1]

    st.subheader("Prediction result")

    if prediction == 1:
        st.error(" Customer is likely to DEFAULT on the next payment")
    else:
        st.success(" Customer is NOT likely to default")

    st.metric("Probability of Default",f"{probability:.2%}")


