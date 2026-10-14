import streamlit as st
import pandas as pd
st.title("CSV Reading")
uploade_file = st.file_uploader("選一個CSV文件")
#st.write(uploade_file)
if uploade_file is not None:
    df = pd.read_csv(uploade_file)
    st.subheader("原始數據")
    df = df.drop(columns=["時間"])
    st.dataframe(df)
    st.subheader("視覺化")
    st.line_chart(df)
