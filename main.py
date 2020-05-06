from __future__ import print_function

import json
import os
import sys

from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

SCOPES = ['https://www.googleapis.com/auth/drive.appdata', 'https://www.googleapis.com/auth/drive.file',
          'https://www.googleapis.com/auth/drive.metadata.readonly']


def print_inline(text):
    sys.stdout.write('\r\033[K\r{}'.format(text)),
    sys.stdout.flush()


def upload(filepath):
    with open('my_account.json') as json_file:
        my_account = json.load(json_file)
        directory = my_account.get('directory')

    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    credentials = service_account.Credentials.from_service_account_file("service_account.json", scopes=SCOPES)
    # delegated_credentials = credentials.with_subject(mail)
    service = build('drive', 'v3', credentials=credentials)

    parent_id = None

    # Call the Drive v3 API
    next_page_token = None
    while parent_id is None:
        results = service.files().list(
            pageSize=10, fields="nextPageToken, files(id, name)",
            pageToken=next_page_token
        ).execute()
        next_page_token = results.get('nextPageToken')
        items = results.get('files', [])

        if not items or len(items) == 0:
            break
        for item in items:
            if item['name'] == directory:
                parent_id = item['id']
                break

    if parent_id is None:
        print("Directory %s not found!" % directory)
        return
    print("Found directory %s - Parent ID: %s" % (directory, parent_id))

    media = MediaFileUpload(filepath, chunksize=256 * 1024, resumable=True)
    filename = os.path.basename(filepath)
    file_metadata = {'name': filename, 'parents': [parent_id]}

    request = service.files().create(body=file_metadata,
                                     media_body=media,
                                     fields='id, owners')
    response = None
    while response is None:
        status, response = request.next_chunk()
        if status:
            print_inline("Uploaded %.2f%%" % (status.progress() * 100))
    print("Upload Complete!")
    print('File ID: %s - File Name: %s' % (response.get('id'), filename))


if __name__ == '__main__':
    upload(sys.argv[1])
