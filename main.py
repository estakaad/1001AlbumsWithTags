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

    if 'toptags' in album_tags:
        if len(album_tags['toptags']['tag']) < 5:
            tag_count = len(album_tags['toptags']['tag'])
        if album_tags['toptags']['tag']:
            for item in album_tags['toptags']['tag'][:tag_count]:
                tags.append(item['name'])
        else:
            tags.append('N/A')
    else:
        tags.append('N/A')

    return tags


def write_results_to_file(input_file):
    with open(input_file, 'r', encoding='utf-8') as reader:
        line = reader.readline()
        artist_pattern = re.compile(r'.*(?=\s\-)')
        the_artist_pattern = re.compile(r'.*(?=,\sThe\s)')
        album_pattern = re.compile(r'(?<=-\s).*')

        while line != '':
            with open('albums_with_tags.txt', 'a', encoding='utf-8') as results_file:
                if artist_pattern.search(line) != None:
                    if the_artist_pattern.search(line) != None:
                        result = the_artist_pattern.search(line)
                        artist = 'The ' + result.group(0)
                    else:
                        result = artist_pattern.search(line)
                        artist = result.group(0)
                if album_pattern.search(line) != None:
                    result = album_pattern.search(line)
                    album = result.group(0)
                tags = get_top_tag(artist, album)
                results_file.write(artist + ' - ' + album + ' - ' + ', '.join(tags) + '\n')
                line = reader.readline()

write_results_to_file('1001.txt')