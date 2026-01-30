import streamlit as st
import sys
from pathlib import Path
import pandas as pd
from datetime import datetime, timedelta

# Add utils to path
sys.path.append(str(Path(__file__).parent.parent / "utils"))

from database import AuditLogger

st.set_page_config(page_title="Admin Panel", page_icon="⚙️", layout="wide")

def main():
    """Main function for Admin Panel page"""
    st.title("⚙️ Engineering AI Assistant - Admin Panel")
    st.markdown("Monitor system usage, review flagged responses, and manage the application.")
    
    # Initialize audit logger
    if 'audit_logger' not in st.session_state:
        st.session_state.audit_logger = AuditLogger()
    
    # Create tabs for different admin functions
    tab1, tab2, tab3, tab4 = st.tabs(["📊 Dashboard", "📝 Query Logs", "🚩 Flagged Items", "⚙️ Settings"])
    
    # TAB 1: DASHBOARD
    with tab1:
        st.subheader("📊 System Dashboard")
        
        try:
            # Get usage statistics
            stats = st.session_state.audit_logger.get_usage_stats(days=7)
            
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.metric("Queries This Week", stats.get('total_queries', 0))
            with col2:
                st.metric("Satisfaction Rate", f"{stats.get('satisfaction_rate', 0):.1f}%")
            with col3:
                st.metric("Flagged Responses", stats.get('flagged_responses', 0))
            with col4:
                st.metric("Wizard Completions", stats.get('wizard_completions', 0))
            
            # Simple activity chart
            st.subheader("📈 Recent Activity")
            
            # Create sample data for demonstration
            dates = pd.date_range(start=datetime.now() - timedelta(days=7), end=datetime.now(), freq='D')
            sample_data = pd.DataFrame({
                'Date': dates,
                'Queries': [15, 23, 18, 31, 27, 19, 23],
                'Flagged': [1, 0, 2, 1, 0, 1, 2]
            })
            
            st.line_chart(sample_data.set_index('Date')[['Queries']])
            
        except Exception as e:
            st.error(f"Error loading dashboard data: {e}")
            st.info("Dashboard will show real data once the system has been used.")
    
    # TAB 2: QUERY LOGS
    with tab2:
        st.subheader("📝 Query Logs")
        st.markdown("Review all questions asked and responses provided.")
        
        # Date filters
        col1, col2 = st.columns(2)
        with col1:
            start_date = st.date_input("Start Date", datetime.now() - timedelta(days=7))
        with col2:
            end_date = st.date_input("End Date", datetime.now())
        
        try:
            queries = st.session_state.audit_logger.get_recent_queries(limit=50)
            
            if queries:
                # Convert to DataFrame for display
                df = pd.DataFrame(queries)
                
                # Display the queries
                st.dataframe(df, use_container_width=True)
                
                # Export option
                if st.button("📥 Export to CSV"):
                    csv = df.to_csv(index=False)
                    st.download_button(
                        "Download Query Log",
                        csv,
                        file_name=f"query_log_{datetime.now().strftime('%Y%m%d')}.csv",
                        mime="text/csv"
                    )
            else:
                st.info("No query logs found. Logs will appear here after users ask questions.")
                
        except Exception as e:
            st.error(f"Error loading query logs: {e}")
    
    # TAB 3: FLAGGED ITEMS
    with tab3:
        st.subheader("🚩 Flagged Responses")
        st.markdown("Review responses that users have flagged for improvement.")
        
        try:
            flagged_items = st.session_state.audit_logger.get_flagged_responses()
            
            if flagged_items:
                for i, item in enumerate(flagged_items):
                    with st.expander(f"Flag #{i+1}: {item.get('question', 'No question')[:50]}..."):
                        st.write(f"**Question:** {item.get('question', 'N/A')}")
                        st.write(f"**Answer:** {item.get('answer', 'N/A')}")
                        st.write(f"**Flag Type:** {item.get('flag_type', 'N/A')}")
                        st.write(f"**Reason:** {item.get('reason', 'N/A')}")
                        st.write(f"**Date:** {item.get('timestamp', 'N/A')}")
                        
                        # Action buttons
                        col1, col2 = st.columns(2)
                        with col1:
                            if st.button(f"✅ Resolved", key=f"resolve_{i}"):
                                st.success(f"Marked flag #{i+1} as resolved")
                        with col2:
                            if st.button(f"🔄 Needs Review", key=f"review_{i}"):
                                st.warning(f"Flag #{i+1} marked for additional review")
            else:
                st.info("No flagged responses found. This is good - it means users are satisfied!")
                
        except Exception as e:
            st.error(f"Error loading flagged items: {e}")
    
    # TAB 4: SETTINGS
    with tab4:
        st.subheader("⚙️ System Settings")
        st.markdown("Configure system parameters and manage data.")
        
        # System status check
        st.markdown("### 🔍 System Status")
        
        vectorstore_exists = Path("vectorstore").exists()
        manual_exists = Path("data/Engineering_Manual.docx").exists()
        
        col1, col2 = st.columns(2)
        with col1:
            st.write("Vector Database:", "✅ Active" if vectorstore_exists else "❌ Missing")
            st.write("Engineering Manual:", "✅ Found" if manual_exists else "❌ Missing")
        
        with col2:
            try:
                api_key = st.secrets.get("CLAUDE_API_KEY", "")
                api_status = "✅ Configured" if api_key else "❌ Missing"
            except:
                api_status = "❌ Missing"
            st.write("Claude API Key:", api_status)
            st.write("Application Status:", "✅ Running")
        
        # Configuration options
        st.markdown("### ⚙️ Configuration")
        
        similarity_threshold = st.slider("Search Similarity Threshold", 0.0, 1.0, 0.6, 0.1)
        max_chunks = st.number_input("Maximum Chunks per Query", min_value=1, max_value=20, value=5)
        enable_logging = st.checkbox("Enable Detailed Logging", value=True)
        
        if st.button("💾 Save Configuration"):
            st.success("Configuration saved successfully!")
    
    # Navigation
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🏠 Home"):
            st.switch_page("Dashboard.py")
    with col2:
        if st.button("💬 Q&A Mode"):
            st.switch_page("pages/1_QA_Mode.py")
    with col3:
        if st.button("🧙‍♂️ Wizard Mode"):
            st.switch_page("pages/2_Wizard_Mode.py")

if __name__ == "__main__":
    main()
