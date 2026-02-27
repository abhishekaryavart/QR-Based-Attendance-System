from flask import Flask, render_template
from utils.google_sheet import get_attendance_data
import os
import json

app = Flask(__name__)

# Load configuration
app.config.from_object('config')

@app.route('/')
def dashboard():
    # Fetch RAW attendance data from Google Sheets
    attendance_data = get_attendance_data()

    # Pass the raw data directly to the template as JSON for frontend sorting/filtering
    attendance_data_json = json.dumps(attendance_data)

    return render_template('dashboard.html', 
                           attendance_data_json=attendance_data_json)

if __name__ == '__main__':
    app.run(debug=True)
