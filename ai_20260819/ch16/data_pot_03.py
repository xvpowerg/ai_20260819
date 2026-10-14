import streamlit as st
import pandas as pd
import numpy as np
st.title("資料表格範例")
data = pd.DataFrame({"x":np.arange(1,101),
                     "y":np.random.randn(100)})
st.line_chart(data,x="x",y="y")    