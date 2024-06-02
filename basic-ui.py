import streamlit as st
import pandas as pd
from datetime import datetime as dt
import datetime

# 버튼 클릭
button = st.button('button')

if button:
    st.write(':blue[버튼]이 눌렸습니다 :sparkles:')

# 파일 다운로드 버튼
dataframe = pd.DataFrame({
    'first column' : [1, 2, 3, 4],
    'second column' : [10, 20, 30, 40],
})

# Download Button
st.download_button(
    label='Download to CSV',
    data=dataframe.to_csv(),
    file_name='sample.csv',
    mime='text/csv'
)

# check box
agree = st.checkbox('agree')

if agree:
    st.write('Thanks for your agree :100:')

# radio
# mbti = st.radio(
#     'What is your MBTI',
#     ('ISFJ', 'ESTJ', 'NONE')
# )

# if mbti == 'ISFJ':
#     st.write('You\'re a :blue[guardian]')
# elif mbti == 'ESTJ':
#     st.write('You\'re a :green[consul]')
# else :
#     st.write('You\'re :red[not in the database]:grey_exclamation:')

# select box
# mbti = st.selectbox(
#     'What is your MBTI',
#     ('ISFJ', 'ESTJ', 'NONE'),
#     index=2
# )

# if mbti == 'ISFJ':
#     st.write('You\'re a :blue[guardian]')
# elif mbti == 'ESTJ':
#     st.write('You\'re a :green[consul]')
# else :
#     st.write('You\'re :red[not in the database]:grey_exclamation:')

# Multiple choice 
options = st.multiselect(
    'What is your favorite fruits',
    ['Mango', 'Orange', 'Apple', 'Banana'],
    ['Mango', 'Orange']
)

st.write(f'Your choice are :red[{options}]')

# Slider
values = st.slider(
    'Ranging :sparkles:',
    0.0, 100.0, (25.0, 75.0)
)
st.write('Range:', values)

start_time = st.slider(
    'appointment time',
    min_value=dt(2024, 1, 1, 0, 0),
    max_value=dt(2024, 12, 31, 23, 59),
    value=dt(2024, 6, 2, 0, 0),
    step=datetime.timedelta(hours=1),
    format='MM/DD/Y - HH:mm'
)

st.write('Choiced appointment time : ', start_time)

# input the text
title = st.text_input(
    label='Destination you want to go',
    placeholder='Input the Destination'
)
st.write(f'Choiced your Destination : :violet[{title}]')

# input the number
number = st.number_input(
    label='input your age',
    min_value=10,
    max_value=100,
    value=24,
    step=1
)
st.write('Entered your age : ', number)