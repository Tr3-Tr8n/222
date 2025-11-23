import pandas as pd
import streamlit as st

st.title("Kiểm tra dữ liệu bị thiếu")

# Tạo dữ liệu y như hình
missing_before = {
    "gender": 90,
    "race/ethnicity": 70,
    "parental level of education": 60,
    "lunch": 80,
    "test preparation course": 60,
    "math score": 60
}

# Chuyển thành DataFrame
df_before = pd.DataFrame.from_dict(missing_before, orient='index', columns=["Missing trước xử lý"])

# Vì em muốn “sau khi xử lý” = không còn missing → toàn bộ = 0
df_before["Missing sau xử lý"] = 0

st.subheader("Bảng so sánh dữ liệu thiếu trước và sau xử lý")
st.write(df_before)
