# Simple Google Drive Upload

### Requirements:
- Platform: Linux/MacOSX
- Python 3.6 + virtualenv

### Prepare
- Create Service Account Credentials: Click [here](https://console.developers.google.com/apis/credentials) for detail!
- Get the email address of Service Account. Create a folder in your drive, then share permission for that email.

### Execute:

1. Copy content of Service Account JSON to `service_account.json`, which look similar like this:

```json
{
  "type": "service_account",
  "project_id": "example_project",
  "private_key_id": "...",
  "private_key": "-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n",
  "client_email": "example_project@example_project.iam.gserviceaccount.com",
  "client_id": "...",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/example_project%40example_project.iam.gserviceaccount.com"
}
```
2. Create file `my_account.json`:

```json
{
  "directory": "sharefolder"
}
```
3. Run this script:

```
./upload.sh <my_file>
```
