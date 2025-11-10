import hashlib

def mashthis(title:str, link:str):
    combined = (title+link).encode("utf-8")
    return hashlib.sha256(combined).hexdigest()
    