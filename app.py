import streamlit as st
import os
from pathlib import Path

# This line configures how your web page looks and behaves
# Think of it like setting the name, logo, and layout of your restaurant
st.set_page_config(
    page_title="Engineering AI Assistant",     # What shows in the browser tab
    page_icon="🏗️",                            # The emoji that shows in the tab
    layout="wide",                             # Use the full width of the screen
    initial_sidebar_state="expanded"           # Start with the sidebar open
)

# This is CSS code that makes your app look professional
# CSS is like the interior design rules for your restaurant
# You don't need to understand CSS - just know it makes things look good
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #1f4e79 0%, #2d5aa0 100%);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        text-align: center;
    }
    .status-card {
        background: #f8f9fa;
        border: 1px solid #dee2e6;
        border-radius: 8px;
        padding: 1rem;
        margin: 0.5rem 0;
    }
    .success { border-left: 4px solid #28a745; }
    .warning { border-left: 4px solid #ffc107; }
    .info { border-left: 4px solid #17a2b8; }
</style>
""", unsafe_allow_html=True)

def check_system_status():
    """
    This function checks if all the required parts of your system are working
    Think of it like a restaurant manager checking if the kitchen, dining room,
    and staff are all ready before opening for business
    """
    # Create a dictionary to track what's working and what isn't
    # A dictionary in Python is like a checklist with items and their status
    status = {
        'vector_db': False,      # Is the search database ready?
        'manual_file': False,    # Is the engineering manual file available?
        'api_configured': False  # Is the Claude API key set up correctly?
    }
    
    # Check if the vector database exists and has files in it
    # The vector database is like your restaurant's recipe collection
    vectorstore_path = Path("vectorstore")  # Look in the vectorstore folder
    if vectorstore_path.exists() and any(vectorstore_path.iterdir()):
        status['vector_db'] = True  # Mark as working if folder exists and has files
    
    # Check if the original manual file is available
    # This is like checking if you have the original cookbook
    manual_path = Path("data/Engineering_Manual.docx")  # Look for the manual file
    if manual_path.exists():  # If the file exists
        status['manual_file'] = True  # Mark it as available
    
    # Check if the Claude API key is properly configured
    # API key is like having a phone number to call Claude for help
    try:
        claude_key = st.secrets.get("CLAUDE_API_KEY", "")  # Try to get the API key
        if claude_key and claude_key.startswith("sk-ant-"):  # Check if it looks right
            status['api_configured'] = True  # Mark as configured
    except:
        pass  # If there's any error, just leave it as False
    
    return status  # Return the checklist of what's working

def main():
    """
    This is the main function that creates your home page
    Think of it as the function that sets up your restaurant's front entrance
    """
    # Create the main header (like a big sign at your restaurant entrance)
    st.markdown("""
    <div class="main-header">
        <h1>🏗️ Engineering AI Assistant</h1>
        <p>Municipal Engineering Policy Support System</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Check what's working and what isn't (like a daily system check)
    st.subheader("📊 System Status")
    status = check_system_status()  # Call our checking function
    
    # Create three columns to show status side by side
    # Think of this like having three information boards at your entrance
    col1, col2, col3 = st.columns(3)
    
    # Column 1: Vector Database status
    with col1:
        if status['vector_db']:  # If the database is working
            st.markdown("""
            <div class="status-card success">
                <h4>✅ Vector Database</h4>
                <p>Ready for searching</p>
            </div>
            """, unsafe_allow_html=True)
        else:  # If the database is not working
            st.markdown("""
            <div class="status-card warning">
                <h4>⚠️ Vector Database</h4>
                <p>Not found - run notebook first</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Column 2: Engineering Manual status
    with col2:
        if status['manual_file']:  # If the manual file exists
            st.markdown("""
            <div class="status-card success">
                <h4>✅ Engineering Manual</h4>
                <p>Available for reference</p>
            </div>
            """, unsafe_allow_html=True)
        else:  # If the manual file is missing
            st.markdown("""
            <div class="status-card warning">
                <h4>⚠️ Engineering Manual</h4>
                <p>Upload to data folder</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Column 3: Claude API status
    with col3:
        if status['api_configured']:  # If the API key is set up
            st.markdown("""
            <div class="status-card success">
                <h4>✅ Claude API</h4>
                <p>Configured and ready</p>
            </div>
            """, unsafe_allow_html=True)
        else:  # If the API key is not set up
            st.markdown("""
            <div class="status-card warning">
                <h4>⚠️ Claude API</h4>
                <p>Add key to secrets</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Create the main navigation section (like a menu of restaurant options)
    st.subheader("🎯 Choose Your Mode")
    
    # Create three columns for the three main features
    col1, col2, col3 = st.columns(3)
    
    # Column 1: Q&A Mode (like ordering from a menu)
    with col1:
        st.markdown("""
        ### 💬 Q&A Mode
        Ask questions about engineering policies and get cited answers from the manual.
        
        **Features:**
        - Semantic search through manual
        - Source citations for every answer
        - Abstention when answer not found
        - Flagging system for feedback
        """)
        # Create a button that takes users to the Q&A page
        if st.button("🚀 Launch Q&A Mode", key="qa_mode"):
            st.switch_page("pages/1_QA_Mode.py")  # Go to the Q&A page
    
    # Column 2: Wizard Mode (like having a personal assistant)
    with col2:
        st.markdown("""
        ### 🧙‍♂️ Wizard Mode
        Step-by-step guidance for permit reviews and compliance checks.
        
        **Features:**
        - Interactive decision trees
        - Automated checklist generation
        - Compliance verification
        - Review documentation
        """)
        # Create a button that takes users to the Wizard page
        if st.button("🚀 Launch Wizard Mode", key="wizard_mode"):
            st.switch_page("pages/2_Wizard_Mode.py")  # Go to the Wizard page
    
    # Column 3: Admin Panel (like the manager's office)
    with col3:
        st.markdown("""
        ### ⚙️ Admin Panel
        Monitor system usage, review flagged responses, and manage the system.
        
        **Features:**
        - Query audit logs
        - Response monitoring
        - User feedback review
        - System management
        """)
        # Create a button that takes users to the Admin page
        if st.button("🚀 Launch Admin Panel", key="admin_mode"):
            st.switch_page("pages/3_Admin.py")  # Go to the Admin page
    
    # Create a help section that users can expand if they need guidance
    with st.expander("📚 Quick Start Guide"):
        st.markdown("""
        ### First Time Setup:
        1. **Upload your manual** to the `data/` folder
        2. **Run the development notebook** to process your manual
        3. **Add your Claude API key** to Streamlit secrets
        4. **Test Q&A mode** with a sample question
        5. **Try wizard mode** for permit review workflows
        
        ### Daily Usage:
        - **Q&A Mode**: Ask policy questions, flag incorrect responses
        - **Wizard Mode**: Guide permit reviews and compliance checks
        - **Admin Panel**: Monitor usage and review flagged items weekly
        
        ### Need Help?
        - Check system status above for configuration issues
        - Review the documentation in your project folder
        - Contact your system administrator for technical support
        """)
    
    # Create a footer with system information
    st.markdown("---")  # This creates a horizontal line
    st.markdown("""
    <div style='text-align: center; color: #666;'>
        <p>Engineering AI Assistant v1.0 | Powered by Claude API | Built with Streamlit</p>
        <p>Municipal Engineering Department | ECE 570 Course Project</p>
    </div>
    """, unsafe_allow_html=True)

# This is the standard Python way to run the main function when the file is executed
if __name__ == "__main__":
    main()  # Call the main function to set up the page
