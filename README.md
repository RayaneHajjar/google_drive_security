# google_drive_security  

**Objective**: To make secure file storage in cloud computing using hybrid cryptography.

# Features

* Secure file data in Google Drive.
* Key is sent directly to you email ID.
* Pure-Python

# Getting Started

To get started with the code on this repo, you need to either clone or download this repo into your machine.

# Dependencies

Before you begin playing with the source code you might need to install deps just as shown below;

`pip3 install -r requirements.txt`

# Authentication

Drive API requires OAuth2.0 for authentication. PyDrive makes your life much easier by handling complex authentication steps for you.  
1. Go to APIs Console and make your own project.  
2. Search for ‘Google Drive API’, select the entry, and click ‘Enable’.  
3. Select ‘Credentials’ from the left menu, click ‘Create Credentials’, select ‘OAuth client ID’.  
4. Now, the product name and consent screen need to be set -> click ‘Configure consent screen’ and follow the instructions. Once finished:  
    a. Select ‘Application type’ to be Web application.  
    b. Enter an appropriate name.  
    c. Input http://localhost:8080 for ‘Authorized JavaScript origins’.  
    d. Input http://localhost:8080/ for ‘Authorized redirect URIs’.
    e. Click ‘Save’.
5. Click ‘Download JSON’ on the right side of Client ID to download client_secret_<really long ID>.json.  
The downloaded file has all authentication information of your application. Rename the file to “client_secrets.json” and place it in your working directory.

# Setting up Gmail account

The decryption phase of this process involves the use of your gmail account, although using this feature may affect in your privacy setting but in order to receive mail from third party you need to do this.

Google now doesn’t accept the login from less secure apps. So you need to go to [Google's Privacy Settings](https://myaccount.google.com/security) scroll to the bottom and turn ON “Allow less secure apps: ON”. You need to do this for the email ID you are adding in your Send as a section.

# Running the App

In order to run the app in your device, first you need to make some changes in the `encrypt.py` and the `settings.yaml` files. You need to modify the value of all those variables whose values are specified in between `< >`.

After changing the values of every variables,

`python3 main.py`