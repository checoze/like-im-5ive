def is_url(term):
    if term.startswith('http' or 'www'):
        return True
    else:
        return False