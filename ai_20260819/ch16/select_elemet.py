import streamlit as st
from datetime import datetime
st.title("選擇元素範例")
option_selected = st.selectbox("你喜歡什麼顏色:", ["紅色", "綠色", "藍色"])
st.write(f"你選擇的顏色是: {option_selected}")
option_mult =  st.multiselect("請選你喜歡的水果:", 
               ["蘋果", "香蕉", "橘子", "葡萄"])
st.write(f"你選擇的水果有: {', '.join(option_mult)}")

option_radio = st.radio("請選擇你的性別:", ["男", "女"])
st.write(f"你選擇的性別是: {option_radio}")

atte_checkbox = st.checkbox("你是否同意條款?")
if atte_checkbox:
    st.write("你已同意條款。")
else:
    st.write("你尚未同意條款。")   

data_input = st.date_input("請選擇日期:", datetime.today().date())     
st.write(f"你選擇的日期是: {data_input}")