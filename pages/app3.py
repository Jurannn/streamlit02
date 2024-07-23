import streamlit as st
import pandas as pd  # st은 입력과 출력만 담당할 뿐 실제 로직은 나머지 파이썬 코드로 구현됩니다.

data = pd.DataFrame(
    [
       {"command": "st.selectbox", "rating": 4, "is_widget": True},
       {"command": "st.balloons", "rating": 5, "is_widget": False},
       {"command": "st.time_input", "rating": 3, "is_widget": True},
   ]
)

# 입력
st.title('1. 입력버튼들')

button_result = st.button('Hit me')
# 버튼을 누르면 데이터프레임이 등장하도록 로직을 만들어주세요
if button_result == True:
    st.write(button_result)
    st.data_editor(data)

check_result = st.checkbox('Check me out')
if check_result == True:
    st.data_editor(data)


radio_result = st.radio('Pick one:', ['nose','ear']) #둘 중 하나를 선택
st.write(radio_result)


st.selectbox('Select', [1,2,3]) #선택지에 있는 것중에서 하나만 선택 가능

st.multiselect('Multiselect', [1,2,3]) #선택지에 있는 것에서 여러개 선택

st.slider('Slide me', min_value=0, max_value=10) #정수로만 움직임
st.select_slider('Slide to select', options=[1,2,3]) #1,2,3중에서만 선택

ani_list = ['짱구는못말려', '몬스터','릭앤모티']
img_list = ['https://i.imgur.com/t2ewhfH.png', 
            'https://i.imgur.com/ECROFMC.png', 
            'https://i.imgur.com/MDKQoDc.jpg']

search = st.text_input('Enter some text')
for ani_ in ani_list:
    if search in ani_:
        img_idx = ani_list.index(ani_)

if search != '':
    st.image(img_list[img_idx])

st.number_input('Enter a number') #기본값이 float

area1 = st.text_area('Area for textual entry') #긴 text를 적는 경우 ex. 게시판에 내용 작성
st.write(area1) #입력 값 조작 가능

st.date_input('Date input') #날짜 입력
st.time_input('Time entry') #시간 입력
st.file_uploader('File uploader')
st.download_button( #파일 다운로드
    label="Download data as CSV",
    data=data.to_csv(),
    file_name='app_df.csv',
    mime='text/csv' #파일이 어떤 형식인지 미리 확인
)
picture = st.camera_input("Take a picture") #녹화, 카메라

if picture:
    st.image(picture)
    
st.color_picker('Pick a color') #색상 선택

#마크다운도 호환됨
# 출력
st.title('2. 출력메서드들')
st.text('Fixed width text')
st.markdown('_Markdown_') # see #* 마크다운 문법 사용 가눙~~
st.caption('Balloons. Hundreds of them...') #작고 연하게 출력
st.latex(r''' e^{i\pi} + 1 = 0 ''') #수식 입력
st.write('Most objects')
st.write(data) #데이터프레임을 st.write에 넣어도 제대로 보여줌
#st.write는 df, err, func, keras! 모든 형식을 알아서 예쁘게 출력~~
#파이썬 코드로 읽어서 출력함
st.write(['st', 'is <', 3]) # see * -> 파이썬의 리스트 코드 그대로!!~
st.title('My title')
st.header('My header')
st.subheader('My sub')
st.code('for i in range(8): foo()')

# * optional kwarg unsafe_allow_html = True

# 출력
