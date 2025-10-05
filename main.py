import csv
from prettytable import PrettyTable  # dùng để in bảng đẹp

# 🧾 Điền thông tin thời tiết bạn tra được từ accuweather.com tại đây:
data = [
    {
        "Thành phố": "Hà Nội",
        "Tình hình thời tiết": "Nhiều mây",
        "Nhiệt độ (°C)": 31,
        "Độ ẩm (%)": 70,
        "Tốc độ gió (km/h)": 10,
        "Chất lượng không khí": 45
    },
    {
        "Thành phố": "Hồ Chí Minh",
        "Tình hình thời tiết": "Nắng nhẹ",
        "Nhiệt độ (°C)": 33,
        "Độ ẩm (%)": 65,
        "Tốc độ gió (km/h)": 12,
        "Chất lượng không khí": 40
    },
    {
        "Thành phố": "Hải Phòng",
        "Tình hình thời tiết": "Có mưa rào",
        "Nhiệt độ (°C)": 29,
        "Độ ẩm (%)": 80,
        "Tốc độ gió (km/h)": 8,
        "Chất lượng không khí": 50
    },
    {
        "Thành phố": "Đà Nẵng",
        "Tình hình thời tiết": "Trời quang",
        "Nhiệt độ (°C)": 32,
        "Độ ẩm (%)": 60,
        "Tốc độ gió (km/h)": 14,
        "Chất lượng không khí": 42
    },
    {
        "Thành phố": "Cần Thơ",
        "Tình hình thời tiết": "Nhiều mây",
        "Nhiệt độ (°C)": 30,
        "Độ ẩm (%)": 75,
        "Tốc độ gió (km/h)": 11,
        "Chất lượng không khí": 47
    }
]

# 📂 Tên file CSV
filename = "weather_data.csv"

# ✍️ Ghi dữ liệu vào file CSV
with open(filename, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)

# 🧱 Tạo bảng hiển thị 5 cột
table = PrettyTable()
table.field_names = ["Thành phố", "Tình hình thời tiết", "Nhiệt độ (°C)", "Độ ẩm (%)", "Tốc độ gió (km/h)", "Chất lượng không khí"]

for row in data:
    table.add_row([row["Thành phố"], row["Tình hình thời tiết"], row["Nhiệt độ (°C)"], 
                   row["Độ ẩm (%)"], row["Tốc độ gió (km/h)"], row["Chất lượng không khí"]])

# 🖥️ In kết quả ra màn hình
print("✅ DỮ LIỆU THỜI TIẾT CÁC THÀNH PHỐ\n")
print(table)
print(f"\n📁 Dữ liệu đã được lưu trong file '{filename}' thành công!")
