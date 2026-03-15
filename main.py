import streamlit as st
import sqlite3
import pandas as pd

# =========================
# Kết nối database
# =========================
conn = sqlite3.connect("tasks.db", check_same_thread=False)
cursor = conn.cursor()

# =========================
# Tạo bảng
# =========================
cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
description TEXT NOT NULL,
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

    cursor.execute("""
    INSERT INTO tasks
    (name, description, status, start_date, due_date, assignee, note)
    VALUES (?,?,?,?,?,?,?)
    """,(name,description,status,start_date,due_date,assignee,note))

    conn.commit()


# =========================
# Lấy danh sách task
# =========================
def get_tasks():

    cursor.execute("SELECT * FROM tasks")
    rows = cursor.fetchall()

    columns = [i[0] for i in cursor.description]

    df = pd.DataFrame(rows, columns=columns)

    return df


# =========================
# Cập nhật task
# =========================
def update_task(id,name,description,status,start_date,due_date,assignee,note):

    cursor.execute("""
    UPDATE tasks
    SET name=?,description=?,status=?,start_date=?,due_date=?,assignee=?,note=?
    WHERE id=?
    """,(name,description,status,start_date,due_date,assignee,note,id))

    conn.commit()


# =========================
# Xóa task
# =========================
def delete_task(task_id):

    cursor.execute("DELETE FROM tasks WHERE id=?",(task_id,))
    conn.commit()


# =========================
# Giao diện
# =========================
st.set_page_config(page_title="Task Manager", layout="wide")

st.title("📋 Task Manager")

menu = st.sidebar.selectbox(
"Menu",
["Thêm Task","Danh sách Task"]
)

# =========================
# THÊM TASK
# =========================
if menu == "Thêm Task":

    st.subheader("➕ Thêm công việc")

    with st.form("task_form"):

        name = st.text_input("Tên Task *")
        description = st.text_area("Mô tả *")

        status = st.selectbox(
        "Trạng thái",
        ["Đang làm","Hoàn thành","Tạm dừng"]
        )

        start_date = st.date_input("Ngày bắt đầu")

        due_date = st.date_input("Ngày kết thúc")

        assignee = st.text_input("Người phụ trách *")

        note = st.text_area("Ghi chú / Link")

        submit = st.form_submit_button("Thêm Task")

        if submit:

            if name == "" or description == "" or assignee == "":
                st.error("⚠️ Phải nhập đầy đủ thông tin bắt buộc")

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

                st.success("✅ Thêm task thành công")


# =========================
# DANH SÁCH TASK
# =========================
if menu == "Danh sách Task":

    st.subheader("📊 Danh sách công việc")

    df = get_tasks()

    if df.empty:

        st.info("Chưa có task")

    else:

        edited_df = st.data_editor(
        df,
        num_rows="dynamic",
        use_container_width=True
        )

        col1,col2 = st.columns(2)

        # Lưu chỉnh sửa
        with col1:

            if st.button("💾 Lưu chỉnh sửa"):

                for index,row in edited_df.iterrows():

                    update_task(
                    row["id"],
                    row["name"],
                    row["description"],
                    row["status"],
                    row["start_date"],
                    row["due_date"],
                    row["assignee"],
                    row["note"]
                    )

                st.success("Đã cập nhật dữ liệu")


        # Xóa task
        with col2:

            task_id = st.number_input("ID Task cần xóa",step=1)

            if st.button("❌ Xóa Task"):

                delete_task(task_id)

                st.success("Task đã bị xóa")
