import base64

def get_header_value(headers, name):
    """Utility to extract header value by name (e.g., 'Subject')."""
    if not headers:
        return ""
    for header in headers:
        if header['name'].lower() == name.lower():
            return header['value']
    return "(No Subject)"

def clean_body(data):
    """Decodes base64url encoded string."""
    try:
        if not data:
            return ""
        # Add padding if necessary
        clean_data = data.replace("-", "+").replace("_", "/")
        padding = len(clean_data) % 4
        if padding != 0:
            clean_data += "=" * (4 - padding)
        return base64.b64decode(clean_data).decode('utf-8')
    except Exception as e:
        return "(Error decoding content)"

def parse_email(message):
    """
    Parses a raw Gmail API message object into a clean dictionary.
    """
    payload = message.get('payload', {})
    headers = payload.get('headers', [])
    
    # 1. Extract Headers
    sender = get_header_value(headers, 'From')
    subject = get_header_value(headers, 'Subject')
    date_str = get_header_value(headers, 'Date')
    
    # 2. Extract Body
    body = ""
    if 'parts' in payload:
        for part in payload['parts']:
            if part['mimeType'] == 'text/plain':
                body = part['body'].get('data', '')
                break
        # Fallback if no text/plain found
        if not body and payload['parts']:
             body = payload['parts'][0]['body'].get('data', '')
    else:
        body = payload.get('body', {}).get('data', '')

    clean_text = clean_body(body)

    # 3. Return Dictionary (KEYS MUST BE LOWERCASE)
    return {
        'from': sender,
        'subject': subject,
        'date': date_str,
        'content': clean_text[:500]
    }