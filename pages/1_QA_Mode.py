import streamlit as st
import sys
from pathlib import Path

# Add utils to path so Python can find our helper files
sys.path.append(str(Path(__file__).parent.parent / "utils"))

from rag_engine import RAGEngine
from database import AuditLogger

st.set_page_config(page_title="Q&A Mode", page_icon="💬", layout="wide")

# Hide default navigation and add custom styling
st.markdown("""
<style>
    /* Hide default streamlit page navigation */
    [data-testid="stSidebarNav"] {
        display: none;
    }
    
    .answer-box {
        background: linear-gradient(135deg, #e8f4f8 0%, #d1ecf1 100%);
        border: 2px solid #17a2b8;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
    }
    .answer-label {
        color: #0c5460;
        font-size: 0.9rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 0.5rem;
    }
    .answer-text {
        color: #0c5460;
        font-size: 1.2rem;
        font-weight: 700;
        line-height: 1.5;
    }
    .details-box {
        background: #f8f9fa;
        border: 1px solid #dee2e6;
        border-left: 4px solid #6c757d;
        border-radius: 8px;
        padding: 1.2rem;
        margin: 1rem 0;
    }
    .details-label {
        color: #495057;
        font-size: 0.85rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 0.75rem;
    }
    .details-text {
        color: #212529;
        font-size: 1rem;
        line-height: 1.6;
    }
    .code-ref {
        background: #fff3cd;
        border: 1px solid #ffc107;
        border-radius: 5px;
        padding: 0.5rem 1rem;
        margin-top: 1rem;
        font-size: 0.9rem;
        color: #856404;
    }
    .source-box {
        background: #fffbeb;
        border: 1px solid #fde68a;
        border-radius: 8px;
        padding: 0.75rem;
        margin: 0.5rem 0;
        font-size: 0.9em;
    }
</style>
""", unsafe_allow_html=True)

# Custom Sidebar Navigation
st.sidebar.title("🏗️ Navigation")
st.sidebar.markdown("---")
st.sidebar.page_link("app.py", label="🏠 Dashboard")
st.sidebar.page_link("pages/1_QA_Mode.py", label="💬 Q&A Mode")
st.sidebar.page_link("pages/2_Wizard_Mode.py", label="🧙‍♂️ Wizard Mode")
st.sidebar.page_link("pages/3_Admin.py", label="⚙️ Admin Panel")
st.sidebar.markdown("---")


def parse_response(response_text):
    """Parse the structured response into components"""
    result = {
        'answer': '',
        'details': '',
        'code_reference': '',
        'sources': ''
    }
    
    text = response_text.strip()
    
    if 'ANSWER:' in text:
        answer_start = text.find('ANSWER:') + len('ANSWER:')
        answer_end = text.find('DETAILS:') if 'DETAILS:' in text else len(text)
        result['answer'] = text[answer_start:answer_end].strip()
    
    if 'DETAILS:' in text:
        details_start = text.find('DETAILS:') + len('DETAILS:')
        details_end = text.find('CODE REFERENCE:') if 'CODE REFERENCE:' in text else text.find('SOURCES:') if 'SOURCES:' in text else len(text)
        result['details'] = text[details_start:details_end].strip()
    
    if 'CODE REFERENCE:' in text:
        code_start = text.find('CODE REFERENCE:') + len('CODE REFERENCE:')
        code_end = text.find('SOURCES:') if 'SOURCES:' in text else len(text)
        result['code_reference'] = text[code_start:code_end].strip()
    
    if 'SOURCES:' in text:
        sources_start = text.find('SOURCES:') + len('SOURCES:')
        result['sources'] = text[sources_start:].strip()
    
    return result


def display_formatted_answer(response_text):
    """Display the answer in a nicely formatted way"""
    parsed = parse_response(response_text)
    
    if parsed['answer']:
        st.markdown(f"""
        <div class="answer-box">
            <div class="answer-label">📋 Answer</div>
            <div class="answer-text">{parsed['answer']}</div>
        </div>
        """, unsafe_allow_html=True)
    
    if parsed['details'] or parsed['code_reference']:
        details_html = ""
        if parsed['details']:
            details_lines = parsed['details'].split('\n')
            details_formatted = ""
            for line in details_lines:
                line = line.strip()
                if line.startswith('- ') or line.startswith('* '):
                    details_formatted += f"<li>{line[2:]}</li>"
                elif line:
                    details_formatted += f"<li>{line}</li>"
            if details_formatted:
                details_html = f"<ul style='margin: 0; padding-left: 1.5rem;'>{details_formatted}</ul>"
        
        code_ref_html = ""
        if parsed['code_reference'] and parsed['code_reference'].lower() not in ['n/a', 'see sources below', '']:
            code_ref_html = f"""<div class="code-ref"><strong>📖 Code Reference:</strong> {parsed['code_reference']}</div>"""
        
        st.markdown(f"""
        <div class="details-box">
            <div class="details-label">📝 Supporting Details</div>
            <div class="details-text">{details_html}</div>
            {code_ref_html}
        </div>
        """, unsafe_allow_html=True)


def main():
    """Main function for the Q&A Mode page"""
    st.title("💬 Engineering Q&A Mode")
    st.markdown("Ask questions about engineering policies and get accurate, cited answers.")
    
    if 'rag_engine' not in st.session_state:
        st.session_state.rag_engine = RAGEngine()
    
    if 'audit_logger' not in st.session_state:
        st.session_state.audit_logger = AuditLogger()
    
    if not st.session_state.rag_engine.is_ready():
        st.error("❌ System not ready. Please check configuration.")
        return
    
    st.success("✅ Q&A system is ready!")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("❓ Ask Your Question")
        question = st.text_area(
            "Enter your engineering policy question:",
            height=100,
            placeholder="e.g., What are the maximum slopes for driveways?"
        )
        
        col1a, col1b = st.columns([1, 1])
        with col1a:
            ask_button = st.button("🔍 Get Answer", type="primary")
        with col1b:
            clear_button = st.button("🗑️ Clear")
        
        if clear_button:
            st.rerun()
        
        if ask_button and question.strip():
            with st.spinner("Searching through engineering manual..."):
                try:
                    result = st.session_state.rag_engine.query(question)
                    
                    st.session_state.audit_logger.log_query(
                        question=question,
                        answer=result.get('answer', ''),
                        sources=result.get('sources', []),
                        chunks_used=result.get('chunks_used', 0),
                        model_used=result.get('model_used', 'unknown')
                    )
                    
                    if result.get('chunks_used', 0) > 0:
                        display_formatted_answer(result.get('answer', 'No answer generated'))
                    else:
                        st.warning(result.get('answer', 'No relevant information found.'))
                    
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
                    
                    st.markdown("### 📊 Query Statistics")
                    col1a, col1b = st.columns(2)
                    with col1a:
                        st.metric("Chunks Used", result.get('chunks_used', 0))
                    with col1b:
                        st.metric("Sources Found", len(result.get('sources', [])))
                    
                    st.markdown("### 📢 Feedback")
                    col1a, col1b = st.columns(2)
                    with col1a:
                        if st.button("👍 Helpful"):
                            st.session_state.audit_logger.flag_response(
                                question=question, flag_type="positive", reason="Helpful"
                            )
                            st.success("Thanks for your feedback!")
                    with col1b:
                        if st.button("👎 Needs Improvement"):
                            st.session_state.audit_logger.flag_response(
                                question=question, flag_type="negative", reason="Needs improvement"
                            )
                            st.warning("Feedback recorded.")
                    
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")
    
    with col2:
        st.subheader("💡 Usage Tips")
        st.markdown("""
        **Ask specific questions:**
        - "What are the setback requirements?"
        - "What is the maximum driveway grade?"
        - "When is an as-built survey required?"
        
        **The system will:**
        - Search the engineering manual
        - Provide cited answers
        - Show source locations
        - Abstain if no info found
        """)
        
        st.subheader("🔍 Recent Queries")
        try:
            recent = st.session_state.audit_logger.get_recent_queries(limit=5)
            if recent:
                for q in recent:
                    with st.expander(f"🔎 {q['question'][:40]}..."):
                        st.write(f"**Asked:** {q['timestamp']}")
            else:
                st.write("No recent queries.")
        except:
            st.write("Query history will appear here.")


if __name__ == "__main__":
    main()
