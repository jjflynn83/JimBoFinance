# -*- coding: utf-8 -*-
"""
Created on Fri Sep 26 14:04:21 2025

@author: JJFly
"""
import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime
import zoneinfo

def capture_browser_timezone(session_key="timezone", offset_key="timezone_offset"):
    # Create a visible input for JS injection
    tz = st.text_input("Browser Timezone", key=session_key, label_visibility="collapsed")

    # Inject JavaScript to populate the input
    html_block = """
        <script>
            const tz = Intl.DateTimeFormat().resolvedOptions().timeZone;
            const input = window.parent.document.querySelector('input[data-testid="stTextInput"]');
            if (input && input.value === "") {{
                    input.value = tz;
                    input.dispatchEvent(new Event('input', {{ bubbles: true }}));
            }}
        </script>
        """
    components.html(html_block, height=0)

    # Display and log results
    if tz:
        st.session_state[session_key] = tz
        try:
            tzinfo = zoneinfo.ZoneInfo(tz)
            offset = datetime.now(tzinfo).utcoffset().total_seconds() / 3600
            st.session_state[offset_key] = offset
            st.success(f"🕒 Timezone: `{tz}` — UTC Offset: `{offset:+.1f} hours`")
        except Exception as e:
            st.session_state[offset_key] = 0.0
            st.warning(f"⚠️ Timezone detected but offset failed: {e}")
    else:
        st.session_state[offset_key] = 0.0
        st.info("Waiting for browser timezone…")