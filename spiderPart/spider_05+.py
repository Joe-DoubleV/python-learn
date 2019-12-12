import requests
import re
import bs4

def getHTMLText(url,kv):
	try:
		r = requests.get(url,params = kv,timeout = 30)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		return r.text

	except Exception as e:
		return ""	

def getHtmlByLocal():
	file = open('./ht.html','rb')
	ht =  file.read()
	# print (ht)
	return ht



def fillInfoList(infoList,html):
	soup = bs4.BeautifulSoup(html,"html.parser")
	goodTemList = soup.body('ul', class_="gl-warp clearfix")[0].find_all('li')

	count = 0
	for tag in goodTemList:
		count += 1
		try :
			price = tag.find(class_ = "p-price").i.string
			if price is None:				
				price = tag.find(class_ = "p-price").strong.attrs['data-price']
			if price is None:
				price = 'unknown'

			name_type = tag.find(class_ = "p-name p-name-type-2").em.text
			infoList.append([count,price,name_type])			
		except :
			continue

def printList(infoList):
	tlt = '{:<4}\t{:^6}\t{}'
	print(tlt.format('	','价格','产品'))
	for x in infoList:
		print(tlt.format(x[0],x[1],x[2]))

def writeList(infoList, fileName='jd2'):
	tlt = '{:<4},{:^6},{}\n'
	filePath = './{}.csv'.format(fileName)
	fo = open(filePath,'w')
	fo.write(tlt.format('index','价格','商品'))
	for x in infoList:
		fo.write(tlt.format(x[0],x[1],x[2]))

def main():
	JD_url = 'https://search.jd.com/Search?keyword={}&enc=utf-8'
	JD_url = 'https://search.jd.com/Search?keyword=%E5%8D%8E%E4%B8%BA&enc=utf-8&suggest=1.his.0.0&wq=&pvid=5265a916013846cb9162a1567eb6fd2b'
	JD_url = 'https://diannao.jd.com/'
	JD_url = 'https://search.jd.com/Search?'
	
	
	infoList = []
	html = getHtmlByLocal()
	# print(html)
	fillInfoList(infoList,html)
	printList(infoList)
	# writeList(infoList, 'jdinfo')
if __name__ == '__main__':
	main()