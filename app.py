import streamlit as st
from pathlib import Path

# Page configuration
st.set_page_config(
    page_title="Engineering AI Assistant",
    page_icon="👷‍♂️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Hide default page navigation and add custom styling
st.markdown("""
<style>
    /* Hide default streamlit page navigation */
    [data-testid="stSidebarNav"] {
        display: none;
    }
    
    /* Custom navigation styling */
    .nav-link {
        display: block;
        padding: 0.5rem 1rem;
        margin: 0.25rem 0;
        border-radius: 5px;
        text-decoration: none;
        color: #262730;
        background: #f0f2f6;
        transition: background 0.2s;
    }
    .nav-link:hover {
        background: #e0e2e6;
    }
    .nav-link.active {
        background: #ff4b4b;
        color: white;
    }
    
    /* Header styling */
    .main-header {
        background: linear-gradient(135deg, #1e3a5f 0%, #2d5a87 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    .main-header h1 {
        margin: 0;
        font-size: 2.5rem;
    }
    .main-header p {
        margin: 0.5rem 0 0 0;
        opacity: 0.9;
    }
    
    /* Status cards */
    .status-card {
        background: white;
        border-left: 4px solid #28a745;
        padding: 1rem;
        border-radius: 5px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }
    .status-card.warning {
        border-left-color: #ffc107;
    }
    .status-card.error {
        border-left-color: #dc3545;
    }
    
    /* Mode cards */
    .mode-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        height: 100%;
    }
    .mode-card h3 {
        margin-top: 0;
    }
</style>
""", unsafe_allow_html=True)

# Custom Sidebar Navigation (Admin Panel removed)
st.sidebar.title("🧭 Navigation")
st.sidebar.markdown("---")

# Navigation buttons using page_link - only Dashboard, Q&A, and Wizard
st.sidebar.page_link("app.py", label="🏡 Dashboard", icon=None)
st.sidebar.page_link("pages/1_QA_Mode.py", label="💬 Q&A Mode", icon=None)
st.sidebar.page_link("pages/2_Wizard_Mode.py", label="🧙‍♂️ Wizard Mode", icon=None)

st.sidebar.markdown("---")
st.sidebar.markdown("**Engineering AI Assistant**")
st.sidebar.markdown("v1.0 | Brentwood, TN")

# Main content
st.markdown("""
<div class="main-header">
    <h1>👷‍♂️ Engineering AI Assistant</h1>
    <p>Municipal Engineering Policy Support System</p>
</div>
""", unsafe_allow_html=True)

# Mode Selection Section (now at top, Admin Panel card removed)
st.subheader("🎯 Choose Your Mode")

# Changed to 2 columns since Admin Panel is removed
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 💬 Q&A Mode")
    st.markdown("Ask questions about engineering policies and get cited answers from the manual.")
    st.markdown("""
    **Features:**
    - Semantic search through manual
    - Source citations for every answer
    - Abstention when answer not found
    - Flagging system for feedback
    """)
    if st.button("🚀 Launch Q&A Mode", key="qa_btn"):
        st.switch_page("pages/1_QA_Mode.py")

with col2:
    st.markdown("### 🧙‍♂️ Wizard Mode")
    st.markdown("Step-by-step guidance for permit reviews and compliance checks.")
    st.markdown("""
    **Features:**
    - Interactive decision trees
    - Automated checklist generation
    - Compliance verification
    - Review documentation
    """)
    if st.button("🚀 Launch Wizard Mode", key="wizard_btn"):
        st.switch_page("pages/2_Wizard_Mode.py")

# Quick Start Guide (remains as expander)
st.markdown("---")
with st.expander("📚 Quick Start Guide"):
    st.markdown("""
    ### Getting Started
    
    1. **Q&A Mode**: Best for quick policy questions
       - Type your question in natural language
       - Review the cited answer and sources
       - Flag any responses that need improvement
    
    2. **Wizard Mode**: Best for permit reviews
       - Select the type of review (Transitional Lot, HP Lot, etc.)
       - Follow the step-by-step checklist
       - Generate compliance documentation
    
    ### Tips for Best Results
    
    - Be specific in your questions
    - Reference specific code sections when known
    - Use the feedback system to improve responses
    - Check multiple sources for complex questions
    """)

# System Status Section (moved to bottom, now as expander for developer use)
with st.expander("📊 System Status (Developer Info)"):
    col1, col2, col3 = st.columns(3)
    
    # Check vector database
    vectorstore_path = Path("vectorstore")
    vector_ready = vectorstore_path.exists()
    
    # Check manual file
    data_path = Path("data")
    manual_ready = data_path.exists()
    
    # Check API (we'll assume it's configured if secrets exist)
    try:
        api_ready = bool(st.secrets.get("CLAUDE_API_KEY"))
    except:
        api_ready = False
    
    with col1:
        if vector_ready:
            st.success("✅ **Vector Database**\n\nReady for searching")
        else:
            st.warning("⚠️ **Vector Database**\n\nNot initialized")
    
    with col2:
        if manual_ready:
            st.success("✅ **Engineering Manual**\n\nAvailable for reference")
        else:
            st.warning("⚠️ **Engineering Manual**\n\nNot found")
    
    with col3:
        if api_ready:
            st.success("✅ **Claude API**\n\nConfigured and ready")
        else:
            st.error("❌ **Claude API**\n\nNot configured")

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #666; font-size: 0.9rem;'>"
    "Engineering AI Assistant v1.0 | Powered by Claude API | Built with Streamlit"
    "</div>",
    unsafe_allow_html=True
)
