import os
import requests
import re
import json
from config import api_key


apikey = api_key
artist = 'pearl jam'
album = 'ten'
url = 'http://ws.audioscrobbler.com/2.0/?method=album.gettoptags&artist=' +  artist + '&album=' + album + '&api_key=' + apikey  + '&format=json'

r = requests.get(url)
r = r.text
album_tags = json.loads(r)

print(album_tags[0][0][1])
