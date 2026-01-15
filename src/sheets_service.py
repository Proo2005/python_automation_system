import os.path
import sys
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import config

def get_sheets_service():
    creds = None
    if os.path.exists(config.TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(config.TOKEN_FILE, config.SCOPES)
    
    # We assume creds are valid because gmail_service.py just created them.
    # If they are expired, we refresh them.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            # Re-run flow if necessary (should be rare if token.json exists)
            flow = InstalledAppFlow.from_client_secrets_file(
                config.CREDENTIALS_FILE, config.SCOPES)
            creds = flow.run_local_server(port=0)
        
        with open(config.TOKEN_FILE, 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('sheets', 'v4', credentials=creds)
        return service
    except Exception as e:
        print(f"Error creating Sheets service: {e}")
        return None

if __name__ == '__main__':
    service = get_sheets_service()
    if service:
        # Quick test: Read the headers from your sheet
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=config.SPREADSHEET_ID,
                                    range=config.RANGE_NAME).execute()
        values = result.get('values', [])
        print("Connection Successful! Data found:", values)