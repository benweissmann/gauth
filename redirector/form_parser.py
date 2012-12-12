import urllib2
import lxml.html

TOKEN_FIELD_NAME = "Authentication Token"

# gets the entry id for the auth token field
def get_entry_id(form_url):
    try:
        page = urllib2.urlopen(form_url)
    except urllib2.HTTPError:
        return None

    p = lxml.html.parse(page)
    root = p.getroot()
    labels = root.cssselect('label:contains("Authentication Token")')
    if len(labels) < 1:
        return None
    return labels[0].get('for')


