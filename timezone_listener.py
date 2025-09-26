# -*- coding: utf-8 -*-
"""
Created on Fri Sep 26 14:32:00 2025

@author: JJFly
"""

import streamlit as st
import streamlit.components.v1 as components

_timezone_component = components.declare_component("timezone_listener", path="components/timezone")

def get_browser_timezone():
    return _timezone_component()
