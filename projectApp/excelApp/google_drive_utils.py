import os
import pickle
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# The scope gives full Drive access
SCOPES = ["https://www.googleapis.com/auth/drive.file"]

# --- FIXED VERSION ---
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOKEN_PATH = os.path.join(BASE_DIR, "token.pickle")
CREDENTIALS_PATH = os.path.join(BASE_DIR, "credentials.json")

def get_drive_service():
    creds = None

    if os.path.exists(TOKEN_PATH):
        with open(TOKEN_PATH, "rb") as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_PATH, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(TOKEN_PATH, "wb") as token:
            pickle.dump(creds, token)

    service = build("drive", "v3", credentials=creds)
    return service


def upload_to_drive(file_path, folder_id=None):
    service = get_drive_service()
    file_metadata = {"name": os.path.basename(file_path)}
    if folder_id:
        file_metadata["parents"] = [folder_id]

    media = MediaFileUpload(file_path, resumable=True)
    file = service.files().create(
        body=file_metadata, media_body=media, fields="id"
    ).execute()
    print(f"✅ File uploaded to Drive, ID: {file.get('id')}")
