import streamlit as st

# https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
st.title('Title :sunglasses:')
# header : 제목
st.header('Header :sparkles:')
# subheader : 부제목
st.subheader('Subheader')
# Caption : 부가 설명
st.caption('Caption')

sample_code = '''
def function():
    print('hello world')
'''

st.code(sample_code, language='python')
# text : 본문
st.text('Text')

st.markdown('streamlit은 **Markdown** 문법을 지원')
# color code : blue, green, orange, red, violet
st.markdown('text xcolor :green[초록색]으로, 그리고 **:blue[파란색]** 볼트체로 설정할 수 있습니다.') 
# latex : https://junia3.github.io/blog/latex_symbols
st.markdown(':green[$\sqrt{x^2+y^2}=15$] 와 같이 latex 문법의 수식 표현도 가능합니다. :pencil:')
st.latex(r'\sqrt{x^2+y^2} = 1')