import sys
import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from config import GOOGLE_SHEETS_CREDENTIALS, GOOGLE_SHEET_NAME

# Ensure the app context is available
sys.path.append(os.getcwd())

if __name__ == "__main__":
    print('Testing Google Sheet Connection...')
    try:
        scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
                 "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name(GOOGLE_SHEETS_CREDENTIALS, scope)
        client = gspread.authorize(creds)
        
        sheet = client.open(GOOGLE_SHEET_NAME)
        worksheets = sheet.worksheets()
        print(f"✅ Available sheets in '{GOOGLE_SHEET_NAME}':")
        for ws in worksheets:
            print(f"  - {ws.title}")
            
    except Exception as e:
        print(f"Error: {e}")
