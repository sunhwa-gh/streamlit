import streamlit as st
import pandas as pd
import numpy as np

st.header('라인 차트')

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)