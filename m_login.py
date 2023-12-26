# please do not change anything

def logout():
    st.session_state.logged_in = False
    st.session_state.username = None

def display_user_files(username):
    st.title("Your Uploaded Files")
    user_id = get_user_id(username)
    if user_id:
        cursor.execute("SELECT file_name, upload_time, LENGTH(file_content) FROM files WHERE user_id = ?", (user_id,))
        files = cursor.fetchall()
        if files:
            st.subheader("File History:")
            for file in files:
                file_name, upload_time, file_size = file
                upload_time = datetime.fromisoformat(upload_time)
                file_type = file_name.split(".")[-1]
                st.write(f"File Name: {file_name}")
                st.write(f"Uploaded on: {upload_time}")
                st.write(f"File Size: {file_size} bytes")
                st.write(f"File Type: {file_type.upper()}")
                st.write("---")
        else:
            st.write("You haven't uploaded any files yet.")