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
		print('artist - ' + artist + ' album: ' + album)
			#print(line, end='')
		line = reader.readline()