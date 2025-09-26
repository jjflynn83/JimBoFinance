import streamlit as st
import subprocess
from datetime import datetime, timedelta
import streamlit.components.v1 as components



def git_status():
    ''' Retuns status of the GitHub library'''
    try:
        result = subprocess.run(["git", "status"], capture_output=True, text=True)
        st.subheader("🔍 Git Status")
        st.code(result.stdout)
    except Exception as e:
        st.error(f"Git status failed: {e}")



def get_user_timezone_offset() -> str:
    components.html("""
        <script>
            const offsetMinutes = new Date().getTimezoneOffset();
            const offsetHours = -offsetMinutes / 60;
            const input = window.parent.document.querySelector('input[name="user_offset"]');
            if (input) input.value = offsetHours;
            const form = window.parent.document.querySelector('form');
            if (form) form.dispatchEvent(new Event('submit', { bubbles: true }));
        </script>
    """, height=0)

    with st.expander("Debug: Timezone Offset", expanded=False):
        return st.text_input("user_offset", value="0")








##================================================================
##=== Setup some one time variables
##================================================================
stss = st.session_state

if "show_balloons_once" not in st.session_state:
    stss.show_balloons_once = True


raw_offset = get_user_timezone_offset()

try:
    offset = float(raw_offset)
    st.write(f"📍 raw_offset: `{offset}`")

    # Only store if offset is non-zero and hasn't been stored yet
    if offset != 0.0 and "timezone_offset" not in st.session_state:
        st.session_state.timezone_offset = offset
        st.write(f"✅ Stored timezone_offset: `{offset}`")
    else:
        stss.timezone_offset = 0.0
except:
    st.warning("⚠️ Could not parse timezone offset.")
    stss.timezone_offset = 0.0

   
    
if "home_launch_time" not in st.session_state:
    #stss.home_launch_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    stss.home_launch_time = (datetime.utcnow() \
                          + timedelta(hours=stss.timezone_offset) \
                          ).strftime("%Y-%m-%d %H:%M:%S")
    
    
### Start at the home page
if "page" not in st.session_state:
    stss.page = "Home"



##================================================================
##=== Setup some one time variables
##================================================================
def go_home():
    stss.page = "Home"

def go_github_status():
    stss.page = "GitHub Status"




##================================================================
##=== Page: Home
##================================================================
if stss.page == "Home":
   st.title("💰 JimBo's Finance Fun 💰")
   if stss.show_balloons_once:
      stss.show_balloons_once = False
      st.balloons()  ## This jumps back to top so do it last
   st.write(f"App launched at: `{stss.home_launch_time}`")
   st.write(f"timezone offset: {stss.timezone_offset}")
   mytime = ( datetime.utcnow() \
            + timedelta(hours=stss.timezone_offset) \
            ).strftime("%Y-%m-%d %H:%M:%S")
   st.write(f"Page launched at: `{mytime}`")
   st.button("GitHub Status", on_click=go_github_status)



##================================================================
##== Page: GitHub Status
##================================================================
elif st.session_state.page == "GitHub Status":
    st.title("💰 JimBo's GitHub Status 💰")
    st.write(f"App launched at: `{stss.home_launch_time}`")
    mytime = ( datetime.utcnow() \
             + timedelta(hours=stss.timezone_offset) \
             ).strftime("%Y-%m-%d %H:%M:%S")
    st.write(f"Page launched at: `{mytime}`")

    # Git status
    try:
        result = subprocess.run(["git", "status"], capture_output=True, text=True)
        st.subheader("🔍 Git Status")
        st.code(result.stdout)
    except Exception as e:
        st.error(f"Git status failed: {e}")

    st.button("Return to Home", on_click=go_home)


