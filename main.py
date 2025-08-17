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
        st.video("https://www.youtube.com/watch?v=0SPwwpruGIA")

with col2:
    if st.button("🍣 Sushi"):
        st.header("Sushi")
        st.image("https://upload.wikimedia.org/wikipedia/commons/6/60/Sushi_platter.jpg", width=400)
        st.write("🌏 Xuất xứ: Nhật Bản 🇯🇵")
        st.video("https://www.youtube.com/watch?v=BtM0m9x0Eo8")

with col3:
    if st.button("🍕 Pizza"):
        st.header("Pizza")
        st.image("https://upload.wikimedia.org/wikipedia/commons/d/d3/Supreme_pizza.jpg", width=400)
        st.write("🌏 Xuất xứ: Ý 🇮🇹")
        st.video("https://www.youtube.com/watch?v=uUQXJ1kF1h0")

with col4:
    if st.button("🥗 Gỏi cuốn"):
        st.header("Gỏi cuốn")
        st.image("https://upload.wikimedia.org/wikipedia/commons/7/77/Vietnamese_spring_rolls.jpg", width=400)
        st.write("🌏 Xuất xứ: Việt Nam 🇻🇳")
        st.video("https://www.youtube.com/watch?v=9-aPYtkldHQ")

with col5:
    if st.button("🍰 Bánh kem"):
        st.header("Bánh kem")
        st.image("https://upload.wikimedia.org/wikipedia/commons/0/04/Birthday_cake_with_candles.jpg", width=400)
        st.write("🌏 Xuất xứ: Pháp 🇫🇷")
        st.video("https://www.youtube.com/watch?v=J---aiyznGQ")
