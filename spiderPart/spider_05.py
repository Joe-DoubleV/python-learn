'''https://s.taobao.com/search?q=%E4%B9%A6%E5%8C%85&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306
https://s.taobao.com/search?q=%E4%B9%A6%E5%8C%85&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&bcoffset=3&ntoffset=3&p4ppushleft=1%2C48&s=44
"view_price":"39.90","view_fee":"0.00","item_loc":"湖南 邵阳","raw_title"	'''

import requests
import re

def getHTMLText(url):
	try:
		r = requests.get(url,timeout = 30)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		return r.text
	except :
		return ""	
def parsePage(ilt,html):
	try:
		plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
		tlt = re.findall(r'\"raw_title\"\:\".*?\"',html)
		plc = re.findall(r'\"item_loc\"\:\".*?\"',html)
		for x in range(len(plt)):
			price = eval(plt[x].split(':')[1])
			plice = eval(plc[x].split(':')[1])
			title = eval(tlt[x].split(':')[1])
			ilt.append([price,plice,title])
	except :
		return ""
	

def printGoodsList(ilt):
	tplt = '{:4}\t{:8}\t{:8}\t{:16}'
	print(tplt.format('序号','价格','产地','商品名称'))
	count = 0
	
	for x in ilt:
		count += 1
		print(tplt.format(count,x[0],x[1],x[2]))

def main():
	goods = input("输入商品名：")
	depth = 1
	start_url = 'https://s.taobao.com/search?q=' + goods
	infoList = []
	for x in range(depth):
		try:
			url = start_url + '&s=' + str(44*x)
			html = getHTMLText(url)
			parsePage(infoList,html)
		except Exception as e:
			raise e
	printGoodsList(infoList)

if __name__ == '__main__':
	main()