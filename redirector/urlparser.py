import urlparse

def get_formkey(url):
    parsed = urlparse.urlparse(url)
    params = urlparse.parse_qs(parsed.query)
    if not 'formkey' in params:
        return None
    else:
        return params['formkey'][0]