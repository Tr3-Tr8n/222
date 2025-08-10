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
    use_column_width=True
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
st.header("📅 Timeline Sự Nghiệp")
timeline = {
    "2012": "Ra mắt ca khúc 'Cơn mưa ngang qua' và trở nên nổi tiếng.",
    "2015": "Ra mắt 'Âm thầm bên em', đạt hàng chục triệu view.",
    "2017": "'Lạc trôi' và 'Nơi này có anh' phá kỷ lục YouTube Việt Nam.",
    "2019": "'Hãy trao cho anh' hợp tác với Snoop Dogg, gây tiếng vang quốc tế.",
    "2021": "Ra mắt 'Muộn rồi mà sao còn' đạt hàng triệu view trong vài giờ."
}
for year, event in timeline.items():
    st.write(f"**{year}** - {event}")

# ========================
# Mục Bài hát yêu thích
# ========================
st.header("🎵 Bài hát yêu thích")

songs = {
    "Chạy Ngay Đi": "https://samplelib.com/lib/preview/mp3/sample-3s.mp3",  # Thay bằng file mp3 thật
    "Hãy Trao Cho Anh": "https://samplelib.com/lib/preview/mp3/sample-6s.mp3",
    "Nơi Này Có Anh": "https://samplelib.com/lib/preview/mp3/sample-9s.mp3"
}

for song_name, song_url in songs.items():
    st.subheader(f"🎧 {song_name}")
    st.audio(song_url)

# ========================
# Mục MV yêu thích
# ========================
st.header("🎬 MV yêu thích")

mvs = {
    "Chạy Ngay Đi": "https://www.youtube.com/watch?v=32sYGCOYJUM",
    "Hãy Trao Cho Anh": "https://www.youtube.com/watch?v=knW7-x7Y7RE",
    "Nơi Này Có Anh": "https://www.youtube.com/watch?v=I3izrLn-sz8"
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

# ========================
# Fan quotes
# ========================
st.header("💬 Fan Quotes")
quotes = [
    "Sơn Tùng luôn là niềm tự hào của Sky 💙",
    "Âm nhạc của anh là thanh xuân của tôi!",
    "Mỗi bài hát đều mang một câu chuyện cảm xúc."
]
for q in quotes:
    st.success(q)

# ========================
# Form góp ý
# ========================
st.header("📝 Góp ý của bạn")
with st.form("feedback_form"):
    name = st.text_input("Tên của bạn")
    feedback = st.text_area("Cảm nhận của bạn về Sơn Tùng M-TP")
    submitted = st.form_submit_button("Gửi")
    if submitted:
        st.write(f"💌 Cảm ơn **{name}** đã chia sẻ cảm nhận!")
