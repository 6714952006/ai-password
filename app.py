import streamlit as st
from zxcvbn import zxcvbn

st.set_page_config(page_title="AI Password Checker", page_icon="🔐")

st.title("🔐 AI Password Strength Checker")
st.write("ตรวจสอบความปลอดภัยของรหัสผ่านด้วย AI Logic (zxcvbn)")

password = st.text_input("กรอกรหัสผ่านที่ต้องการเช็ค:", type="password")

if password:
    res = zxcvbn(password)
    score = res['score'] # 0-4
    
    # แสดงผลตามคะแนน
    levels = ["🔴 แย่มาก", "🟠 อ่อน", "🟡 ปานกลาง", "🟢 ดี", "🔵 ปลอดภัยมาก"]
    st.subheader(f"ระดับ: {levels[score]}")
    st.progress((score + 1) * 20)
    
    if res['feedback']['warning']:
        st.warning(f"คำแนะนำ: {res['feedback']['warning']}")
    
    for s in res['feedback']['suggestions']:
        st.info(f"💡 {s}")
