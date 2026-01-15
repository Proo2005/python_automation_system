import os

# Scopes required for the project
# We need 'modify' to mark emails as read after processing [cite: 32]
SCOPES = [
    'https://www.googleapis.com/auth/gmail.modify',
    'https://www.googleapis.com/auth/spreadsheets'
]

# File paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CREDENTIALS_FILE = os.path.join(BASE_DIR, 'credentials', 'credentials.json')
TOKEN_FILE = os.path.join(BASE_DIR, 'credentials', 'token.json')

# Google Sheet Configuration
# Create a new Google Sheet in your browser and copy the ID from the URL


SPREADSHEET_ID = '16FVkvOM4Zl66EUut7WEGoz0VCpKp9aWEnI7CJHW-N5w' 
RANGE_NAME = 'Sheet1!A1'