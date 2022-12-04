## Google 2FA

Python program to verify 2FA codes generated through the Google Authenticator app.

Given a base32 secret, this program can return a provisioning URI which can then be displayed as a QR code for a user to onboard the issuer (this program/service where this program will be used). This program also contains a function which, when given a base32 secret, can verify that a particular user provisioned a valid TOTP with the help of the Google Authenticator app. 

"example issuer" can be changed to any name.

Run the program (as a script and not a module) for an example. The `qrcode` package is used to display the QR code you can scan with your app and a random secret is used in the example run. 
