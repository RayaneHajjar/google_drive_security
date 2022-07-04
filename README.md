# google_drive_security  

**Objective**: To make secure file storage in cloud computing using hybrid cryptography.

### Features
* Secure file data in Google Drive.
* Key is sent directly to your email.
* Pure-Python

### Getting Started
To get started with the code on this repo, you need to either clone or download this repo into your machine.

### Dependencies
Before you begin playing with the source code you might need to install deps just as shown below;
`pip install -r requirements.txt`

### Authentication
Drive API requires OAuth2.0 for authentication. PyDrive makes your life much easier by handling complex authentication steps for you.  
1. Go to (https://console.cloud.google.com). 
2. Create a new project and select it.  
3. Select ‘APIs & Services’ from the navigation bar.  
4. Select ‘Enable APIs and Services’.   
5. Search for ‘Google Drive API’ and enable it.  
6. Select ‘OAuth consent screen’ from the left menu.  
7. Check the ‘External’ option then click ‘Create’.  
8. Now enter your custom ‘App name’ and enter your gmail in both ‘User support email’ and ‘Developer contact information’ fields then click ‘Save and Continue’.  
9. Click ‘Save and Continue’ for Scopes and for Test Users then click ‘Back to Dashboard’.  
10. Select ‘Credentials’ from the left menu, click ‘Create Credentials’, select ‘OAuth client ID’.  
11. Select ‘Application type’ to be Desktop application. Enter an appropriate name. Input http://localhost:8080 for ‘Authorized JavaScript origins’. Input http://localhost:8080/ for ‘Authorized redirect URIs’. Click ‘Save’.  
12. Click ‘Download JSON’ on the right side of Client ID to download client_secret_<really long ID>.json.  
The downloaded file has all authentication information of your application. Rename the file to “client_secrets.json” and place it in your working directory.
13. Go back to ‘OAuth consent screen’ and click ‘Publish App’ then ‘Confirm’.  

### Setting up Gmail account
1. Go to (https://myaccount.google.com).  
2. Select ‘Security’ from the left menu.  
3. Click ‘App passwords’ under Signing in to Google.   
4. Select ‘other(custom name)’ on Select app. Enter your custom name. Select ‘Windows Computer’ on Select device. Click ‘Generate’. Copy the password to paste it inside the application.  

### Running the App
In order to run the app in your device, first you need to make some changes in the `encrypt.py` and the `settings.yaml` files. You need to modify the value of all those variables whose values are specified in between `< >`.  
For the password: enter the copied password.  
For the sender_email: enter your gmail used in the previous steps.  
For the receiver_email: enter an email to receive the informations needed like key.  
After changing the values of every variables, execute:  
`python main.py`
