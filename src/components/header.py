import streamlit as st
import base64
from pathlib import Path


def get_logo_base64():
    logo_path = Path(__file__).parent.parent.parent / "assets" / "rollcall-ai-logo.svg"
    logo_bytes = logo_path.read_bytes()
    return base64.b64encode(logo_bytes).decode()


def header_home():

    logo_b64 = get_logo_base64()
    
    st.markdown(f"""
        <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:30px; margin-top:30px">
            <img src='data:image/svg+xml;base64,{logo_b64}' style='height:100px;' />
        </div>   
                
                """, unsafe_allow_html=True)


def header_dashboard():

    logo_b64 = get_logo_base64()
    
    st.markdown(f"""
        <div style="display:flex; align-items:center; justify-content:center; gap:10px">
            <img src='data:image/svg+xml;base64,{logo_b64}' style='height:85px;' />
        </div>   
                
                """, unsafe_allow_html=True)