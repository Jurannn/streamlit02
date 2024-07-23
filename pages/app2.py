import streamlit as st

ani_list = ['짱구는못말려', '몬스터','릭앤모티']
img_list = ['https://i.imgur.com/t2ewhfH.png', 
            'https://i.imgur.com/ECROFMC.png', 
            'https://i.imgur.com/MDKQoDc.jpg']


#검색창
input = st.text_input(label = "애니메이션 이름을 입력해 주세요: ", key = 'msg')


#입력 창에서 데이터를 입력 받아서
st.write(input)
#ani_list와 문자열이 일치하는 이미지를 화면에 출력

for i in range(len(ani_list)):
    if st.session_state.msg == ani_list[i]:
        st.image(img_list[i])

        st.download_button(label = '이미지를 다운받으세요.', data = img_list[i]) 



'''
import streamlit as st

ani_list = ['짱구는못말려', '몬스터','릭앤모티']
img_list = ['https://i.imgur.com/t2ewhfH.png', 
            'https://i.imgur.com/ECROFMC.png', 
            'https://i.imgur.com/MDKQoDc.jpg']


#검색창
input = st.text_input(label = "애니메이션 이름을 입력해 주세요: ", key = 'msg')


#입력 창에서 데이터를 입력 받아서
st.write(input)
#ani_list와 문자열이 일치하는 이미지를 화면에 출력

for i in range(len(ani_list)):
    for j in range(len(st.session_state.msg)):
        if st.session_state.msg[j] in ani_list[i]:
            st.image(img_list[i])

            st.download_button(label = '이미지를 다운받으세요.', data = img_list[i])

'''