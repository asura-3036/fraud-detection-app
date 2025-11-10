import streamlit as st
import pandas as pd
import joblib

st.title("💳 Fraud Detection Prediction App")
model = joblib.load('fraud_detection_pipeline.pkl')

st.markdown("Enter transaction details and click **Predict** to detect possible fraud.")

type_ = st.selectbox('Transaction Type', ['PAYMENT','TRANSFER','CASH_OUT','DEBIT','CASH_IN'])
amount = st.number_input('Amount', min_value=0.0, value=1000.0)
oldbalanceOrg = st.number_input('Old Balance (Sender)', min_value=0.0, value=10000.0)
newbalanceOrig = st.number_input('New Balance (Sender)', min_value=0.0, value=9000.0)
oldbalanceDest = st.number_input('Old Balance (Receiver)', min_value=0.0, value=0.0)
newbalanceDest = st.number_input('New Balance (Receiver)', min_value=0.0, value=0.0)

if st.button('Predict'):
    input_data = pd.DataFrame([{ 
        'type': type_, 'amount': amount,
        'oldbalanceOrg': oldbalanceOrg, 'newbalanceOrig': newbalanceOrig,
        'oldbalanceDest': oldbalanceDest, 'newbalanceDest': newbalanceDest
    }])
    prediction = model.predict(input_data)[0]
    if prediction == 1:
        st.error('🚨 This transaction **can be fraud**!')
    else:
        st.success('✅ This transaction looks legitimate.')

st.divider()
st.caption('Fraud Detection Model | Built with Streamlit & Scikit-learn')
