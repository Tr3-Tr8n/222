import streamlit as st

# Thông tin cửa hàng
st.sidebar.title("🛒 Cửa hàng Mô Hình Anime")
st.sidebar.write("Chuyên bán các mô hình nhân vật hoạt hình chất lượng cao.")
st.sidebar.write("📍 Địa chỉ: 123 Đường ABC, TP.HCM")
st.sidebar.write("📞 Hotline: 0909-123-456")
st.sidebar.write("✉️ Email: lienhe@shopmohinh.vn")

st.title("✨ Cửa Hàng Mô Hình Anime ✨")
st.write("Chọn chủ đề mô hình bạn yêu thích:")

# Dữ liệu mẫu các mô hình
models = {
    "Dragon Ball": [
        {"id": "DB01", "name": "Goku Super Saiyan", "img": "https://i.imgur.com/fXrxvY7.png"},
        {"id": "DB02", "name": "Vegeta Super Saiyan", "img": "https://i.imgur.com/k0yZVqN.png"},
        {"id": "DB03", "name": "Piccolo", "img": "https://i.imgur.com/xXv1WUn.png"}
    ],
    "Naruto": [
        {"id": "NA01", "name": "Naruto Sage Mode", "img": "https://i.imgur.com/dck0XGd.png"},
        {"id": "NA02", "name": "Sasuke Sharingan", "img": "https://i.imgur.com/N7xqk4C.png"},
        {"id": "NA03", "name": "Kakashi Hatake", "img": "https://i.imgur.com/2u8IxmH.png"}
    ],
    "One Piece": [
        {"id": "OP01", "name": "Luffy Gear 4", "img": "https://i.imgur.com/6R6C7S9.png"},
        {"id": "OP02", "name": "Zoro", "img": "https://i.imgur.com/cNoY9kd.png"},
        {"id": "OP03", "name": "Sanji", "img": "https://i.imgur.com/fn8X2Yj.png"}
    ]
}

# Nút chọn chủ đề
choice = st.radio("📌 Chọn bộ sưu tập:", ["Dragon Ball", "Naruto", "One Piece"])

st.subheader(f"🖼 Danh sách mô hình: {choice}")
cols = st.columns(3)

for i, model in enumerate(models[choice]):
    with cols[i]:
        st.image(model["img"], caption=f"{model['id']} - {model['name']}", use_column_width=True)

# Đặt hàng
st.subheader("📝 Đặt Hàng")
with st.form("order_form"):
    theme = st.selectbox("Chọn bộ sưu tập", list(models.keys()))
    model_id = st.selectbox("Chọn mã mô hình", [m["id"] for m in models[theme]])
    quantity = st.number_input("Số lượng", min_value=1, value=1)
    name = st.text_input("Họ tên")
    phone = st.text_input("Số điện thoại")
    address = st.text_area("Địa chỉ giao hàng")
    confirm = st.form_submit_button("Xác nhận đặt hàng")

    if confirm:
        model_name = [m["name"] for m in models[theme] if m["id"] == model_id][0]
        st.success("✅ Đặt hàng thành công!")
        st.write("### 🧾 Hóa đơn")
        st.write(f"Khách hàng: **{name}**")
        st.write(f"SĐT: {phone}")
        st.write(f"Địa chỉ: {address}")
        st.write(f"Sản phẩm: {model_name} ({model_id})")
        st.write(f"Số lượng: {quantity}")
        st.write(f"Thành tiền: {quantity * 300000} VNĐ")  # giả sử giá 300k/sp
        st.download_button("📥 In hóa đơn", 
                           data=f"Hóa đơn mua hàng\nKhách hàng: {name}\nSĐT: {phone}\nĐịa chỉ: {address}\nSản phẩm: {model_name} ({model_id})\nSố lượng: {quantity}\nThành tiền: {quantity * 300000} VNĐ",
                           file_name="hoa_don.txt")
