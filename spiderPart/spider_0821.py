import requests
import re
import bs4
import traceback

def getHTMLText(url, code="utf-8"):
	try:
		r = requests.get(url)
		r.raise_for_status()
		r.encoding = code
		return r.text
	except:
		return ""

def getStockList(lst,stockUrl):
	html = getHTMLText(stockUrl)
	soup = bs4.BeautifulSoup(html,'html.parser')
	a = soup.find_all('a')
	for x in a:
		try:
			href = x.attrs['href']
			lst.append(re.findall(r'sh[3-9]\d{5}|sz\d{6}',href)[0])
		except :
			continue
	# print(len(lst))
	# print(lst)
def getStockInfo(lst,stockUrl,fPath):
	count = 0
	for x in lst:

		html = getHTMLText(stockUrl.format(x))
		try:
			if html == "":
				count +=1 
				print("\r当前进度: {:.2f}%".format(count*100/len(lst)),end="")
				continue
			stockData = {}
			soup = bs4.BeautifulSoup(html,'html.parser')
			stockName = re.split(" ",re.findall(r'\S.*',soup.h1.a.text)[0])[0]		#get stock name
			stockPrice = soup.find(class_ = "_close").string						#get stock price
			if stockPrice is None:
				count +=1 
				print("\r当前进度: {:.2f}%".format(count*100/len(lst)),end="")
				continue
			stockData['股票代码'] = x
			stockData['股票名称'] = stockName
			stockData['股票价格'] = stockPrice
			for d in soup.find(class_='bets-content').find_all('dl'):
				# print(d.dt.text,d.dd.text)
				stockData[d.dt.text] = re.findall(r'\S.*',d.dd.text)[0]


			if stockData['成交量'] =='--':
				stockData.clear
			else:
				with open(fPath,'a',encoding = 'utf-8') as f:
					f.write(str(stockData)+'\n')
			count +=1 
			print("\r当前进度: {:.2f}%".format(count*100/len(lst)),end="")
		except :
			# traceback.print_exc()
			# print(html)
			count +=1 
			print("\r当前进度: {:.2f}%".format(count*100/len(lst)),end="")
			continue
		
		# print(type(soup.find(class_='bets-content').find_all('dl')))

		# print(re.split(" ",re.findall(r'\S.*',soup.h1.a.text)[0])[0],soup.find(class_ = "_close").string)



def main():
	stock_list_url = 'http://quote.eastmoney.com/stock_list.html'
	stock_info_url = 'https://gupiao.baidu.com/stock/{}.html'
	out_file_path = 'E:/pythonfile/mocc/BaiduStock.txt'
	stockList = []

	getStockList(stockList,stock_list_url)
	# print(stockList)
	getStockInfo(stockList[:100],stock_info_url,out_file_path)

if __name__ == '__main__':
	main()