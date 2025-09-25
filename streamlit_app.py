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

# === Main User Page ===
st.title("💰 JimBo's Finance Fun 💰")
st.balloons()
log_timestamp("App launched")
git_status()


