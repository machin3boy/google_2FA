import pyotp
import qrcode

# Generate a secret key
secret_key = pyotp.random_base32()

# Store the secret key in your database and associate it with the user's account

# Generate a time-based one-time password (TOTP)
totp = pyotp.TOTP(secret_key)

# Generate a provisioning URI that contains the secret key
provisioning_uri = totp.provisioning_uri("example@example.com", issuer_name="Example")

# Generate a QR code image from the provisioning URI
qr = qrcode.make(provisioning_uri)

# Display the QR code image to the user so that they can scan it using the Google Authenticator app
qr.show()

# Prompt the user to enter the TOTP from the Google Authenticator app
user_totp = input("Enter the TOTP from the Google Authenticator app: ")

# Verify the TOTP
if totp.verify(user_totp):
    print("TOTP verified successfully!")
else:
    print("Invalid TOTP!")

