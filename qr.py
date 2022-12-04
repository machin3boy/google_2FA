import importlib.util
from subprocess import run

# Check if pip is installed
if importlib.util.find_spec("pip") is None:
    # Download the get-pip.py script
    run(["curl", "https://bootstrap.pypa.io/get-pip.py", "-o", "get-pip.py"])
    # Install pip using the get-pip.py script
    run(["python", "get-pip.py"])

if importlib.util.find_spec("pyotp") is None:
    # Install the package using pip
    run(["pip", "install", "pyotp"])

if importlib.util.find_spec("qrcode") is None:
    # Install the package using pip
    run(["pip", "install", "qrcode"])

import pyotp
import qrcode

def random_secret():
    return pyotp.random_base32()

def totp(secret_key):
    # Generate a time-based one-time password (TOTP)
    totp = pyotp.TOTP(secret_key)

    return totp

def qr_object(uri):
    qr = qrcode.make(uri)

    return qr

def show_qr(qr_object):
    qr_object.show()

def prompt_totp():
    user_totp = input("Enter the TOTP from the Google Authenticator app: ")
    return user_totp

def verify_totp(totp_obj, user_totp):
    if totp_obj.verify(user_totp):
        print("TOTP verified successfully!")
    else:
        print("Invalid TOTP!")
       
if __name__=="__main__":
    totp_obj = totp(random_secret())
    #generate a URI for a QR code
    provisioning_uri = totp_obj.provisioning_uri("example issuer")
    qr_obj = qr_object(provisioning_uri)
    show_qr(qr_obj)
    user_totp = prompt_totp()
    verify_totp(totp_obj, user_totp)

