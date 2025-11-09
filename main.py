import pandas as pd
import streamlit as st


data = {
    "Tên khách hàng": ["DƯƠNG NGỌC BẢO TRÂN", "TRẦN THỊ MINH TÂM", "VÕ THIỆN TÍN"],
    "Gói sản phẩm": ["A", "B", "C"],
    "Số lượng": [2, 1, 3],
    "Giá gói": [100000, 500000, 50000],
    "Thành tiền": [200000, 500000, 150000]
}

df = pd.DataFrame(data)

# --- THÊM DÒNG MỚI ---
new_row = {
    "Tên khách hàng": "NGUYỄN NHẬT NAM",
    "Gói sản phẩm": "D",
    "Số lượng": 1,
    "Giá gói": 300000,
    "Thành tiền": 300000
}
df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

# --- TÍNH TỔNG THÀNH TIỀN ---
tong_thanh_tien = df["Thành tiền"].sum()

# --- SẮP XẾP THEO GIÁ GÓI TĂNG DẦN ---
df_sorted = df.sort_values(by="Giá gói", ascending=True)

# --- GIAO DIỆN STREAMLIT ---
st.title("📊 Quản lý đơn hàng khách hàng")

st.subheader("Dữ liệu đơn hàng (đã cập nhật)")
st.dataframe(df_sorted, use_container_width=True)

st.markdown(f"### 💰 Tổng thành tiền nhận được: **{tong_thanh_tien:,} VND**")
