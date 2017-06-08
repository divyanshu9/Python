import urllib3
from bs4 import BeautifulSoup

http = urllib3.PoolManager()
def scrapit(url):
	response = http.request('GET', url)
	soup = BeautifulSoup(response.data)
	#print soup
	for tag in soup.find_all("h3", { "class" : "lister-item-header" }):
		lis = tag.find('a')
		text = lis.text.encode('ascii', 'ignore').decode('ascii')
		print text
		with open("namelist2.txt", "a") as f:
			f.write("\n"+text)
			print "Written"
	
i=1
while(i<11):
	url = "http://www.imdb.com/search/title?count=100&groups=top_1000&sort=user_rating&page=%s&ref_=adv_nxt" %(i)
	print url
	i+=1;
	scrapit(url)

