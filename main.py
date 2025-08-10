import streamlit as st

# ========================
# Setup giao diện
# ========================
st.set_page_config(page_title="Sơn Tùng M-TP Fanpage", page_icon="🎤", layout="wide")

# ========================
# Sidebar - Thông tin ca sĩ
# ========================
st.sidebar.image(
    "https://upload.wikimedia.org/wikipedia/commons/4/4c/S%C6%A1n_T%C3%B9ng_M-TP_2017.png",
    use_container_width
)
st.sidebar.title("🌟 Sơn Tùng M-TP")
st.sidebar.write("""
- **Tên thật**: Nguyễn Thanh Tùng  
- **Ngày sinh**: 5/7/1994  
- **Quê quán**: Thái Bình, Việt Nam  
- **Nghề nghiệp**: Ca sĩ, nhạc sĩ, diễn viên  
- **Fanclub**: SKY  
""")
st.sidebar.markdown("📷 [Instagram](https://www.instagram.com/sontungmtp/) | 🎥 [YouTube](https://www.youtube.com/c/MTPEntertainment)")

# ========================
# Banner
# ========================
st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>🎶 Sơn Tùng M-TP 🎶</h1>", unsafe_allow_html=True)
st.image("https://i.ytimg.com/vi/knW7-x7Y7RE/maxresdefault.jpg", use_column_width=True)

# ========================
# Timeline sự nghiệp
# ========================



# ========================
# Mục Bài hát yêu thích
# ========================
st.header("🎵 Bài hát yêu thích")





# ========================
# Mục MV yêu thích
# ========================
st.header("🎬 MV yêu thích")

mvs = {
    "Chạy Ngay Đi": "https://www.youtube.com/watch?v=32sYGCOYJUM",
    "Hãy Trao Cho Anh": "https://www.youtube.com/watch?v=knW7-x7Y7RE",
    "Nơi Này Có Anh": "https://www.youtube.com/watch?v=FN7ALfpGxiI&ab_channel=S%C6%A1nT%C3%B9ngM-TPOfficial"
}

cols = st.columns(len(mvs))
for i, (mv_name, mv_url) in enumerate(mvs.items()):
    with cols[i]:
        st.subheader(f"📺 {mv_name}")
        st.video(mv_url)

# ========================
# Album
# ========================
st.header("💿 Album & Single")
st.table({
    "Năm": [2017, 2019, 2021],
    "Tên Album/Single": ["Lạc Trôi", "Hãy Trao Cho Anh", "Muộn Rồi Mà Sao Còn"]
})


st.header("📝 Góp ý của bạn")
with st.form("feedback_form"):
    name = st.text_input("Tên của bạn")
    feedback = st.text_area("Cảm nhận của bạn về Sơn Tùng M-TP")
    submitted = st.form_submit_button("Gửi")
    if submitted:
        st.write(f"💌 Cảm ơn **{name}** đã chia sẻ cảm nhận!")
