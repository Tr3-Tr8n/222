import pandas as pd
import streamlit as st

# Tạo dữ liệu thời tiết
data = {
    "Thành phố": ["Hà Nội", "Hồ Chí Minh", "Hải Phòng", "Đà Nẵng", "Cần Thơ"],
    "Tình hình thời tiết": ["Nắng", "Mây rải rác", "Mưa nhẹ", "Nhiều mây", "Nắng nhẹ"],
    "Nhiệt độ (°C)": [31, 33, 29, 30, 32],
    "Độ ẩm (%)": [60, 65, 70, 68, 66],
    "Tốc độ gió (km/h)": [10, 8, 12, 9, 7],
    "Chất lượng không khí (AQI)": [45, 55, 50, 42, 48]
}

# Tạo DataFrame
df = pd.DataFrame(data)

# Hiển thị trên Streamlit
st.title("🌤️ Bảng Dữ Liệu Thời Tiết Các Thành Phố Việt Nam")
st.dataframe(df)

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
