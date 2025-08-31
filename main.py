import streamlit as st

st.title("🍽️ Thực đơn trong ngày")


st.header("Bữa sáng")
breakfast_options = ["Xôi", "Bánh mì", "Phở", "Bún riêu", "Bánh cuốn", "Hủ tiếu"]
breakfast = st.multiselect("Chọn món cho bữa sáng", breakfast_options)


st.header("Bữa trưa")
lunch_main_options = ["Thịt kho tàu", "Cá kho", "Gà rán", "Thịt bò xào", "Tôm rim"]
lunch_side_options = ["Canh chua", "Canh rau ngót", "Rau muống xào", "Bí đỏ hầm"]

lunch_main = st.multiselect("Chọn 2 món mặn", lunch_main_options)
lunch_side = st.multiselect("Chọn 1 món rau hoặc canh", lunch_side_options)


st.header("Bữa tối")
dinner_main_options = ["Thịt rang", "Cá chiên", "Gà nướng", "Bò lúc lắc", "Mực xào"]
dinner_side_options = ["Canh cải", "Canh bí xanh", "Rau cải xào", "Canh khổ qua"]

dinner_main = st.multiselect("Chọn 2 món mặn", dinner_main_options)
dinner_side = st.multiselect("Chọn 1 món rau hoặc canh", dinner_side_options)


if st.button("📋 Xem thực đơn"):
    st.subheader("Thực đơn hôm nay:")

    st.write("**Bữa sáng:**", ", ".join(breakfast) if breakfast else "Chưa chọn")

    if len(lunch_main) == 2 and len(lunch_side) == 1:
        st.write("**Bữa trưa:**", ", ".join(lunch_main + lunch_side))
    else:
        st.warning(" Bữa trưa: Cần chọn đúng 2 món mặn và 1 món rau/canh.")

    if len(dinner_main) == 2 and len(dinner_side) == 1:
        st.write("**Bữa tối:**", ", ".join(dinner_main + dinner_side))
    else:
        st.warning(" Bữa tối: Cần chọn đúng 2 món mặn và 1 món rau/canh.")
