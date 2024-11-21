def alphanumeric(password):
    import re

    return bool(re.fullmatch(r"[a-zA-Z0-9]+", password))

