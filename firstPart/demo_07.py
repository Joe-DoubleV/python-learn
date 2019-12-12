#
height,weight = eval(input("m,kg"))
bmi = weight / pow(height, 2)
print ("BMI值为:{:.2f}".format(bmi))
who,nat = "",""

if bmi < 18.5 :
	who,nat = "偏瘦","偏瘦"
elif bmi < 24 :
	who,nat = "正常","正常"
elif bmi < 25 :
	who,nat = "正常","偏胖"
elif bmi < 28 :
	who,nat = "偏胖","偏胖"
elif bmi < 30 :
	who,nat = "偏胖","肥胖"
else :
	who,nat = "肥胖","肥胖"

print ("根据国际BMI制身体{},根据国内BMI制身体{}".format(who,nat))
