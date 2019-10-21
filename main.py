import os
import requests
import re
import json
from config import api_key


apikey = api_key

def get_top_tag(artist, album):
    url = 'http://ws.audioscrobbler.com/2.0/?method=album.gettoptags&artist=' + artist + '&album=' + album + '&api_key=' + apikey + '&format=json'

    r = requests.get(url)
    r = r.text
    album_tags = json.loads(r)

    tag_count = 5
    tags = []

    if len(album_tags['toptags']['tag']) < 5:
        tag_count = len(album_tags['toptags']['tag'])

    for item in album_tags['toptags']['tag'][:tag_count]:
        tags.append(item['name'])

    return tags


with open("1001.txt", "r", encoding="utf-8") as reader:
    line = reader.readline()
    artist_pattern = re.compile(r'.*(?=\s\-)')
    album_pattern = re.compile(r'(?<=-\s).*')

    while line != '':
        if artist_pattern.search(line) != None:
            result = artist_pattern.search(line)
            artist = result.group(0)
        if album_pattern.search(line) != None:
            result = album_pattern.search(line)
            album = result.group(0)
        print('artist: ' + artist + ' album: ' + album + get_top_tag(artist, album))
        line = reader.readline()