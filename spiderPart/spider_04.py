import re

print(re.search(r'[1-9]\d{5}',"ABCD 122500").group(0))

print(re.match(r'[1-9]\d{5}',"122500 asdc").group(0))

print(re.findall(r'[1-9]\d{5}',"122500 asdc 122528"))

print(re.split(r'[1-9]\d{5}',"zxcvb122500 asdc 122528qwerty"))

print(re.split(r'[1-9]\d{5}',"zxcvb122500 asdc 122528qwerty",maxsplit = 1))

for m in re.finditer(r'[1-9]\d{5}',"zxcvb122500 asdc 122528qwerty"):
	if m:
		print(m.group(0))

print(re.sub(r'[1-9]\d{5}','zipCode','lingyuan:122500,dahebi:122528'))

pat = re.compile(r'[1-9]\d{5}')
rst = pat.search('lingyuan:122500')
r = re.search(r'[1-9]\d{5}',"ABCD 122500")
print(type(rst),type(r))

print(rst.group(0))