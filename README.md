# Engineering AI Assistant

A municipal engineering AI assistant that provides accurate, cited answers from policy documents and guides users through permit review workflows.

## 🎯 Purpose

This application helps municipal engineering staff and developers by:
- Answering policy questions with precise citations
- Guiding permit reviews through structured workflows  
- Maintaining audit logs for accountability
- Ensuring consistent application of engineering standards

## 🚀 Quick Start

### Prerequisites
- Python 3.10 or higher
- Claude API key from Anthropic
- Engineering manual in .docx format

### Installation

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure API key**
   Create `.streamlit/secrets.toml`:
   ```toml
   CLAUDE_API_KEY = "your-api-key-here"
   ```

3. **Add your data**
   - Place your `Engineering_Manual.docx` in the `data/` folder
   - Copy your vector database to `vectorstore/`

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

## 📁 Project Structure

```
├── app.py                 # Main entry point
├── pages/
│   ├── 1_QA_Mode.py      # Question answering interface
│   ├── 2_Wizard_Mode.py  # Guided workflows
│   └── 3_Admin.py        # Administrative dashboard
├── utils/
│   ├── rag_engine.py     # Question-answering logic
│   ├── wizard_engine.py  # Workflow management
│   └── database.py       # Audit logging
├── data/                 # Engineering manual storage
├── vectorstore/          # Search database
├── logs/                 # Activity logs
└── requirements.txt      # Python dependencies
```

## 🔧 Features

### Q&A Mode
- Semantic search through engineering manual
- Source citations for every answer  
- Confidence-based abstention when unsure
- User feedback and flagging system

### Wizard Mode
- Step-by-step permit review workflows
- Automated checklist generation
- Progress tracking and documentation

### Admin Panel
- Query audit logs and analytics
- Flagged response management
- System configuration options

## 📞 Support

For technical issues, check system status on the main page and verify all components are properly configured.

---

**Engineering AI Assistant v1.0**  
*Built with Streamlit and Claude API*  
*Municipal Engineering Department*
