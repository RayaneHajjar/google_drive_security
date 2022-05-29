from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import ntpath

# Get The File Name From Path
def path_leaf(path):
  ntpath.basename("a/b/c")
  head, tail = ntpath.split(path)
  return tail or ntpath.basename(head)

# Init Google Drive
def googleDrive():
  gauth = GoogleAuth()
  # Creates local webserver and auto handles authentication
  gauth.LocalWebserverAuth()
  drive = GoogleDrive(gauth)
  return drive

# Upload File To Drive
def uploadFile(drive, file_location):
  file_name = path_leaf(file_location)
  file1 = drive.CreateFile({'title': file_name})
  file1.SetContentFile(file_location)
  file1.Upload()

# List All Files
def listFiles(drive):
  file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
  for file1 in file_list:
    print('title: %s, id: %s' % (file1['title'], file1['id']))

# Download File From Drive
def downloadFile(drive, file_id):
  file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
  for file1 in file_list:
    if file1['id'] == file_id:
      file1.GetContentFile(file1['title'])