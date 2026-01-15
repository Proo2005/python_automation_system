import sys
import os

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import config
from src.gmail_service import get_gmail_service
from src.sheets_service import get_sheets_service
from src.email_parser import parse_email

def main():
    # 1. Authenticate
    print("Authenticating...")
    gmail = get_gmail_service()
    sheets = get_sheets_service()

    if not gmail or not sheets:
        print("Failed to connect to APIs.")
        return

    # 2. Fetch Unread Emails
    print("Checking for unread emails...")
    results = gmail.users().messages().list(userId='me', q='is:unread').execute()
    messages = results.get('messages', [])

    if not messages:
        print("No new emails found.")
        return

    print(f"Found {len(messages)} new emails. Processing...")

    new_rows = []
    
    # 3. Process Each Email
    for msg in messages:
        # Fetch full details
        msg_detail = gmail.users().messages().get(userId='me', id=msg['id']).execute()
        
        # Parse content
        email_data = parse_email(msg_detail)
        print(f"Processing: {email_data['subject']}")

        # Prepare row for Sheets [From, Subject, Date, Content]
        row = [
            email_data['from'],
            email_data['subject'],
            email_data['date'],
            email_data['content']
        ]
        new_rows.append(row)

        # 4. Mark as Read (Modify Labels)
        # This acts as our state management. Once read, we won't fetch it again.
        gmail.users().messages().batchModify(
            userId='me',
            body={
                'ids': [msg['id']],
                'removeLabelIds': ['UNREAD']
            }
        ).execute()

    # 5. Append to Google Sheets
    if new_rows:
        body = {
            'values': new_rows
        }
        result = sheets.spreadsheets().values().append(
            spreadsheetId=config.SPREADSHEET_ID,
            range="Sheet1!A1", # Appends to the bottom of the table automatically
            valueInputOption="USER_ENTERED",
            body=body
        ).execute()
        print(f"{result.get('updates').get('updatedCells')} cells appended.")

if __name__ == '__main__':
    main()