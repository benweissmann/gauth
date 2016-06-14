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
    
    headings = root.cssselect('div[role=heading]:contains("'+TOKEN_FIELD_NAME+'")')
    if len(headings) < 1:
        return None

    heading = headings[0]
    parent_wrappers = [e for e in heading.iterancestors() if e.attrib.get('role') == 'listitem']
    if len(parent_wrappers) < 1:
        return None

    parent_wrapper = parent_wrappers[0]
    inputs = parent_wrapper.cssselect('input[type=hidden]')
    if len(inputs) < 1:
        return None    

    return inputs[0].get('name')


