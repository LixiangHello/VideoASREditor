"""
@File    :   webdemo.py
@Time    :   2024/10/19 11:41:57
@Author  :   lixiang
"""

import streamlit as st
import tempfile
import os

state = st.session_state


def init():
    state.setdefault("save_root", tempfile.gettempdir())


def body():
    with st.container(height=300):
        cols = st.columns(2)
        ori_video, new_video = cols[0], cols[1]


def main():
    init()
    body()


if __name__ == "__main__":
    main()
