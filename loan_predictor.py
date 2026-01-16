import streamlit as st
import joblib
import pandas as pd

st.set_page_config(layout="wide")
model, scaler = joblib.load('lr_model.pkl'), joblib.load('scaler.pkl')

st.title("💳 Loan Risk Checker")

col1, col2 = st.columns(2)
with col1: 
    loan_amt = st.number_input("Loan Amount", 10000, 500000, 50000)  # Text box
    monthly_bill = st.number_input("Monthly Bill", 0, 200000, 25000)  # Text box
with col2: 
    age = st.number_input("Age", 20, 80, 35)  # Text box
    delay = st.number_input("Payment Delay (months)", 0, 8, 1)  # Text box
payment_amt = st.number_input("Monthly Payment", 0, 50000, 2000)  # Text box

if st.button("Predict"):
    data = pd.DataFrame({
        'ID':[0],
        'LIMIT_BAL':[loan_amt],'SEX':[2],'EDUCATION':[2],'MARRIAGE':[2],
        'AGE':[age],'PAY_0':[delay],'PAY_2':[delay],'PAY_3':[delay],
        'PAY_4':[0],'PAY_5':[0],'PAY_6':[0],'BILL_AMT1':[monthly_bill],
        'BILL_AMT2':[monthly_bill],'BILL_AMT3':[monthly_bill],'BILL_AMT4':[monthly_bill],
        'BILL_AMT5':[monthly_bill],'BILL_AMT6':[monthly_bill],
        'PAY_AMT1':[payment_amt],
        'PAY_AMT2':[payment_amt],'PAY_AMT3':[payment_amt],
        'PAY_AMT4':[payment_amt],'PAY_AMT5':[payment_amt],'PAY_AMT6':[payment_amt]
    })
    
    risk = model.predict_proba(scaler.transform(data))[0,1]*100
    st.metric("Default Risk", f"{risk:.0f}%")
    st.success("✅ Safe" if risk<30 else "❌ Risky")
