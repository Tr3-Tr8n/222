import streamlit as st
import sqlite3
import pandas as pd

# =========================
# Kết nối SQLite
# =========================
conn = sqlite3.connect("tasks.db", check_same_thread=False)
c = conn.cursor()

# Tạo bảng
c.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    description TEXT,
    status TEXT,
    start_date TEXT,
    due_date TEXT,
    assignee TEXT,
    note TEXT
)
""")
conn.commit()


# =========================
# Hàm thêm task
# =========================
def add_task(name, description, status, start_date, due_date, assignee, note):
    c.execute("""
    INSERT INTO tasks (name, description, status, start_date, due_date, assignee, note)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (name, description, status, start_date, due_date, assignee, note))
    conn.commit()


# =========================
# Lấy danh sách task
# =========================
def get_tasks():
    c.execute("SELECT * FROM tasks")
    data = c.fetchall()
    df = pd.DataFrame(data, columns=[
        "ID","Tên Task","Mô tả","Trạng thái",
        "Ngày bắt đầu","Ngày kết thúc",
        "Người phụ trách","Ghi chú"
    ])
    return df


# =========================
# Cập nhật task
# =========================
def update_task(id, name, description, status, start_date, due_date, assignee, note):
    c.execute("""
    UPDATE tasks
    SET name=?, description=?, status=?, start_date=?, due_date=?, assignee=?, note=?
    WHERE id=?
    """, (name, description, status, start_date, due_date, assignee, note, id))
    conn.commit()


# =========================
# Giao diện
# =========================
st.set_page_config(page_title="Task Manager", layout="wide")

st.title("📋 Task Manager")

menu = ["Thêm Task", "Danh sách Task"]
choice = st.sidebar.selectbox("Menu", menu)


# =========================
# Thêm Task
# =========================
if choice == "Thêm Task":

    st.subheader("➕ Thêm công việc")

    with st.form("task_form"):

        name = st.text_input("Tên task *")
        description = st.text_area("Mô tả *")

        status = st.selectbox(
            "Trạng thái *",
            ["Đang làm", "Hoàn thành", "Tạm dừng"]
        )

        start_date = st.date_input("Ngày bắt đầu *")
        due_date = st.date_input("Ngày kết thúc *")

        assignee = st.text_input("Người phụ trách *")

        note = st.text_area("Ghi chú / Link")

        submit = st.form_submit_button("Thêm Task")

        # Kiểm tra bắt buộc nhập
        if submit:

            if name == "" or description == "" or assignee == "":
                st.error("⚠️ Bạn phải nhập đầy đủ thông tin bắt buộc!")
            else:
                add_task(
                    name,
                    description,
                    status,
                    str(start_date),
                    str(due_date),
                    assignee,
                    note
                )
                st.success("✅ Thêm task thành công!")


# =========================
# Danh sách Task
# =========================
elif choice == "Danh sách Task":

    st.subheader("📊 Danh sách công việc")

    df = get_tasks()

    if df.empty:
        st.info("Chưa có task nào")
    else:

        # Hiển thị bảng
        edited_df = st.data_editor(
            df,
            num_rows="dynamic",
            use_container_width=True
        )

        # Nút lưu chỉnh sửa
        if st.button("💾 Lưu thay đổi"):

            for index, row in edited_df.iterrows():

                update_task(
                    row["ID"],
                    row["Tên Task"],
                    row["Mô tả"],
                    row["Trạng thái"],
                    row["Ngày bắt đầu"],
                    row["Ngày kết thúc"],
                    row["Người phụ trách"],
                    row["Ghi chú"]
                )

            st.success("✅ Đã cập nhật dữ liệu!")
