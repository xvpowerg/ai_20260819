import streamlit as st
import pandas as pd
import joblib
st.title("銷售預測應用")
linear_model,linear_scaler = joblib.load(r"C:\python_code\ai_20260819\ch16\linear_model.pkl")
tv_spend = st.number_input("輸入TV廣告支出",min_value=0.0)
radio_spend = st.number_input("輸入Radio廣告支出",min_value=0.0)
newspaper_spend =st.number_input("輸入newspaper廣告支出",min_value=0.0) 
if st.button("預測銷售"):
    input_data = {
        "TV":tv_spend,
        "radio":radio_spend,
        "newspaper":newspaper_spend}
    input_df = pd.DataFrame([input_data])
    input_scaler = linear_scaler.transform(input_df)
    pred = linear_model.predict(input_scaler)
    st.write(f"預測銷售額:{pred}")