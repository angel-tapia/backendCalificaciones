import requests
from jose import jwt, JWTError
from fastapi import HTTPException

# Replace {tenant_id} with your actual Azure tenant ID
AZURE_DISCOVERY_URL = "https://login.microsoftonline.com/caca9011-7b6a-44de-861f-095a2ca883b7/v2.0/.well-known/openid-configuration"
response = requests.get(AZURE_DISCOVERY_URL)
jwks_uri = response.json()["jwks_uri"]
keys = requests.get(jwks_uri).json()["keys"]

def verify_token(token: str) -> bool:
    token = token.split(" ")[1]
    try:
      unverified_header = jwt.get_unverified_header(token)
    except JWTError:
        return False
        #raise HTTPException(status_code=401, detail="Invalid token header.")

    rsa_key = {}
    for key in keys:
        if key["kid"] == unverified_header["kid"]:
            rsa_key = {
                "kty": key["kty"],
                "kid": key["kid"],
                "use": key["use"],
                "n": key["n"],
                "e": key["e"]
            }
    if rsa_key:
        try:
            payload = jwt.decode(token, rsa_key, algorithms=["RS256"], audience="1ace8fa1-74dd-4854-b713-95c6738b5c3b")
            return True
        except JWTError:
            return False
            #raise HTTPException(status_code=401, detail="Token is invalid or expired.")
    else:
        return False
        #raise HTTPException(status_code=401, detail="Invalid token header.")