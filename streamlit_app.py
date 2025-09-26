import streamlit as st
import subprocess
from datetime import datetime, timedelta
import streamlit.components.v1 as components
import zoneinfo
from timezone_listener import get_browser_timezone

timezone = get_browser_timezone()

if timezone:
    st.success(f"Detected Timezone: `{timezone}`")
    try:
        tzinfo = zoneinfo.ZoneInfo(timezone)
        offset = datetime.now(tzinfo).utcoffset().total_seconds() / 3600
        st.write(f"UTC Offset: `{offset:+.1f} hours`")
        st.session_state["timezone_offset"] = offset
    except Exception as e:
        st.error(f"Failed to compute offset: {e}")
else:
    st.info("Waiting for browser timezone…")




st.session_state.timezone_offset = -5



##=================================================================
## Function to show GitHub Status
##=================================================================
def git_status():
    ''' Retuns status of the GitHub library'''
    try:
        result = subprocess.run(["git", "status"], capture_output=True, text=True)
        st.subheader("🔍 Git Status")
        st.code(result.stdout)
    except Exception as e:
        st.error(f"Git status failed: {e}")


##================================================================
##=== Setup some one time variables
##================================================================
stss = st.session_state

if "show_balloons_once" not in st.session_state:
    stss.show_balloons_once = True


  
    
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


