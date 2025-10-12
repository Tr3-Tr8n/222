import pandas as pd
import streamlit as st
cities = ["Hà Nội", "Hồ Chí Minh", "Hải Phòng", "Đà Nẵng", "Cần Thơ"]
weather_data = [
    ["Nắng nhẹ", 32, 60, "10 km/h", "Tốt"],
    ["Trời nhiều mây", 30, 70, "8 km/h", "Trung bình"],
    ["Mưa rào", 28, 85, "12 km/h", "Tốt"],
    ["Nắng nóng", 34, 55, "9 km/h", "Trung bình"],
    ["Mưa nhẹ", 29, 80, "11 km/h", "Tốt"]
]
df = pd.DataFrame(
    weather_data,
    columns=["Tình hình thời tiết", "Nhiệt độ (°C)", "Độ ẩm (%)", "Tốc độ gió", "Chất lượng không khí"],
    index=cities
)
pd.set_option('display.max_columns', None)
df.to_csv("score.csv")
data = pd.read_csv("score.csv", index_col=0)
st.title("Thông tin thời tiết các thành phố")
st.dataframe(data)
# 2