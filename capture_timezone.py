# -*- coding: utf-8 -*-
"""
Created on Fri Sep 26 14:04:21 2025

@author: JJFly
"""
import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime
import zoneinfo

def capture_browser_timezone(session_key="browser_tz", offset_key="timezone_offset"):
    # Create a visible input for JS injection
    tz = st.text_input("Browser Timezone", key=session_key, label_visibility="collapsed")

    # Inject JavaScript to populate the input
    components.html(f"""
    <script>
        const tz = Intl.DateTimeFormat().resolvedOptions().timeZone;
        const input = window.parent.document.querySelector('input[data-testid="stTextInput"]');
        if (input && input.value === "") {{
            input.value = tz;
            input.dispatchEvent(new Event('input', {{ bubbles: true }}));
        }}
    </script>
    """, height=0)

    # Compute offset and return it
    if tz:
        try:
            tzinfo = zoneinfo.ZoneInfo(tz)
            offset = datetime.now(tzinfo).utcoffset().total_seconds() / 3600
            st.session_state[offset_key] = offset
            return offset
        except Exception as e:
            st.session_state[offset_key] = 0.0
            return 0.0
    else:
        st.session_state[offset_key] = 0.0
        return 0.0
