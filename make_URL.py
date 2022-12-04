import pyotp

def createURL(secret):
    return pyotp.totp.TOTP(secret).provisioning_uri(name='vera', issuer_name='Vera dApp')

if __name__=="__main__":
    x = createURL("sample")
    print(x)
