import streamlit as st
import sqlite3
import pandas as pd

# =========================
# DATABASE
# =========================

conn = sqlite3.connect("tasks.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks(
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
# FUNCTIONS
# =========================

def add_task(name,description,status,start_date,due_date,assignee,note):

    cursor.execute("""
    INSERT INTO tasks
    (name,description,status,start_date,due_date,assignee,note)
    VALUES (?,?,?,?,?,?,?)
    """,(name,description,status,start_date,due_date,assignee,note))

    conn.commit()


def get_tasks():

    cursor.execute("SELECT * FROM tasks")

    data = cursor.fetchall()

    columns = [i[0] for i in cursor.description]

    df = pd.DataFrame(data,columns=columns)

    return df


def update_task(id,name,description,status,start_date,due_date,assignee,note):

    cursor.execute("""
    UPDATE tasks
    SET name=?,description=?,status=?,start_date=?,due_date=?,assignee=?,note=?
    WHERE id=?
    """,(name,description,status,start_date,due_date,assignee,note,id))

    conn.commit()


def delete_task(id):

    cursor.execute("DELETE FROM tasks WHERE id=?",(id,))
    conn.commit()


# =========================
# UI
# =========================

st.set_page_config(page_title="Task Manager",layout="wide")

st.title("📋 Task Manager")

menu = st.sidebar.selectbox(
"Menu",
["Thêm Task","Danh sách Task"]
)


# =========================
# ADD TASK
# =========================

if menu == "Thêm Task":

    st.subheader("➕ Thêm công việc")

    name = st.text_input("Tên task *")

    description = st.text_area("Mô tả *")

    status = st.selectbox(
    "Trạng thái",
    ["Đang làm","Hoàn thành","Tạm dừng"]
    )

    start_date = st.date_input("Ngày bắt đầu")

    due_date = st.date_input("Ngày kết thúc")

    assignee = st.text_input("Người phụ trách *")

    note = st.text_area("Ghi chú")

    if st.button("Thêm Task"):

        if name == "" or description == "" or assignee == "":
            st.error("⚠️ Phải nhập đầy đủ thông tin")

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

            st.success("✅ Task đã được thêm")

            st.rerun()


# =========================
# TASK LIST
# =========================

if menu == "Danh sách Task":

    st.subheader("📊 Danh sách công việc")

    df = get_tasks()

    if df.empty:

        st.info("Chưa có task")

    else:

        st.write("✏️ Bạn có thể chỉnh sửa trực tiếp trong bảng")

        edited_df = st.data_editor(
        df,
        use_container_width=True,
        num_rows="dynamic"
        )

        # SAVE BUTTON
        if st.button("💾 Save Changes"):

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

            st.success("✅ Đã lưu thay đổi")

        st.divider()

        # DELETE TASK
        st.subheader("❌ Xóa Task")

        delete_id = st.number_input("Nhập ID task cần xóa",step=1)

        if st.button("Delete Task"):

            delete_task(delete_id)

            st.success("Task đã bị xóa")

            st.rerun()
