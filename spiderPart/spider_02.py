import requests
from bs4 import BeautifulSoup
import re
global demo
url = "http://python123.io/ws/demo.html"
try:
	r = requests.get(url)
	r.raise_for_status()
	r.encoding = r.apparent_encoding
	demo = r.text
except Exception as e:
	print(e)

soup = BeautifulSoup(demo,"html.parser")

'''	Tag		Name 	Attributes	NavigableString Comment	'''
'''			.name 	.attr 		.string 		.string'''

# print("Tag(title):",soup.title)
# print("Tag(a）:",soup.a)

# print("Name(a.parent.name):",soup.a.parent.name)
# print("Attributes(a.attrs):",soup.a.attrs)
# print("a.attrs['class']:",soup.a.attrs['class'])

# print('type(soup.a.attrs):',type(soup.a.attrs))
# print('type(soup.a):',type(soup.a))

# print("NavigableString(soup.a.string):",soup.a.string)
# print(type(soup.a.string))

# print('soup.head:',soup.head)
# print('soup.head.contents:',soup.head.contents)

# print('soup.body:',soup.body)
# print('soup.body.contents:',soup.body.contents)
# print("".center(40,"-"))
# for child in soup.body.descendants:
# 	if child is None:
# 		print(child)
# 	else:
# 		print(child.name)

# print("".center(40,"-"))
# print(soup.a.parent)
# for parent in soup.a.parents:
# 	if parent is None:
# 		print(parent)
# 	else :
# 		print(parent.name)

# print(soup.prettify())

for link in soup.find_all(['a','p']):
	print(link.get("href"))
	print(link)

print("".center(40,"-"))
print (soup.find_all('p','course'))

print("".center(40,"-"))
print(soup.find_all(id=re.compile('.ink1')))

print("".center(40,"-"))
print(soup.find_all('a',recursive = False))

print("".center(40,"-"))
print(soup(string=re.compile('p.')))

print("".center(40,"-"))
print(soup.body(string=re.compile('p.')))