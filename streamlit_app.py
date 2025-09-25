import streamlit as st
import subprocess
from datetime import datetime

def git_status():
    try:
        result = subprocess.run(["git", "status"], capture_output=True, text=True)
        st.subheader("🔍 Git Status")
        st.code(result.stdout)
    except Exception as e:
        st.error(f"Git status failed: {e}")

def log_timestamp(label: str = "Session started"):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.text(f"{label}: {now}")

# === Navigation setup ===
if "page" not in st.session_state:
    st.session_state.page = "Home"

def go_home():
    st.session_state.page = "Home"

def go_github_status():
    st.session_state.page = "GitHub Status"

# === Page: Home =================================================
if st.session_state.page == "Home":
   st.title("💰 JimBo's Finance Fun 💰")
   st.balloons()
   log_timestamp("App launched")
   st.button("GitHub Status", on_click=go_github_status())
   
elif st.session_state.page == "GitHub Status":
    st.title("💰 JimBo's GitHub Status 💰")
    log_timestamp("App launched")
    launch_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.write(f"App launched at: `{launch_time}`")

    # Git status
    try:
        result = subprocess.run(["git", "status"], capture_output=True, text=True)
        st.subheader("🔍 Git Status")
        st.code(result.stdout)
    except Exception as e:
        st.error(f"Git status failed: {e}")

    st.button("Return to Home", on_click=go_home)


