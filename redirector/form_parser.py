import urllib2
import lxml.html
from gauth.settings import TOKEN_FIELD_NAME

# gets the entry id for the auth token field
def get_entry_id(form_url):
    try:
        page = urllib2.urlopen(form_url)
    except urllib2.HTTPError:
        return None

    p = lxml.html.parse(page)
    root = p.getroot()
    labels = root.cssselect('label:contains("'+TOKEN_FIELD_NAME+'")')
    if len(labels) < 1:
        return None
    return labels[0].get('for')


