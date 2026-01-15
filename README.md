# Gmail to Sheets Automation

## 📌 Project Overview
This project is a Python-based automation tool that connects to the **Gmail API** and **Google Sheets API**. It fetches real-time unread emails from a user's inbox, parses the relevant data (Sender, Subject, Date, Content), and logs them into a Google Sheet.

## Sample Image
[Sample](./sample%20image//i1.png)
[Sample](./sample%20image//i2.png)


## 🏗 Architecture
[Gmail Server]  <-- (OAuth 2.0) -->  [Python Script]  <-- (OAuth 2.0) -->  [Google Sheets]
       |                                     |                                     |
   (1. Fetch Unread)                   (2. Parse Data)                     (3. Append Row)
       |                                     |
   (4. Mark as Read) ------------------------+

**Flow:**
1. **Auth:** Script authenticates using OAuth 2.0 (User Credentials).
2. **Fetch:** Requests only messages with label `UNREAD`.
3. **Parse:** Decodes email body and extracts headers.
4. **Store:** Appends data to Google Sheets.
5. **Update State:** Marks email as `READ` in Gmail to prevent duplicate processing in future runs.

## ⚙️ Setup Instructions

### Prerequisites
* Python 3.x
* Google Cloud Console Project with Gmail & Sheets APIs enabled.
* `credentials.json` (OAuth Client ID).

### Installation
1.  **Clone the repository:**
    ```bash
    git clone <your-repo-link>
    cd gmail-to-sheets
    ```

2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure Credentials:**
    * Place your `credentials.json` file inside the `credentials/` folder.
    * *Note: This file is not included in the repo for security.*

4.  **Update Configuration:**
    * Open `config.py`.
    * Add your `SPREADSHEET_ID`.

### Usage
Run the main script:
```bash
python src/main.py