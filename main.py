import streamlit as st
import pandas as pd

st.title("📊 Phân tích dữ liệu mô tả – Streamlit + Pandas")

# =======================
# 1. TẠO DATAFRAME TỪ DỮ LIỆU
# =======================
data = {
    "Chất lượng giấc ngủ": [
        3,4,2,3,2,3,3,4,2,1,2,3,2,4,4,2,3,1,2,2,3,3,2,3,5,3,5,5,2,3,
        5,5,5,2,4,5,4,3,3,3,4,4,4,2,5,4,2,4,4,3,1,5,1,3
    ],
    "Khối lượng học tập": [
        4,3,1,2,5,2,4,4,4,2,5,1,4,4,2,5,3,1,1,2,2,4,3,4,2,2,1,1,1,1,
        5,2,5,1,4,3,2,1,5,4,2,5,3,4,4,2,2,4,2,4,2,2
    ],
    "Hoạt động ngoại khóa": [
        2,3,4,3,5,1,3,1,5,5,2,4,4,1,5,3,3,1,2,3,1,3,2,2,1,2,5,1,1,3,
        5,3,2,2,5,2,4,1,3,4,2,1,5,1,4,1,2,4,3,3
    ],
    "Mức độ stress": [
        3,2,4,3,3,1,5,1,1,2,4,1,3,1,2,4,4,2,3,4,2,3,2,3,1,1,5,1,2,1,
        5,4,5,2,2,5,5,3,1,3,2,5,4,3,5,4,4,2,1,3,1,2
    ]
}


df = pd.DataFrame(data)

# =======================
# 2. HIỂN THỊ DỮ LIỆU
# =======================

st.subheader("📌 Dữ liệu ban đầu")
st.dataframe(df)

# =======================
# 3. THỐNG KÊ MÔ TẢ
# =======================

st.subheader("📌 Thống kê mô tả")
st.write(df.describe())

# =======================
# 4. BIỂU ĐỒ PHÂN PHỐI (BAR CHART)
# =======================

st.subheader("📌 Biểu đồ phân phối dữ liệu")
selected_col = st.selectbox("Chọn cột để xem biểu đồ:", df.columns)
st.bar_chart(df[selected_col])

# =======================
# 5. BIỂU ĐỒ TƯƠNG QUAN (SCATTER)
# =======================

st.subheader("📌 Biểu đồ tương quan giữa hai biến")
x = st.selectbox("Chọn biến X:", df.columns, key="x")
y = st.selectbox("Chọn biến Y:", df.columns, key="y")

st.scatter_chart(df[[x, y]])
