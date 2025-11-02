from google.oauth2 import service_account

try:
    creds = service_account.Credentials.from_service_account_file('credentials.json')
    print("✅ Valid Service Account")
    print("Client Email:", creds.service_account_email)
except Exception as e:
    print("❌ Error:", e)
