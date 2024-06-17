import base64

# Given string
encoded_string = "1fOdmrR9DcdaceoJ3f328O53X4Q0BayLyDd1gNrBs1U="

# Decode the given string from base64
decoded_bytes = base64.urlsafe_b64decode(encoded_string)

# If the length is not 32, adjust accordingly
if len(decoded_bytes) != 32:
    print("yes")
    if len(decoded_bytes) > 32:
        decoded_bytes = decoded_bytes[:32]  # Truncate
    else:
        decoded_bytes = decoded_bytes + b'=' * (32 - len(decoded_bytes))  # Pad with '='

# Encode the bytes back to base64
fernet_key = base64.urlsafe_b64encode(decoded_bytes).decode()

print("Fernet key:", fernet_key)