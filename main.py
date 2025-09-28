import streamlit as st

# =========================
# Thông tin cửa hàng
# =========================
st.sidebar.title("🛒 Cửa Hàng Mô Hình Anime")
st.sidebar.info(
    """
    **Liên hệ:**  
    📍 Địa chỉ: 123 Anime Street, TP.HCM  
    📞 Điện thoại: 0909 999 999  
    📧 Email: shop@anime.vn  
    """
)

st.title("✨ Cửa hàng mô hình nhân vật Anime ✨")
st.write("Chọn chủ đề mô hình bạn yêu thích:")

# =========================
# Danh sách sản phẩm
# =========================
products = {
    "Dragon Ball": [
        {"id": "DB01", "name": "Goku Super Saiyan", "img": "https://i.imgur.com/GG7wLra.png", "price": 250000},
        {"id": "DB02", "name": "Vegeta Blue", "img": "https://i.imgur.com/QvC7JvR.png", "price": 280000},
        {"id": "DB03", "name": "Frieza Final Form", "img": "https://i.imgur.com/IVj9ubW.png", "price": 300000},
    ],
    "Naruto": [
        {"id": "NA01", "name": "Naruto Sage Mode", "img": "https://i.imgur.com/BJxQ2bP.png", "price": 260000},
        {"id": "NA02", "name": "Sasuke Sharingan", "img": "https://i.imgur.com/JRfXZcC.png", "price": 270000},
        {"id": "NA03", "name": "Kakashi Hatake", "img": "https://i.imgur.com/3l5l4zL.png", "price": 290000},
    ],
    "One Piece": [
        {"id": "OP01", "name": "Luffy Gear 4", "img": "https://i.imgur.com/rFfWc7X.png", "price": 320000},
        {"id": "OP02", "name": "Zoro 3 Swords", "img": "https://i.imgur.com/dvF0O2n.png", "price": 310000},
        {"id": "OP03", "name": "Sanji Black Leg", "img": "https://i.imgur.com/NzD5Zdn.png", "price": 280000},
    ]
}

# =========================
# Chọn chủ đề
# =========================
theme = st.radio("Chọn chủ đề:", list(products.keys()))

st.subheader(f"🧸 Danh sách mô hình {theme}")
cols = st.columns(3)

for idx, p in enumerat
