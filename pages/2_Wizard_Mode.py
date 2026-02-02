"""
==============================================================================
WIZARD MODE - Interactive Plan Review Checklist
==============================================================================
File: pages/2_Wizard_Mode.py
Purpose: Guide reviewers through plan review with interactive checklists
         and automatic comment generation.

Features:
- Review type selection (Transitional, HP, Standard, Pool, Fence)
- Interactive Yes/No/N/A checklist
- Automatic comment suggestions when "No" is selected
- Custom notes support
- Word document export with full checklist and comments

Update Log:
- 2026-02-02: Added explicit text colors and !important to all CSS classes
              to fix invisible text when browser is in dark mode.
- 2026-02-02: Added custom sidebar navigation to replace default "app" label.
==============================================================================
"""

import streamlit as st
import sys
from pathlib import Path
from datetime import datetime
from io import BytesIO

# Add utils to path
sys.path.append(str(Path(__file__).parent.parent / "utils"))

from checklist_data import (
    REVIEW_TYPES, 
    REVIEWERS, 
    CHECKLIST_SECTIONS,
    get_checklist_for_review_type
)
from comments_database import COMMENTS, get_comment

# Import python-docx for Word export
try:
    from docx import Document
    from docx.shared import Inches, Pt, RGBColor
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.enum.style import WD_STYLE_TYPE
    DOCX_AVAILABLE = True
except ImportError:
    DOCX_AVAILABLE = False

st.set_page_config(page_title="Wizard Mode", page_icon="📋", layout="wide")

# =============================================================================
# CUSTOM CSS - Dark Mode Safe
# =============================================================================
# Every class with a light background explicitly sets color: #1a1a2e (dark navy)
# with !important so Streamlit's dark theme cannot override text to white.
# =============================================================================
st.markdown("""
<style>
    /* Hide default streamlit page navigation */
    [data-testid="stSidebarNav"] {
        display: none;
    }
    .review-header {
        background: linear-gradient(135deg, #1e3a5f 0%, #2d5a87 100%) !important;
        color: white !important;
        padding: 1.5rem;
        border-radius: 10px;
        margin-bottom: 1rem;
    }
    .section-header {
        background: #f0f4f8 !important;
        color: #1a1a2e !important;
        padding: 0.75rem 1rem;
        border-left: 4px solid #1e3a5f;
        margin: 1rem 0 0.5rem 0;
        font-weight: bold;
    }
    .checklist-item {
        background: #ffffff !important;
        color: #1a1a2e !important;
        border: 1px solid #e0e0e0;
        border-radius: 5px;
        padding: 0.75rem;
        margin: 0.5rem 0;
    }
    .comment-box {
        background: #fff8e1 !important;
        color: #1a1a2e !important;
        border: 1px solid #ffd54f;
        border-radius: 5px;
        padding: 0.75rem;
        margin: 0.5rem 0 0.5rem 1rem;
        font-size: 0.9em;
    }
    .status-yes { color: #2e7d32 !important; font-weight: bold; }
    .status-no { color: #c62828 !important; font-weight: bold; }
    .status-na { color: #757575 !important; font-weight: bold; }
    .export-section {
        background: #e8f5e9 !important;
        color: #1a1a2e !important;
        border: 1px solid #a5d6a7;
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


def initialize_session_state():
    """Initialize session state variables"""
    if 'wizard_review_type' not in st.session_state:
        st.session_state.wizard_review_type = None
    if 'wizard_permit_number' not in st.session_state:
        st.session_state.wizard_permit_number = ""
    if 'wizard_address' not in st.session_state:
        st.session_state.wizard_address = ""
    if 'wizard_reviewer' not in st.session_state:
        st.session_state.wizard_reviewer = None
    if 'wizard_checklist_state' not in st.session_state:
        st.session_state.wizard_checklist_state = {}
    if 'wizard_selected_comments' not in st.session_state:
        st.session_state.wizard_selected_comments = {}
    if 'wizard_custom_notes' not in st.session_state:
        st.session_state.wizard_custom_notes = {}
    if 'wizard_started' not in st.session_state:
        st.session_state.wizard_started = False


def reset_checklist():
    """Reset checklist state when review type changes"""
    st.session_state.wizard_checklist_state = {}
    st.session_state.wizard_selected_comments = {}
    st.session_state.wizard_custom_notes = {}


def generate_word_document():
    """Generate a Word document with review comments"""
    if not DOCX_AVAILABLE:
        return None
    
    doc = Document()
    
    # =========================================================================
    # TITLE
    # =========================================================================
    title = doc.add_heading('Engineering Plan Review', 0)
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    
    # =========================================================================
    # PROJECT INFORMATION
    # =========================================================================
    doc.add_heading('Project Information', level=1)
    info_table = doc.add_table(rows=5, cols=2)
    info_table.style = 'Table Grid'
    
    info_data = [
        ('Review Type:', st.session_state.wizard_review_type or 'Not specified'),
        ('Permit Number:', st.session_state.wizard_permit_number or 'Not specified'),
        ('Address:', st.session_state.wizard_address or 'Not specified'),
        ('Reviewer:', st.session_state.wizard_reviewer or 'Not specified'),
        ('Review Date:', datetime.now().strftime('%Y-%m-%d %H:%M')),
    ]
    
    for i, (label, value) in enumerate(info_data):
        info_table.rows[i].cells[0].text = label
        info_table.rows[i].cells[1].text = value
        # Bold the labels
        info_table.rows[i].cells[0].paragraphs[0].runs[0].bold = True
    
    doc.add_paragraph()
    
    # =========================================================================
    # SUMMARY STATISTICS
    # =========================================================================
    doc.add_heading('Review Summary', level=1)
    
    yes_count = sum(1 for v in st.session_state.wizard_checklist_state.values() if v == "Yes")
    no_count = sum(1 for v in st.session_state.wizard_checklist_state.values() if v == "No")
    na_count = sum(1 for v in st.session_state.wizard_checklist_state.values() if v == "N/A")
    total = yes_count + no_count + na_count
    
    summary_table = doc.add_table(rows=4, cols=2)
    summary_table.style = 'Table Grid'
    summary_data = [
        ('Total Items Reviewed:', str(total)),
        ('Compliant (Yes):', str(yes_count)),
        ('Issues Found (No):', str(no_count)),
        ('Not Applicable:', str(na_count)),
    ]
    for i, (label, value) in enumerate(summary_data):
        summary_table.rows[i].cells[0].text = label
        summary_table.rows[i].cells[1].text = value
    
    doc.add_paragraph()
    
    # =========================================================================
    # FULL CHECKLIST WITH STATUS AND COMMENTS
    # =========================================================================
    doc.add_heading('Plan Review Checklist', level=1)
    
    # Get the checklist for the current review type
    checklist = get_checklist_for_review_type(st.session_state.wizard_review_type)
    
    for section_id, section_data in checklist.items():
        # Section header
        section_heading = doc.add_heading(section_data["name"], level=2)
        
        for item in section_data["items"]:
            item_key = item["id"]
            status = st.session_state.wizard_checklist_state.get(item_key, "Not Reviewed")
            
            # Create paragraph for checklist item
            para = doc.add_paragraph()
            
            # Add item ID and description
            item_run = para.add_run(f"{item['id']} - {item['description']}")
            item_run.bold = False
            
            # Add status on new line with color/bold
            para.add_run("\n")
            status_run = para.add_run(f"Status: {status}")
            status_run.bold = True
            
            # Color code the status
            if status == "Yes":
                status_run.font.color.rgb = RGBColor(0, 128, 0)  # Green
            elif status == "No":
                status_run.font.color.rgb = RGBColor(200, 0, 0)  # Red
            elif status == "N/A":
                status_run.font.color.rgb = RGBColor(128, 128, 128)  # Gray
            else:
                status_run.font.color.rgb = RGBColor(255, 165, 0)  # Orange for not reviewed
            
            # If "No", show comments
            if status == "No":
                selected = st.session_state.wizard_selected_comments.get(item_key, [])
                custom_note = st.session_state.wizard_custom_notes.get(item_key, "")
                
                if selected or custom_note.strip():
                    para.add_run("\n")
                    comments_label = para.add_run("Comments:")
                    comments_label.bold = True
                    comments_label.font.color.rgb = RGBColor(0, 0, 128)  # Dark blue
                    
                    # Add each selected comment
                    for comment_id in selected:
                        comment_text = COMMENTS.get(comment_id, "")
                        if comment_text:
                            comment_para = doc.add_paragraph()
                            comment_para.paragraph_format.left_indent = Inches(0.5)
                            comment_run = comment_para.add_run(f"• [{comment_id}] {comment_text}")
                            comment_run.font.size = Pt(10)
                    
                    # Add custom note if provided
                    if custom_note.strip():
                        custom_para = doc.add_paragraph()
                        custom_para.paragraph_format.left_indent = Inches(0.5)
                        custom_run = custom_para.add_run(f"• [CUSTOM] {custom_note}")
                        custom_run.font.size = Pt(10)
                        custom_run.italic = True
        
        # Add space after each section
        doc.add_paragraph()
    
    # =========================================================================
    # COMMENTS FOR COPY/PASTE (Only "No" items)
    # =========================================================================
    doc.add_page_break()
    doc.add_heading('Comments for Copy/Paste', level=1)
    
    intro_para = doc.add_paragraph()
    intro_para.add_run("Use the comments below for Bluebeam or permit system. ").italic = True
    intro_para.add_run("Only items marked 'No' with selected comments are included.").italic = True
    doc.add_paragraph()
    
    # Collect all comments in order
    all_comments = []
    
    for section_id, section_data in checklist.items():
        for item in section_data["items"]:
            item_key = item["id"]
            if st.session_state.wizard_checklist_state.get(item_key) == "No":
                selected = st.session_state.wizard_selected_comments.get(item_key, [])
                custom_note = st.session_state.wizard_custom_notes.get(item_key, "")
                
                for comment_id in selected:
                    comment_text = COMMENTS.get(comment_id, "")
                    if comment_text:
                        all_comments.append(comment_text)
                
                if custom_note.strip():
                    all_comments.append(custom_note)
    
    if all_comments:
        for i, comment in enumerate(all_comments, 1):
            para = doc.add_paragraph()
            num_run = para.add_run(f"{i}. ")
            num_run.bold = True
            para.add_run(comment)
            doc.add_paragraph()  # Space between comments
    else:
        doc.add_paragraph("No comments to include - all items are compliant or N/A.")
    
    # Save to BytesIO
    buffer = BytesIO()
    doc.save(buffer)
    buffer.seek(0)
    return buffer


def main():
    """Main function for Wizard Mode"""
    initialize_session_state()
    
    st.title("📋 Engineering Review Wizard")
    st.markdown("Interactive checklist for plan reviews with automatic comment generation.")
    
    # =========================================================================
    # STEP 1: PROJECT SETUP
    # =========================================================================
    st.markdown("---")
    st.subheader("📝 Step 1: Project Setup")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        review_type = st.selectbox(
            "Review Type",
            options=[""] + REVIEW_TYPES,
            index=0 if not st.session_state.wizard_review_type else REVIEW_TYPES.index(st.session_state.wizard_review_type) + 1,
            key="review_type_select"
        )
        
        # Check if review type changed
        if review_type and review_type != st.session_state.wizard_review_type:
            st.session_state.wizard_review_type = review_type
            reset_checklist()
            st.rerun()
        elif review_type:
            st.session_state.wizard_review_type = review_type
    
    with col2:
        permit_number = st.text_input(
            "Permit Number",
            value=st.session_state.wizard_permit_number,
            placeholder="e.g., SW2024-001"
        )
        st.session_state.wizard_permit_number = permit_number
    
    with col3:
        address = st.text_input(
            "Address",
            value=st.session_state.wizard_address,
            placeholder="e.g., 1808 Sonoma Trce"
        )
        st.session_state.wizard_address = address
    
    with col4:
        reviewer = st.selectbox(
            "Reviewer",
            options=[""] + REVIEWERS,
            index=0 if not st.session_state.wizard_reviewer else REVIEWERS.index(st.session_state.wizard_reviewer) + 1
        )
        st.session_state.wizard_reviewer = reviewer if reviewer else None
    
    # Check if we can proceed
    if not st.session_state.wizard_review_type:
        st.info("👆 Select a review type to begin.")
        return
    
    # =========================================================================
    # STEP 2: INTERACTIVE CHECKLIST
    # =========================================================================
    st.markdown("---")
    st.subheader(f"📋 Step 2: {st.session_state.wizard_review_type} Checklist")
    
    # Get applicable checklist
    checklist = get_checklist_for_review_type(st.session_state.wizard_review_type)
    
    # Calculate progress
    total_items = sum(len(section["items"]) for section in checklist.values())
    completed_items = len(st.session_state.wizard_checklist_state)
    
    st.progress(completed_items / total_items if total_items > 0 else 0)
    st.caption(f"Progress: {completed_items} of {total_items} items reviewed")
    
    # Display checklist by section
    for section_id, section_data in checklist.items():
        st.markdown(f'<div class="section-header">{section_data["name"]}</div>', unsafe_allow_html=True)
        
        for item in section_data["items"]:
            item_key = item["id"]
            
            # Create columns for item layout
            col1, col2 = st.columns([3, 1])
            
            with col1:
                st.markdown(f"**{item['id']}** - {item['description']}")
            
            with col2:
                # Status dropdown
                current_status = st.session_state.wizard_checklist_state.get(item_key, "")
                status_options = ["", "Yes", "No", "N/A"]
                
                status = st.selectbox(
                    "Status",
                    options=status_options,
                    index=status_options.index(current_status) if current_status in status_options else 0,
                    key=f"status_{item_key}",
                    label_visibility="collapsed"
                )
                
                if status:
                    st.session_state.wizard_checklist_state[item_key] = status
                elif item_key in st.session_state.wizard_checklist_state:
                    del st.session_state.wizard_checklist_state[item_key]
            
            # If "No" is selected, show comment options
            if st.session_state.wizard_checklist_state.get(item_key) == "No":
                with st.container():
                    st.markdown('<div class="comment-box">', unsafe_allow_html=True)
                    st.markdown("**📝 Select applicable comments:**")
                    
                    # Get available comments for this item
                    comment_ids = item.get("comment_ids", [])
                    
                    if comment_ids:
                        # Initialize selected comments if not exists
                        if item_key not in st.session_state.wizard_selected_comments:
                            st.session_state.wizard_selected_comments[item_key] = []
                        
                        # Show each comment with checkbox
                        for comment_id in comment_ids:
                            comment_text = COMMENTS.get(comment_id, "Comment not found")
                            
                            # Truncate long comments for display
                            display_text = comment_text[:150] + "..." if len(comment_text) > 150 else comment_text
                            
                            is_selected = comment_id in st.session_state.wizard_selected_comments[item_key]
                            
                            if st.checkbox(
                                f"**{comment_id}**: {display_text}",
                                value=is_selected,
                                key=f"comment_{item_key}_{comment_id}"
                            ):
                                if comment_id not in st.session_state.wizard_selected_comments[item_key]:
                                    st.session_state.wizard_selected_comments[item_key].append(comment_id)
                            else:
                                if comment_id in st.session_state.wizard_selected_comments[item_key]:
                                    st.session_state.wizard_selected_comments[item_key].remove(comment_id)
                            
                            # Show full comment in expander if long
                            if len(comment_text) > 150:
                                with st.expander("View full comment"):
                                    st.write(comment_text)
                    
                    # Custom notes field
                    st.markdown("**✏️ Custom notes (optional):**")
                    custom_note = st.text_area(
                        "Custom note",
                        value=st.session_state.wizard_custom_notes.get(item_key, ""),
                        key=f"custom_{item_key}",
                        height=80,
                        label_visibility="collapsed",
                        placeholder="Add any additional comments specific to this review..."
                    )
                    st.session_state.wizard_custom_notes[item_key] = custom_note
                    
                    st.markdown('</div>', unsafe_allow_html=True)
            
            st.markdown("---")
    
    # =========================================================================
    # STEP 3: REVIEW SUMMARY & EXPORT
    # =========================================================================
    st.markdown("---")
    st.subheader("📊 Step 3: Review Summary & Export")
    
    # Summary statistics
    yes_count = sum(1 for v in st.session_state.wizard_checklist_state.values() if v == "Yes")
    no_count = sum(1 for v in st.session_state.wizard_checklist_state.values() if v == "No")
    na_count = sum(1 for v in st.session_state.wizard_checklist_state.values() if v == "N/A")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("✅ Compliant", yes_count)
    with col2:
        st.metric("❌ Issues Found", no_count)
    with col3:
        st.metric("➖ N/A", na_count)
    with col4:
        st.metric("📝 Total Reviewed", yes_count + no_count + na_count)
    
    # Export section
    st.markdown('<div class="export-section">', unsafe_allow_html=True)
    st.markdown("### 📤 Export Review")
    
    if no_count == 0 and (yes_count + na_count) > 0:
        st.success("✅ No issues found! All reviewed items are compliant.")
    elif no_count > 0:
        st.warning(f"⚠️ {no_count} issue(s) found that require comments.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if DOCX_AVAILABLE:
            if st.button("📄 Generate Word Document", type="primary", use_container_width=True):
                if not st.session_state.wizard_permit_number:
                    st.error("Please enter a permit number before exporting.")
                elif completed_items == 0:
                    st.error("Please review at least one item before exporting.")
                else:
                    doc_buffer = generate_word_document()
                    if doc_buffer:
                        filename = f"Review_{st.session_state.wizard_permit_number}_{datetime.now().strftime('%Y%m%d')}.docx"
                        st.download_button(
                            label="⬇️ Download Word Document",
                            data=doc_buffer,
                            file_name=filename,
                            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                            use_container_width=True
                        )
        else:
            st.warning("python-docx not available. Install it to enable Word export.")
    
    with col2:
        if st.button("🗑️ Clear Review", use_container_width=True):
            reset_checklist()
            st.session_state.wizard_permit_number = ""
            st.session_state.wizard_address = ""
            st.session_state.wizard_reviewer = None
            st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Quick copy section for comments
    if no_count > 0:
        st.markdown("---")
        st.subheader("📋 Quick Copy - All Comments")
        st.caption("Copy these comments directly into Bluebeam or your permit system:")
        
        all_comments = []
        for section_id, section_data in checklist.items():
            for item in section_data["items"]:
                item_key = item["id"]
                if st.session_state.wizard_checklist_state.get(item_key) == "No":
                    selected = st.session_state.wizard_selected_comments.get(item_key, [])
                    custom_note = st.session_state.wizard_custom_notes.get(item_key, "")
                    
                    for comment_id in selected:
                        comment_text = COMMENTS.get(comment_id, "")
                        if comment_text:
                            all_comments.append(f"[{comment_id}] {comment_text}")
                    
                    if custom_note.strip():
                        all_comments.append(f"[CUSTOM] {custom_note}")
        
        if all_comments:
            comments_text = "\n\n".join(f"{i+1}. {c}" for i, c in enumerate(all_comments))
            st.text_area(
                "All Comments",
                value=comments_text,
                height=300,
                label_visibility="collapsed"
            )
    
    # Navigation (Admin Panel removed - now 2 columns)
    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🏠 Home"):
            st.switch_page("app.py")
    with col2:
        if st.button("💬 Q&A Mode"):
            st.switch_page("pages/1_QA_Mode.py")


if __name__ == "__main__":
    main()
