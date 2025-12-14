import streamlit as st
import pandas as pd

st.set_page_config(page_title="Phân tích dữ liệu nhà ở", layout="wide")

st.title("📊 PHÂN TÍCH DỮ LIỆU NHÀ Ở (KHÔNG DÙNG read_csv)")

# 1. Tạo dữ liệu trực tiếp trong code
data = {
    'ID': list(range(1, 61)),
    'Quận/Huyện': [
        'Hoàn Kiếm','Ba Đình','Thanh Xuân','Cầu Giấy','Cầu Giấy','Hai Bà Trưng','Hoàn Kiếm','Hoàn Kiếm','Tây Hồ','Ba Đình',
        'Ba Đình','Hoàn Kiếm','Cầu Giấy','Cầu Giấy','Ba Đình','Cầu Giấy','Tây Hồ','Cầu Giấy','Long Biên','Thanh Xuân',
        'Ba Đình','Hai Bà Trưng','Tây Hồ','Đống Đa','Thanh Xuân','Hai Bà Trưng','Cầu Giấy','Đống Đa','Hoàn Kiếm','Hoàn Kiếm',
        'Tây Hồ','Hoàn Kiếm','Đống Đa','Đống Đa','Thanh Xuân','Ba Đình','Long Biên','Hoàn Kiếm','Tây Hồ','Hoàn Kiếm',
        'Thanh Xuân','Đống Đa','Cầu Giấy','Hoàn Kiếm','Ba Đình','Cầu Giấy','Thanh Xuân','Hoàn Kiếm','Cầu Giấy','Hoàn Kiếm',
        'Tây Hồ','Thanh Xuân','Long Biên','Đống Đa','Hai Bà Trưng','Đống Đa','Đống Đa','Cầu Giấy','Thanh Xuân','Hoàn Kiếm'
    ],
    'Diện tích (m2)': [205,212,93,186,236,112,91,168,147,119,286,213,226,192,106,225,133,265,246,248,64,108,260,58,256,130,152,118,66,104,283,291,195,274,233,130,104,217,177,151,276,284,214,167,86,117,85,113,240,193,187,117,241,199,159,279,199,152,142,106],
    'Giá bán/m2': [
        46.49,102.33,227.64,42.89,126.12,58.41,94.41,59.57,173.87,86.06,
        95.44,88.41,108.59,36.88,166.11,77.79,184.40,76.74,90.80,53.37,
        361.37,49.77,104.96,493.37,34.19,210.29,148.65,250.88,208.22,250.02,
        57.05,29.74,74.95,70.24,43.69,152.82,49.09,132.07,161.48,90.26,
        77.54,105.51,50.71,129.55,98.67,217.85,173.87,229.53,90.14,129.29,
        61.58,85.53,71.58,150.67,64.73,81.26,112.45,33.01,173.42,147.36
    ],
    'Loại hình nhà ở': [
        'Nhà cấp 4','Nhà phố','Nhà phố','Biệt thự','Biệt thự','Chung cư','Nhà phố','Chung cư','Nhà phố','Nhà phố',
        'Nhà cấp 4','Nhà phố','Chung cư','Chung cư','Nhà cấp 4','Chung cư','Biệt thự','Nhà cấp 4','Chung cư','Chung cư',
        'Biệt thự','Nhà cấp 4','Biệt thự','Nhà cấp 4','Nhà cấp 4','Nhà phố','Chung cư','Chung cư','Nhà phố','Biệt thự',
        'Nhà phố','Chung cư','Chung cư','Nhà phố','Nhà phố','Nhà phố','Chung cư','Nhà phố','Nhà phố','Biệt thự',
        'Nhà phố','Chung cư','Biệt thự','Nhà cấp 4','Chung cư','Chung cư','Nhà cấp 4','Chung cư','Nhà cấp 4','Nhà cấp 4',
        'Chung cư','Nhà phố','Nhà phố','Nhà cấp 4','Biệt thự','Nhà cấp 4','Nhà cấp 4','Nhà cấp 4','Nhà phố','Nhà phố'
    ]
}

df = pd.DataFrame(data)

# 2. Hiển thị dữ liệu
a = st.checkbox("📋 Hiển thị toàn bộ dữ liệu")
if a:
    st.dataframe(df, use_container_width=True)

# 3. Lọc nhà giá > 100 triệu/m2
st.subheader("🏠 Nhà có giá > 100 triệu/m²")
nha_tren_100 = df[df['Giá bán/m2'] > 100]
st.dataframe(nha_tren_100, use_container_width=True)

# 4. Phân tích theo quận/huyện
st.subheader("📍 Giá nhà trung bình theo quận/huyện")
gia_quan = df.groupby('Quận/Huyện')['Giá bán/m2'].mean().sort_values(ascending=False)
st.bar_chart(gia_quan)

st.write("🔺 Quận giá cao nhất:", gia_quan.idxmax())
st.write("🔻 Quận giá thấp nhất:", gia_quan.idxmin())

# 5. Phân tích theo loại hình nhà ở
st.subheader("🏘️ Giá nhà theo loại hình")
gia_loai = df.groupby('Loại hình nhà ở')['Giá bán/m2'].mean()
st.bar_chart(gia_loai)

# 6. Nhà đắt nhất & rẻ nhất
st.subheader("💰 Nhà đắt nhất và rẻ nhất")
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🏆 Đắt nhất")
    st.write(df.loc[df['Giá bán/m2'].idxmax()])

with col2:
    st.markdown("### 🪙 Rẻ nhất")
    st.write(df.loc[df['Giá bán/m2'].idxmin()])

st.success("✔️ Hoàn thành phân tích dữ liệu")
