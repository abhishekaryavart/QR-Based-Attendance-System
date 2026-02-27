import gspread
from oauth2client.service_account import ServiceAccountCredentials
from config import GOOGLE_SHEETS_CREDENTIALS, GOOGLE_SHEET_NAME
import os
import traceback

def get_attendance_data():
    # Define the scope
    scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
             "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

    # Authenticate using credentials.json
    try:
        creds = ServiceAccountCredentials.from_json_keyfile_name(GOOGLE_SHEETS_CREDENTIALS, scope)
        client = gspread.authorize(creds)
        print("✅ Successfully authenticated with Google Service Account.")
    except Exception as e:
        print(f"❌ Authentication Error: {e}")
        traceback.print_exc()
        return []

    # Open the Google Sheet and specific worksheet
    try:
        # Get the first sheet by index (0) instead of hardcoding the name
        sheet = client.open(GOOGLE_SHEET_NAME).get_worksheet(0)
        print(f"✅ Successfully connected to Google Sheet: '{GOOGLE_SHEET_NAME}' (Tab: '{sheet.title}')")
    except Exception as e:
        print(f"❌ Error opening Google Sheet ({GOOGLE_SHEET_NAME}): {e}")
        traceback.print_exc()
        return []

    # Fetch all records
    try:
        records = sheet.get_all_records()
        print(f"✅ Successfully fetched {len(records)} records from the sheet.")
    except Exception as e:
        print(f"❌ Error fetching records from sheet: {e}")
        traceback.print_exc()
        return []

    # Transform data
    # Google Form columns: ['Timestamp', 'Email address', 'Student Name', 'Enroll Id', 'Class', 'Semester', 'Mobile No.', 'Date']
    attendance_data = []
    
    for row in records:
        name = str(row.get('Student Name', '')).strip()
        class_name = str(row.get('Class', '')).strip()
        enroll_id = str(row.get('Enroll Id', '')).strip()
        semester = str(row.get('Semester', '')).strip()
        date = str(row.get('Date', '')).strip()
        timestamp = str(row.get('Timestamp', '')).strip()
        
        # If no explicit Date column, try to parse it from the Timestamp
        if not date and timestamp:
            date = timestamp.split(' ')[0]
            
        if not name:
            continue
            
        attendance_data.append({
            'name': name,
            'class': class_name,
            'enroll_id': enroll_id,
            'semester': semester,
            'date': date,
            'timestamp': timestamp
        })

    print(f"✅ Fetched and parsed {len(attendance_data)} raw student attendance records.")
    return attendance_data
