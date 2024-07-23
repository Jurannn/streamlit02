import streamlit as st

# Using object notation

#문법1
#sidebox 생성
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

# Using "with" notation - 문법2
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )

    st.write(add_selectbox)
    st.write(add_radio)


#컬럼 만들기 - 전체 화면을 n개의 열로 만들겠당
col1, col2 = st.columns(2) #n을 지정 <- unpacking
col1.write('Column 1')
col1.header('Header')

col2.write('Column 2')
col2.write('hi~~~~~~~~~')

# Three columns with different widths
col1, col2, col3 = st.columns([3,1,1])
#3개로 나누는 방법 -> 3:1:1의 비율로 사용하겠습니당!~~
# col1 is wider

col3.write('컬럼3이에용.')
# Using 'with' notation:
with col1:
    st.image('https://i.imgur.com/MDKQoDc.jpg')
with col2:
    st.image('https://i.imgur.com/t2ewhfH.png')
with col3:
    st.image('https://i.imgur.com/ECROFMC.png')