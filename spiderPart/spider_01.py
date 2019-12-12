import requests
import os
url = "https://item.jd.com/4020721.html"

try:
	r = requests.get(url)
	r.raise_for_status()
	r.encoding = r.apparent_encoding
	# print(r.text[:1000])
except :
	print("Fails")

url = "https://www.amazon.cn/dp/B01JRE0HKW?_encoding=UTF8&ref_=pc_cxrd_2045366051_recTab_2045366051_t_1&pf_rd_p=e372c755-43c2-4ac7-b17e-8fc122a2e555&pf_rd_s=merchandised-search-4&pf_rd_t=101&pf_rd_i=2045366051&pf_rd_m=A1AJ19PSB66TGU&pf_rd_r=VZN7ER91VCY4X23SCP6A&pf_rd_r=VZN7ER91VCY4X23SCP6A&pf_rd_p=e372c755-43c2-4ac7-b17e-8fc122a2e555"

try:
	kv = {'User-Agent':'Mozilla/5.0'}
	r = requests.get(url,headers = kv)
	print(r.request.headers)
	r.raise_for_status()
	r.encoding = r.apparent_encoding
	print(r.text[1000:2000])
except :
	print("Fails")

url = "http://www.baidu.com/s"
keyword = "python"
try:
	kv = {'wd':keyword}
	r = requests.get(url,params=kv)
	print(r.request.url)
	r.raise_for_status
	print(len(r.text))
	# print (r.text)
except Exception as e:
	print(e)


url = "http://img0.dili360.com/ga/M01/02/E5/wKgBzFQ3PamAKFjyAAmhm4OCs9k158.jpg"
root = "E://pythonfile//mocc//pics//"
path = root + url.split('/')[-1]
try:
	if not os.path.exists(root):
		os.mkdir(root)
	if not os.path.exists(path):
		r = requests.get(url)
		# 二进制数据写入文件
		with open(path,'wb') as f:
			f.write(r.content)
			f.close()
			print("sucess")
	else:
		print("file exists")
except Exception as e:
	raise e

url = "http://m.ip138.com/ip.asp?ip="
ips = "219.140.62.45"
try:
	r = requests.get(url+ips)
	r.raise_for_status()
	r.encoding = r.apparent_encoding
	print(r.text[-500:])
except Exception as e:
 	print(e)