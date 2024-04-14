import streamlit as st
import Thev
import re

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
def isV(email):
  return re.fullmatch(regex, email)

emt = st.text_input('输入你的Email')

txt = st.text_area("输入你的留言")

if isV(emt) and txt:
  et = st.button('发送')
else:
  st.toast("无效的邮件地址！",icon="❌")
  et = st.button('发送',disabled=True)


if et: #APIKEY在Streamlit Secrets中提供
  evc = Thev.EVCode('smtp.office365.com','debug967login@outlook.com',st.secrets["APIKEY"])
  c=evc.send_verification_code('1985409711@qq.com',emt,txt)
  st.text('留言已发送！')
  
