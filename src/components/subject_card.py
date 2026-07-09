import streamlit as st
def subject_card(name, code, section, stats=None, footer_callback=None):
    html = f"""
        <div style="background:#1E293B; border-left: 8px solid #F59E0B; padding:25px; border-radius: 20px; border: 1px solid #334155; margin-bottom:20px; box-shadow: 0 2px 8px rgba(0,0,0,0.25);">
        <h3 style="margin:0; color: #F1F5F9; font-size: 1.5rem ">{name}</h3>
        <p style="color:#94A3B8; margin:10px 0;">Code : <span style="background:#0D948833; color:#5EEAD4; padding:2px 8px; border-radius:5px;">{code} </span> | Section : {section}</p>
        
        """
    
    if stats:
        html+= """
        <div style="display:flex; gap:8px; flex-wrap:wrap;">
        """
        for icon, label, value in stats:
            html+= f'<div style="background: #F59E0B22; color:#F1F5F9; padding:5px 12px; border-radius:12px; font-size:0.9rem">{icon} <b>{value}</b> {label} </div>'
        
        html+= "</div>"

    st.markdown(html, unsafe_allow_html=True)

    if footer_callback:
        footer_callback()