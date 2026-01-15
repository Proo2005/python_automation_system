import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Scopes required for the project
# [cite_start]We need 'modify' to mark emails as read after processing [cite: 32]
SCOPES = [
    'https://www.googleapis.com/auth/gmail.modify',
    'https://www.googleapis.com/auth/spreadsheets'
]

# File paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CREDENTIALS_FILE = os.path.join(BASE_DIR, 'credentials', 'credentials.json')
TOKEN_FILE = os.path.join(BASE_DIR, 'credentials', 'token.json')

# Google Sheet Configuration
# Get the ID from the environment variable (returns None if not found)
SPREADSHEET_ID = os.getenv('SPREADSHEET_ID')
RANGE_NAME = 'Sheet1!A1'

# Safety check to ensure ID is loaded
if not SPREADSHEET_ID:
    raise ValueError("SPREADSHEET_ID not found in environment variables. Check your .env file.")