import streamlit as st
import streamlit.components.v1 as components

_timezone_component = components.declare_component("timezone_listener", path="components/timezone")

def get_browser_timezone():
    return _timezone_component()
