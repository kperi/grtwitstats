import requests
import json
import sys

#open a file with twitter ids, and foreach id fetch info. print screen name, followers count, friends count, statuses count & created at fields
def getStatistics(fileWithIds):
	max_pages = 150	 
	f = open(fileWithIdsz, 'r+')
	lines = [line.strip() for line in f]
	f.close()
 
	startingIndex = 0
	total = ""
	for i in range(0,max_pages):
	
		try:
			fromIndex = startingIndex + i*100;
			toIndex = startingIndex + (i+1)*100;
			id_list = ",".join( lines[ fromIndex :toIndex ] );
			
			url = 'https://api.twitter.com/1/users/lookup.json?user_id=%s&include_entities=false' % (id_list)
			content = requests.get(url).content
			data = json.loads(content)
			for j in range(0, len(data)):
				print  data[j]['screen_name'], "\t", data[j]['followers_count'], "\t", data[j]['friends_count'], "\t", data[j]['created_at'], "\t", data[j]['statuses_count'] 
		except:
			break

	print "completed"
