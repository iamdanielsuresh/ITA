def validate_username(username, minlen):
    if minlen < 1:
        raise ValueError("minlen must be atleast 1")
    if len(username) < minlen:
        return False
    if not username.isalnum():
        return False
    return True

