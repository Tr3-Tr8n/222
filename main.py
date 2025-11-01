import pandas as pd
import streamlit as st

# Tạo dữ liệu
data = {
    "Tên phim": ["The Godfather", "12 Angry Men", "Pulp Fiction", "Joker", "Avatar"],
    "Rating": [9.2, 9.0, 8.9, 8.5, 7.9]
}

df = pd.DataFrame(data)

# Sắp xếp theo Rating giảm dần và lấy Top 5
top5 = df.sort_values(by="Rating", ascending=False).head(5)

# Tiêu đề ứng dụng
st.title("TOP 5 PHIM CÓ RATING CAO NHẤT")

# Set Tên phim làm trục Y và Rating làm trục X
st.bar_chart(top5.set_index("Tên phim"))
