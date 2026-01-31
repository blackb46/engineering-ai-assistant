"""
==============================================================================
GOOGLE SHEETS UTILITY - Flagged Response Logging
==============================================================================
File: utils/google_sheets.py
Purpose: Send flagged Q&A responses to a Google Sheet for admin review

This connects to your Google Sheet and appends new rows when users
flag responses as needing improvement.
==============================================================================
"""

import streamlit as st
from datetime import datetime

# Google Sheets libraries
import gspread
from google.oauth2.service_account import Credentials


def get_google_sheet():
    """
    Connect to the Google Sheet using service account credentials.
    
    Returns:
        gspread.Worksheet: The first worksheet in your Google Sheet
        None: If connection fails
    """
    try:
        # Define the scope (permissions) we need
        scopes = [
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive"
        ]
        
        # Get credentials from Streamlit secrets
        credentials = Credentials.from_service_account_info(
            st.secrets["gcp_service_account"],
            scopes=scopes
        )
        
        # Connect to Google Sheets
        client = gspread.authorize(credentials)
        
        # Open the spreadsheet by ID
        sheet_id = st.secrets["GOOGLE_SHEET_ID"]
        spreadsheet = client.open_by_key(sheet_id)
        
        # Get the first worksheet
        worksheet = spreadsheet.sheet1
        
        return worksheet
    
    except Exception as e:
        print(f"Error connecting to Google Sheet: {e}")
        return None


def log_flagged_response(question, ai_response, user_feedback=""):
    """
    Log a flagged response to the Google Sheet.
    
    Args:
        question (str): The question the user asked
        ai_response (str): The AI's response that was flagged
        user_feedback (str): Optional feedback explaining what was wrong
    
    Returns:
        bool: True if successful, False if failed
    """
    try:
        # Get the worksheet
        worksheet = get_google_sheet()
        
        if worksheet is None:
            print("Could not connect to Google Sheet")
            return False
        
        # Prepare the row data
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Truncate long responses to avoid issues
        # Google Sheets cells have a 50,000 character limit
        max_length = 5000
        ai_response_truncated = ai_response[:max_length] if ai_response else ""
        if len(ai_response) > max_length:
            ai_response_truncated += "... [truncated]"
        
        # Create the row
        # Columns: Timestamp | Question | AI Response | User Feedback | Status
        new_row = [
            timestamp,
            question,
            ai_response_truncated,
            user_feedback if user_feedback else "(No feedback provided)",
            "Open"  # Default status
        ]
        
        # Append the row to the sheet
        worksheet.append_row(new_row, value_input_option="USER_ENTERED")
        
        print(f"✅ Flagged response logged to Google Sheet at {timestamp}")
        return True
    
    except Exception as e:
        print(f"Error logging to Google Sheet: {e}")
        return False


def test_connection():
    """
    Test the Google Sheets connection.
    
    Returns:
        tuple: (success: bool, message: str)
    """
    try:
        worksheet = get_google_sheet()
        
        if worksheet is None:
            return False, "Could not connect to Google Sheet"
        
        # Try to read the header row
        headers = worksheet.row_values(1)
        
        if headers:
            return True, f"Connected successfully! Headers: {headers}"
        else:
            return True, "Connected but sheet appears empty. Add headers: Timestamp, Question, AI Response, User Feedback, Status"
    
    except Exception as e:
        return False, f"Connection error: {str(e)}"
