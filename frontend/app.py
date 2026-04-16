import streamlit as st
import requests
import pandas as pd
from datetime import datetime
import os

# Page config
st.set_page_config(
    page_title="Data Flow IDE",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# API Configuration
API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8000")

# Custom CSS
st.markdown("""
<style>
    .main-header {
        text-align: center;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 30px;
        border-radius: 10px;
        color: white;
    }
    .metric-card {
        background: white;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class='main-header'>
    <h1>📊 Data Flow IDE</h1>
    <p>Professional Data Pipeline Management</p>
</div>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("🔧 Navigation")
    page = st.radio("Select Page", ["Upload", "Transform", "Export", "Settings"])
    st.divider()
    st.write("**API Status**")
    try:
        response = requests.get(f"{API_BASE_URL}/health", timeout=2)
        if response.status_code == 200:
            st.success("✅ Backend Connected")
        else:
            st.error("❌ Backend Error")
    except:
        st.error("❌ Backend Offline")

# Page routing
if page == "Upload":
    st.write("# 📤 Upload Data")
    uploaded_file = st.file_uploader("Upload CSV or Excel file", type=["csv", "xlsx", "xls"])
    if uploaded_file:
        st.success(f"✅ File uploaded: {uploaded_file.name}")
        df = pd.read_csv(uploaded_file) if uploaded_file.name.endswith('.csv') else pd.read_excel(uploaded_file)
        st.dataframe(df.head(10))

elif page == "Transform":
    st.write("# 🔄 Transform Data")
    st.info("Select columns to transform")

elif page == "Export":
    st.write("# 📥 Export Data")
    st.write("Export your processed data")

elif page == "Settings":
    st.write("# ⚙️ Settings")
    st.write(f"API URL: {API_BASE_URL}")
    st.write(f"Timestamp: {datetime.now().isoformat()}")