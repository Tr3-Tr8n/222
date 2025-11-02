import streamlit as st
import pandas as pd

# Tiêu đề
st.title("🎬 Top 5 bộ phim có doanh thu cao nhất mọi thời đại")

# Tạo bộ dữ liệu
data = {
    "Tên phim": [
        "Avatar",
        "Avengers: Endgame",
        "Titanic",
        "Star Wars: The Force Awakens",
        "Avengers: Infinity War"
    ],
    "Doanh thu (tỷ USD)": [2.92, 2.80, 2.26, 2.07, 2.05]
}

df = pd.DataFrame(data)

# Hiển thị bảng dữ liệu
st.subheader("📊 Bảng dữ liệu")
st.dataframe(df)

# Biểu đồ cột
st.subheader("📈 Biểu đồ doanh thu phim")
st.bar_chart(df.set_index("Tên phim"))
