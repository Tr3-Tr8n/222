import pandas as pd
import streamlit as st

# Tải dữ liệu
df = pd.read_csv("StudentsPerformance.csv")

st.title("Kiểm tra dữ liệu bị thiếu")

# 1. Số lượng missing ban đầu
missing_before = df.isnull().sum()

# 2. Xử lý dữ liệu bị thiếu
df_clean = df.fillna("Unknown")

# 3. Số lượng missing sau khi xử lý
missing_after = df_clean.isnull().sum()

# 4. Gộp 2 cột vào 1 bảng
missing_table = pd.DataFrame({
    "Missing trước xử lý": missing_before,
    "Missing sau xử lý": missing_after
})

st.subheader("Bảng so sánh dữ liệu thiếu trước và sau xử lý")
st.write(missing_table)

# 5. Hiển thị bảng dữ liệu sạch
st.subheader("Bảng dữ liệu sau khi xử lý thiếu")
st.write(df_clean)
