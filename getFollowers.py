import requests
import json
import sys

def getFollowers():
	screen_name = sys.argv[1]
	max_pages = 4 #number of pages (eg loops), change this to fit the account
	next_cursor = -1

	followers_ids = []

	for i in range(0,max_pages):
		url = 'https://api.twitter.com/1/followers/ids.json?screen_name=%s&cursor=%s' % (screen_name, next_cursor)
		content = requests.get(url).content
		data = json.loads(content)
		next_cursor = data['next_cursor']
		print "loop " , i, "cursor is", next_cursor
		followers_ids.extend(data['ids'])

        print "%s have %s followers!" % (screen_name, str(len(followers_ids)))

        f = open( screen_name + '.txt', 'w+')
	for item in followers_ids:
        f.write("%s\n" % item)
        f.close()
