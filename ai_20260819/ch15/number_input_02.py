import streamlit as st
st.title("數字輸入範例")
n1 = st.number_input("請輸入第一個數字:", value=0)
n2 = st.number_input("請輸入第二個數字:", value=0)
sum_result = n1 + n2
st.write(f"兩個數字的總和為: {sum_result}")
