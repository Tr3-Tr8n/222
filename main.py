
    import streamlit as st

    # Cấu hình trang
    st.set_page_config(page_title="Sơn Tùng M-TP", page_icon="🎤", layout="centered")

    # Sidebar - Thông tin ca sĩ
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

    # Tiêu đề chính
    st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>🎶 Ca sĩ yêu thích: Sơn Tùng M-TP 🎶</h1>", unsafe_allow_html=True)

    # Mục Bài hát yêu thích (Expander)
    with st.expander("🎵 Bài hát yêu thích", expanded=True):
        songs = {
            "Chạy Ngay Đi": "https://raw.githubusercontent.com/user123/mp3-host/main/chay-ngay-di.mp3",
            "Hãy Trao Cho Anh": "https://raw.githubusercontent.com/user123/mp3-host/main/hay-trao-cho-anh.mp3",
            "Nơi Này Có Anh": "https://raw.githubusercontent.com/user123/mp3-host/main/noi-nay-co-anh.mp3"
        }
        for name, url in songs.items():
            st.subheader(f"🎧 {name}")
            st.audio(url)

    # Mục MV yêu thích (Expander)
    with st.expander("🎬 MV yêu thích", expanded=False):
        mvs = {
            "Chạy Ngay Đi": "https://www.youtube.com/watch?v=32sYGCOYJUM",
            "Hãy Trao Cho Anh": "https://www.youtube.com/watch?v=knW7-x7Y7RE",
            "Nơi Này Có Anh": "https://www.youtube.com/watch?v=I3izrLn-sz8"
        }
        for name, url in mvs.items():
            st.subheader(f"📺 {name}")
            st.video(url)
