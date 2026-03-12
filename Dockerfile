FROM python:3.9-slim

WORKDIR /app

# ติดตั้ง dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ก๊อปปี้โค้ดทั้งหมด
COPY . .

# ตั้งค่า Port สำหรับ Streamlit (Render มักใช้ 10000)
EXPOSE 10000

# คำสั่งรัน Streamlit ให้รองรับการเข้าถึงจากภายนอก
CMD ["streamlit", "run", "app.py", "--server.port", "10000", "--server.address", "0.0.0.0"]
