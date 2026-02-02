"""
==============================================================================
UPDATED Q&A MODE - With Google Sheets Feedback System (FIXED)
==============================================================================
File: pages/1_QA_Mode.py
Purpose: Question answering with source citations and feedback popup

FIXED: Answer now stays visible when clicking feedback buttons

Update Log:
- 2026-02-02: Added explicit text colors with !important for dark mode fix.
- 2026-02-02: Added custom sidebar navigation to replace default "app" label.
==============================================================================
"""

import streamlit as st
import sys
from pathlib import Path

# Add utils to path so Python can find our helper files
sys.path.append(str(Path(__file__).parent.parent / "utils"))

from rag_engine import RAGEngine
from database import AuditLogger
from google_sheets import log_flagged_response

st.set_page_config(page_title="Q&A Mode", page_icon="💬", layout="wide")

# CSS styling for professional appearance
st.markdown("""
<style>
    /* Hide default streamlit page navigation */
    [data-testid="stSidebarNav"] {
        display: none;
    }
    .question-box {
        background: #f8f9fa !important;
        color: #1a1a2e !important;
        border: 1px solid #dee2e6;
        border-radius: 8px;
        padding: 1rem;
        margin: 1rem 0;
    }
    .answer-box {
        background: #e7f3ff !important;
        color: #1a1a2e !important;
        border: 1px solid #bee5eb;
        border-radius: 8px;
        padding: 1rem;
        margin: 1rem 0;
    }
    .source-box {
        background: #fff3cd !important;
        color: #1a1a2e !important;
        border: 1px solid #ffeaa7;
        border-radius: 8px;
        padding: 0.5rem;
        margin: 0.5rem 0;
        font-size: 0.9em;
    }
    .feedback-popup {
        background: #fff5f5 !important;
        color: #1a1a2e !important;
        border: 2px solid #fc8181;
        border-radius: 8px;
        padding: 1.5rem;
        margin: 1rem 0;
    }
    .success-message {
        background: #d4edda !important;
        color: #155724 !important;
        border: 1px solid #c3e6cb;
        border-radius: 8px;
        padding: 1rem;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Custom Sidebar Navigation (matches app.py)
st.sidebar.title("🧭 Navigation")
st.sidebar.markdown("---")
st.sidebar.page_link("app.py", label="🏡 Dashboard", icon=None)
st.sidebar.page_link("pages/1_QA_Mode.py", label="💬 Q&A Mode", icon=None)
st.sidebar.page_link("pages/2_Wizard_Mode.py", label="🧙‍♂️ Wizard Mode", icon=None)
st.sidebar.markdown("---")
st.sidebar.markdown("**Engineering AI Assistant**")
st.sidebar.markdown("v1.0 | Brentwood, TN")


def main():
    """Main function for the Q&A Mode page"""
    st.title("💬 Engineering Q&A Mode")
    st.markdown("Ask questions about engineering policies and get accurate, cited answers.")

    # Initialize components
    if 'rag_engine' not in st.session_state:
        st.session_state.rag_engine = RAGEngine()

    if 'audit_logger' not in st.session_state:
        st.session_state.audit_logger = AuditLogger()
    
    # Initialize session state for preserving results
    if 'current_result' not in st.session_state:
        st.session_state.current_result = None
    if 'current_question' not in st.session_state:
        st.session_state.current_question = ""
    if 'show_feedback_form' not in st.session_state:
        st.session_state.show_feedback_form = False
    if 'feedback_submitted' not in st.session_state:
        st.session_state.feedback_submitted = False

    # Check system readiness
    if not st.session_state.rag_engine.is_ready():
        st.error("❌ System not ready. Please check:")
        st.markdown("""
        - Vector database exists in `vectorstore/` folder
        - Claude API key is configured in secrets
        """)
        if st.button("🏠 Return to Home"):
            st.switch_page("app.py")
        return

    st.success("✅ Q&A system is ready!")

    # Main interface
    col1, col2 = st.columns([2, 1])

    with col1:
        # Question input
        st.subheader("❓ Ask Your Question")
        question = st.text_area(
            "Enter your engineering policy question:",
            height=100,
            placeholder="e.g., What are the minimum pipe sizes for drainage systems?",
            key="question_input"
        )

        col1a, col1b = st.columns([1, 1])
        with col1a:
            ask_button = st.button("🔍 Get Answer", type="primary")
        with col1b:
            if st.button("🗑️ Clear"):
                st.session_state.current_result = None
                st.session_state.current_question = ""
                st.session_state.show_feedback_form = False
                st.session_state.feedback_submitted = False
                st.rerun()

        # Process NEW question
        if ask_button and question.strip():
            # Reset feedback state for new question
            st.session_state.show_feedback_form = False
            st.session_state.feedback_submitted = False
            
            with st.spinner("Searching through engineering manual..."):
                try:
                    result = st.session_state.rag_engine.query(question)
                    
                    # Store in session state so it persists
                    st.session_state.current_result = result
                    st.session_state.current_question = question

                    # Log the query
                    st.session_state.audit_logger.log_query(
                        question=question,
                        answer=result.get('answer', ''),
                        sources=result.get('sources', []),
                        chunks_used=result.get('chunks_used', 0),
                        model_used=result.get('model_used', 'unknown')
                    )

                except Exception as e:
                    st.error(f"❌ Error processing question: {str(e)}")
                    st.session_state.current_result = None
        
        # =========================================================
        # DISPLAY RESULTS (from session state - persists on rerun)
        # =========================================================
        if st.session_state.current_result is not None:
            result = st.session_state.current_result
            
            # Show the question that was asked
            st.markdown("---")
            st.markdown(f"**Question:** {st.session_state.current_question}")
            
            # Display answer
            st.markdown("### 📝 Answer")
            st.markdown(f"""
            <div class="answer-box">
                {result.get('answer', 'No answer generated')}
            </div>
            """, unsafe_allow_html=True)

            # Display sources
            if result.get('sources'):
                st.markdown("### 📚 Sources")
                for i, source in enumerate(result['sources'], 1):
                    st.markdown(f"""
                    <div class="source-box">
                        <strong>Source {i}:</strong> {source.get('source_file', 'Unknown')}
                        (Chunk {source.get('chunk_id', 'N/A')})
                        <br><small>Similarity: {source.get('similarity', 0):.3f}</small>
                    </div>
                    """, unsafe_allow_html=True)

            # Performance metrics
            st.markdown("### 📊 Query Statistics")
            col1a, col1b, col1c = st.columns(3)
            with col1a:
                st.metric("Chunks Used", result.get('chunks_used', 0))
            with col1b:
                st.metric("Sources Found", len(result.get('sources', [])))
            with col1c:
                if 'token_usage' in result:
                    total_tokens = result['token_usage'].get('input_tokens', 0) + result['token_usage'].get('output_tokens', 0)
                    st.metric("Tokens Used", f"{total_tokens:,}")

            # =========================================================
            # FEEDBACK SECTION
            # =========================================================
            st.markdown("---")
            st.markdown("### 📢 Was this answer helpful?")
            
            # Only show buttons if feedback not yet submitted
            if not st.session_state.feedback_submitted:
                col_fb1, col_fb2 = st.columns(2)

                with col_fb1:
                    if st.button("👍 Yes, this helped!", use_container_width=True):
                        st.session_state.feedback_submitted = True
                        st.rerun()

                with col_fb2:
                    if st.button("👎 Needs Improvement", use_container_width=True, type="secondary"):
                        st.session_state.show_feedback_form = True
                        st.rerun()
            
            # =========================================================
            # FEEDBACK FORM (shown when user clicks Needs Improvement)
            # =========================================================
            if st.session_state.show_feedback_form and not st.session_state.feedback_submitted:
                st.markdown("""
                <div class="feedback-popup">
                    <h4>🚩 Report an Issue</h4>
                    <p>Help us improve! Tell us what was wrong with this response.</p>
                </div>
                """, unsafe_allow_html=True)
                
                # Feedback text input
                feedback_text = st.text_area(
                    "What was wrong with the response? (optional but helpful)",
                    placeholder="Examples:\n- The answer was incorrect because...\n- It was missing information about...\n- The cited section doesn't actually say that...",
                    height=120,
                    key="feedback_text_input"
                )
                
                col_submit1, col_submit2 = st.columns(2)
                
                with col_submit1:
                    if st.button("📤 Submit Feedback", type="primary", use_container_width=True):
                        # Send to Google Sheets
                        success = log_flagged_response(
                            question=st.session_state.current_question,
                            ai_response=result.get('answer', ''),
                            user_feedback=feedback_text
                        )
                        
                        if success:
                            st.session_state.feedback_submitted = True
                            st.session_state.show_feedback_form = False
                            st.rerun()
                        else:
                            st.error("❌ Could not submit feedback. Please try again.")
                
                with col_submit2:
                    if st.button("❌ Cancel", use_container_width=True):
                        st.session_state.show_feedback_form = False
                        st.rerun()
            
            # Show success message after feedback submitted
            if st.session_state.feedback_submitted:
                st.markdown("""
                <div class="success-message">
                    ✅ <strong>Thank you for your feedback!</strong><br>
                    Your report has been submitted for review.
                </div>
                """, unsafe_allow_html=True)

    with col2:
        # Usage tips
        st.subheader("💡 Usage Tips")
        st.markdown("""
        **Ask specific questions:**
        - "What are the setback requirements?"
        - "What is the max encroachment into PUDE?"
        - "What permits are needed for pools?"

        **The system will:**
        - Search the engineering manual
        - Provide cited answers
        - Show source locations
        - Abstain if no relevant info found

        **Report issues that are:**
        - Incorrect or misleading
        - Missing important details
        - Not relevant to your question
        """)

        # Recent queries (from session)
        st.subheader("🔍 Recent Queries")
        try:
            recent_queries = st.session_state.audit_logger.get_recent_queries(limit=5)

            if recent_queries:
                for query in recent_queries[:5]:
                    q_text = query.get('question', 'No question')
                    q_preview = q_text[:40] + "..." if len(q_text) > 40 else q_text
                    with st.expander(f"📝 {q_preview}"):
                        st.write(f"**Asked:** {query.get('timestamp', 'Unknown')[:19]}")
                        st.write(f"**Sources:** {query.get('sources_count', 0)}")
            else:
                st.write("No recent queries yet.")
        except:
            st.write("Query history will appear here.")

    # Navigation (Admin Panel removed - now 2 columns)
    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🏠 Home"):
            st.switch_page("app.py")
    with col2:
        if st.button("🧙‍♂️ Wizard Mode"):
            st.switch_page("pages/2_Wizard_Mode.py")


if __name__ == "__main__":
    main()
