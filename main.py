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

st.title("Thông tin thời tiết các thành phố")
st.dataframe(data)
# 2



data = {
    "Thời gian": ["12-05-2023", "26-05-2023", "30-05-2023", "10-06-2023", "25-06-2023"],
    "Nội dung": [
        "Phù! Cuối cùng cũng thi xong rồi.",
        "Kết quả khá tốt nha.",
        "Hẹn gặp lại các bạn sau hè.",
        "Nước xanh quá.",
        "Huhu, cao quá, muốn về cơ."
    ],
    "Địa điểm": ["Hà Nội", "Hà Nội", "Hà Nội", "Nha Trang", "Sơn La"],
    "Cảm xúc": ["😰", "🥰", "🤗", "🥳", "😱"]
}


df = pd.DataFrame(data)


st.title("Bảng dữ liệu phần khám phá 2")
st.dataframe(df)
