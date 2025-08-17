import streamlit as st

st.set_page_config(page_title="World Foods", layout="wide")

st.title("🍽️ Ẩm thực thế giới")

# 5 cột cho 5 món ăn
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    if st.button("🍜 Phở"):
        st.header("Phở")
        st.image("https://upload.wikimedia.org/wikipedia/commons/5/53/Pho-Beef-Noodles-2008.jpg", width=400)
        st.write("🌏 Xuất xứ: Việt Nam 🇻🇳")
        st.subheader("Nguyên liệu:")
        st.markdown("- Bánh phở\n- Thịt bò/gà\n- Hành, gừng, quế, hồi\n- Nước hầm xương")
        st.subheader("Cách làm:")
        st.markdown("1. Hầm xương lấy nước dùng.\n2. Thêm gia vị (hồi, quế, hành, gừng).\n3. Chần bánh phở, thịt bò/gà.\n4. Chan nước dùng nóng, thêm rau thơm.")
        st.video("https://www.youtube.com/watch?v=c9GfHgMk1ac&ab_channel=C%C3%B4BaB%C3%ACnhD%C6%B0%C6%A1ng")

with col2:
    if st.button("🍣 Sushi"):
        st.header("Sushi")
        st.image("https://upload.wikimedia.org/wikipedia/commons/6/60/Sushi_platter.jpg", width=400)
        st.write("🌏 Xuất xứ: Nhật Bản 🇯🇵")
        st.subheader("Nguyên liệu:")
        st.markdown("- Cơm dẻo trộn giấm\n- Cá sống (cá hồi, cá ngừ...)\n- Rong biển\n- Rau củ")
        st.subheader("Cách làm:")
        st.markdown("1. Nấu cơm trộn giấm đường.\n2. Đặt cơm lên rong biển.\n3. Thêm cá sống, rau củ.\n4. Cuộn chặt và cắt miếng.")
        st.video("https://www.youtube.com/watch?v=FXFKwKZ9kB0&ab_channel=SushiMonChicago")

with col3:
    if st.button("🍕 Pizza"):
        st.header("Pizza")
        st.image("https://upload.wikimedia.org/wikipedia/commons/d/d3/Supreme_pizza.jpg", width=400)
        st.write("🌏 Xuất xứ: Ý 🇮🇹")
        st.subheader("Nguyên liệu:")
        st.markdown("- Bột mì\n- Nước, men nở\n- Phô mai Mozzarella\n- Xốt cà chua\n- Thịt, rau củ")
        st.subheader("Cách làm:")
        st.markdown("1. Nhào bột, ủ nở.\n2. Cán mỏng, phết xốt cà.\n3. Thêm phô mai, topping.\n4. Nướng 200°C khoảng 15 phút.")
        st.video("https://www.youtube.com/results?search_query=m%C3%B3n+pizza")

with col4:
    if st.button("🥗 Gỏi cuốn"):
        st.header("Gỏi cuốn")
        st.image("https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcSQRzdUXNnaiIBzv68FMhy3zN4nyeboM85SmzKmmsVKe9rBk4l15WPzWkyufb1x5Oryw3niyL7sWCdvgs0tXjz5Qb5hGQzSxx3bkMopNYzV", width=400)
        st.write("🌏 Xuất xứ: Việt Nam 🇻🇳")
        st.subheader("Nguyên liệu:")
        st.markdown("- Bánh tráng\n- Tôm, thịt\n- Bún\n- Rau sống, giá")
        st.subheader("Cách làm:")
        st.markdown("1. Luộc tôm, thịt, thái lát.\n2. Nhúng bánh tráng cho mềm.\n3. Xếp bún, rau, tôm, thịt.\n4. Cuốn chặt, ăn với nước chấm.")
        st.video("https://www.youtube.com/watch?v=w34Qnc-9KBU&ab_channel=C%C3%B4BaB%C3%ACnhD%C6%B0%C6%A1ng")

with col5:
    if st.button("🍰 Bánh kem"):
        st.header("Bánh kem")
        st.image("https://thuhuongcake.vn/wp-content/uploads/2024/12/Banh-kem-ky-niem-ngay-cuoi-1-1.webp", width=400)
        st.write("🌏 Xuất xứ: Pháp 🇫🇷")
        st.subheader("Nguyên liệu:")
        st.markdown("- Bột mì\n- Trứng, đường, sữa\n- Kem tươi\n- Bơ")
        st.subheader("Cách làm:")
        st.markdown("1. Đánh bông trứng với đường.\n2. Trộn bột, sữa, nướng thành cốt bánh.\n3. Đánh bông kem tươi.\n4. Phết kem và trang trí.")
        st.video("https://www.youtube.com/watch?v=KI-MNom4awg&ab_channel=Sukie%27sKitchen")
