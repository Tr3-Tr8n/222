import streamlit as st
import sqlite3
import pandas as pd


conn = sqlite3.connect("tasks.db", check_same_thread=False)
c = conn.cursor()

# Tạo bảng tasks nếu chưa tồn tại
c.execute('''
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    status TEXT,
    due_date TEXT,
    assignee TEXT,
    note TEXT
)
''')
conn.commit()

# =========================
# Hàm thêm task
# =========================
def add_task(name, description, status, due_date, assignee, note):
    c.execute('''
    INSERT INTO tasks (name, description, status, due_date, assignee, note)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (name, description, status, due_date, assignee, note))
    conn.commit()

# =========================
# Hàm lấy danh sách task
# =========================
def get_tasks():
    c.execute("SELECT * FROM tasks")
    data = c.fetchall()
    df = pd.DataFrame(data, columns=['ID', 'Tên task', 'Mô tả', 'Trạng thái', 'Ngày', 'Người phụ trách', 'Ghi chú'])
    return df

# =========================
# Streamlit UI
# =========================
st.set_page_config(page_title="Task Manager", layout="wide")

# Header
st.title("📋 Task Manager")

# Menu sidebar
menu = ["Thêm Task", "Danh sách Task"]
choice = st.sidebar.selectbox("Chọn chức năng", menu)

# =========================
# Thêm Task
# =========================
if choice == "Thêm Task":
    st.subheader("➕ Thêm công việc mới")

    with st.form("task_form"):
        name = st.text_input("Tên task")
        description = st.text_area("Mô tả")
        status = st.selectbox("Trạng thái", ["Đang làm", "Hoàn thành", "Tạm dừng"])
        due_date = st.date_input("Ngày hết hạn")
        assignee = st.text_input("Người phụ trách")
        note = st.text_area("Ghi chú / Link liên quan")
        submit = st.form_submit_button("Thêm Task")

        if submit:
            add_task(name, description, status, due_date.strftime("%Y-%m-%d"), assignee, note)
            st.success(f"Task '{name}' đã được thêm!")

# =========================
# Hiển thị danh sách Task
# =========================
elif choice == "Danh sách Task":
    st.subheader("📊 Danh sách Task")

    df = get_tasks()

    if not df.empty:
        # Hiển thị bảng
        st.dataframe(df, use_container_width=True)

        # Tìm kiếm theo tên hoặc người phụ trách
        search_name = st.text_input("Tìm theo tên task")
        search_assignee = st.text_input("Tìm theo người phụ trách")

        filtered_df = df.copy()
        if search_name:
            filtered_df = filtered_df[filtered_df['Tên task'].str.contains(search_name, case=False)]
        if search_assignee:
            filtered_df = filtered_df[filtered_df['Người phụ trách'].str.contains(search_assignee, case=False)]

        st.dataframe(filtered_df, use_container_width=True)

    else:
        st.info("Chưa có task nào trong danh sách.")