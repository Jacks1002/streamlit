
import streamlit as st

st.title("我的第一個 Streamlit 應用")
st.write("這是一個用純 Python 打造的互動式網頁！")

# 加入互動組件
name = st.text_input("請輸入你的名字：")
if name:
    st.success(f"你好，{name}！歡迎使用 Streamlit。")

# 加入按鈕與狀態控制
if st.button("點擊我有驚喜"):
    st.balloons()
