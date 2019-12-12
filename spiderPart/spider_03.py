import requests
import bs4
import re

url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html'
global demo 

def getHTMLText(url):
	try:
		r = requests.get(url,timeout = 30)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		return r.text

	except Exception as e:
		return ""	

def fillUnivList(uList,html):
	soup = bs4.BeautifulSoup(html,'html.parser')
	for tr in soup.find('tbody').children :
		if isinstance(tr,bs4.element.Tag) :
			tds = tr('td')
			uList.append([tds[0].string,tds[1].string,tds[2].string,tds[3].string])


def printUnivList(uList,num):
	plt = '{0:^6}\t{1:{4}^10}\t{2:{4}^6}\t{3:<6}'
	print (plt.format("排名","学校","地区","得分",chr(12288)))
	for x in range(num):
		u = uList[x]
		print (plt.format(u[0],u[1],u[2],str(u[3]),chr(12288)))

def main():
	uinfo = []
	url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html'
	html = getHTMLText(url)
	fillUnivList(uinfo,html)
	printUnivList(uinfo,20)

if __name__ == '__main__':
	main()