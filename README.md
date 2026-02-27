# QR Based Attendance System

A web-based dashboard built with Flask to visualize and manage student attendance data sourced directly from Google Sheets.

## Features

- **Google Sheets Integration**: Fetches real-time attendance data from a centralized Google Sheet.
- **Interactive Dashboard**: Displays dynamic charts and data tables using Chart.js on the frontend.
- **Advanced Filtering**: Filter attendance records by Class, Semester, and Date instantly on the client side without page reloads.

## Tech Stack

- **Backend**: Python, Flask
- **Data Source**: Google Sheets API (`gspread`, `oauth2client`)
- **Frontend**: HTML, CSS, JavaScript, Chart.js
- **Data Processing**: Pandas

## Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

- Python 3.7+
- A Google Cloud Project with the Google Drive API and Google Sheets API enabled.
- A Service Account with generated `credentials.json` file.
- A Google Sheet containing the attendance data.
- Git (for cloning the repository)

### Cloning the Repository

1. **Clone the repo from GitHub:**
   ```bash
   git clone https://github.com/your-username/your-repository-name.git
   ```

2. **Navigate to the project directory:**
   ```bash
   cd "your-repository-name/qr_attendance_system"
   ```

### Setup Instructions

1. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

2. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Google Sheets API:**
   - Place your Google Service Account credentials file in the root directory and name it `credentials.json` (or update `GOOGLE_SHEETS_CREDENTIALS` in `config.py` to point to it).
   - Share your Google Sheet with the `client_email` found inside your `credentials.json` file.
   - Update `GOOGLE_SHEET_NAME` in `config.py` to match the exact name of your Google Sheet.

4. **Run the application:**
   ```bash
   python app.py
   ```

5. **Access the Application:**
   Open your web browser and go to `http://127.0.0.1:5000/`.

## Folder Structure

A complete overview of the project directory and its structure:

```text
qr_attendance_system/
│
├── app.py                   # Main Flask application file containing the routing logic
├── config.py                # Configuration file for Google Sheets API and Flask settings
├── requirements.txt         # List of Python dependencies
├── credentials.json         # (Not in repo) Google Sheets API authentication credentials
├── attendance.xlsx          # Local backup/exported attendance data
├── error.log                # Application error logs
├── output.log               # Application output logs
│
├── static/                  # Static assets (CSS, JS, Images)
│   ├── css/                 # Stylesheets
│   └── js/                  # Client-side JavaScript logic
│
├── templates/               # HTML templates rendered by Flask
│   ├── base.html            # Base layout template
│   └── dashboard.html       # Analytics dashboard template
│
├── utils/                   # Utility modules
│   └── google_sheet.py      # Core logic to interact with Google Sheets API
│
└── venv/                    # Virtual environment (created during setup)
```

## Future Updates / Roadmap

We are continuously working to improve the system. Upcoming features include:

- **User Authentication**: Add secure login functionality for admins, teachers, and coordinators.
- **Export Functionality**: One-click feature to directly export visualized attendance reports to PDF or CSV from the dashboard.
- **Mobile App Integration**: Develop a dedicated mobile app for faster and more seamless QR scanning directly from smartphones.
- **Automated Email Notifications**: Background job to send daily or weekly attendance summaries automatically.
- **Student Portal**: A dedicated view for students to log in and check their individual attendance and shortfalls.

## License

Distributed under the MIT License. See `LICENSE` for more information.
