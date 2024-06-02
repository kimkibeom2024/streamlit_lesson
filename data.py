import streamlit as st
import pandas as pd
import numpy as np

st.title('DataFrame Tutorial')

# EXCEL 표 만든다고 생각!
dataframe = pd.DataFrame({
    'first column' : [1, 2, 3, 4],
    'second column' : [10, 20, 30, 40],  
})
# Dataframe
st.dataframe(dataframe, use_container_width=True)

# 테이블(Statiac)
st.table(dataframe)

# 메트릭
st.metric(label='온도', value='10°C', delta='1.2°C')
st.metric(label='삼성전자', value='61,000 원', delta='-1,200 원')

col1, col2, col3 = st.columns(3)
col1.metric(label='달러USD', value='1,228 원', delta='-12.00 원')
col2.metric(label='일본JPY(100엔)', value='958.63 원', delta='-7.44 원')
col3.metric(label='유럽연합EUR', value='1,335.82 원', delta='11.44 원')