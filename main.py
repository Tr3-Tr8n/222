import streamlit as st

# Dữ liệu thời khóa biểu
timetable = {
    "Thứ Hai": ["Toán", "Văn", "Anh văn", "Sinh học"],
    "Thứ Ba": ["Lý", "Toán", "Thể dục"],
    "Thứ Tư": ["Văn", "Sử", "Địa", "GDCD"],
    "Thứ Năm": ["Hóa học", "Toán", "Anh văn"],
    "Thứ Sáu": ["Tin học", "Lý", "Công nghệ"],
    "Thứ Bảy": ["Âm nhạc", "Mỹ thuật", "Thể dục"],
    "Chủ Nhật": ["Nghỉ học 🎉"]
}

# Tiêu đề trang
st.title("📅 Quản lý Thời khóa biểu")

# Selectbox chọn ngày
day = st.selectbox("Chọn ngày:", list(timetable.keys()))

# Hiển thị danh sách môn học
st.subheader("Môn học trong ngày " + day)
for mon in timetable[day]:
    st.write("- " + mon)
