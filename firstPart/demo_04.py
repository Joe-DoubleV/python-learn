# string

# weekStr = '星期一星期二星期三星期四星期五星期六星期日'
# weekid = eval(input(chr(10004)))
# weekStr2 ='一二三四五六日'
# print(weekStr[weekid*3-3:weekid*3])
# x = weekStr2[weekid-1:weekid]
# print(f'星期{x}')
print(chr(10004),ord('a'))
for x in range(12):
	print(chr(9800+x),end='\t')
print("\n")
print("line".center(20,'-'))
print('line'.replace("ne","ke").center(20,'-'))
print(' ==line=+ '.strip(" +e=").center(20,'-'))
print('-'.join('line').center(20,'-'))

#format
'''
	:		引导符
	<填充>	填充的单个字符
	<对齐>	<>^，左右中对其
	<宽度>	输出宽度
'''
print ("{:#^20}".format("line"))
'''
	<,>		数字的千位分隔符
	<.精度>	浮点数小数精度
	<类型>	bcdoxX	eEf%
'''
print ("qwerty{:,.2f}".format(123456789.9876).center(40,"-"))
print ("{:b},{:c},{:d},{:o},{:x},{:X}".format(123,425,123,123,123,123))

print(chr(10003))
print ("qwerty{}".format(123456789.9876).center(40,"-"))
