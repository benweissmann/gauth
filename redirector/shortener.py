import urllib2
import json
from gauth.settings import GOOGLE_API_KEY

# Get a short, goo.gl link
def shorten(url):
    params = json.dumps({'longUrl': url})
    headers = {'Content-Type': 'application/json'}
    api_url = "https://www.googleapis.com/urlshortener/v1/url?key=" + GOOGLE_API_KEY
    req = urllib2.Request(api_url, params, headers)
    response = json.loads(urllib2.urlopen(req).read())
    return response['id']