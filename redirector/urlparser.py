import urlparse

def get_formkey(url):
    parts = [part for part in urlparse.urlparse(url).path.split('/') if len(part) > 0]
    if len(parts) != 4:
        return None
    if parts[0] != 'forms':
        return None
    if parts[1] != 'd':
        return None
    if parts[3] != 'viewform':
        return None
    if (len(parts[2]) < 20):
        return None
    return parts[2]
