import streamlit as st
import pandas as pd


st.title(" Top 5 bộ phim có doanh thu cao nhất ")


data = {
    "Tên phim": [
        "Avatar",
        "Avengers: Endgame",
        "Titanic",
        "Star Wars: The Force Awakens",
        "Avengers: Infinity War"
    ],
    "Doanh thu ": [2.92, 2.80, 2.26, 2.07, 2.05]
}

df = pd.DataFrame(data)


st.subheader(" Bảng dữ liệu")
st.dataframe(df)

# Biểu đồ cột
st.subheader(" Biểu đồ doanh thu ")
st.bar_chart(df.set_index("Tên phim"))
