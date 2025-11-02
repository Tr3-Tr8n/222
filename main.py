import streamlit as st
import pandas as pd

# Dữ liệu phim
data = {
    "Tên phim": [
        "The Godfather",
        "12 Angry Men",
        "Pulp Fiction",
        "Joker",
        "Avatar"
    ],
    "Rating": [9.2, 9.0, 8.9, 8.5, 7.9]
}

# Tạo DataFrame
df = pd.DataFrame(data)

# Sắp xếp giảm dần theo rating và lấy top 5
top5 = df.sort_values(by="Rating", ascending=False).head(5)

# Tiêu đề
st.title("Top 5 phim có Rating cao nhất")

# Hiển thị bảng dữ liệu
st.dataframe(top5)

# Vẽ biểu đồ cột
st.bar_chart(
    top5.set_index("Tên phim")["Rating"]
)
