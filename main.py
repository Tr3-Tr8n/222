import pandas as pd
import streamlit as st

# Tạo danh sách các thành phố
cities = ["Hà Nội", "Hồ Chí Minh", "Hải Phòng", "Đà Nẵng", "Cần Thơ"]

# Dữ liệu mẫu
weather_data = [
    ["Nắng nhẹ", 32, 60, "10 km/h", "Tốt"],
    ["Trời nhiều mây", 30, 70, "8 km/h", "Trung bình"],
    ["Mưa rào", 28, 85, "12 km/h", "Tốt"],
    ["Nắng nóng", 34, 55, "9 km/h", "Trung bình"],
    ["Mưa nhẹ", 29, 80, "11 km/h", "Tốt"]
]

# Tạo DataFrame
df = pd.DataFrame(
    weather_data,
    columns=["Tình hình thời tiết", "Nhiệt độ (°C)", "Độ ẩm (%)", "Tốc độ gió", "Chất lượng không khí"],
    index=cities
)

pd.set_option('display.max_columns', None)

# Lưu DataFrame ra CSV
df.to_csv("score.csv")

# Đọc lại dữ liệu từ CSV
data = pd.read_csv("score.csv", index_col=0)

# Hiển thị trên Streamlit
st.title("Thông tin thời tiết các thành phố")
st.dataframe(data)
