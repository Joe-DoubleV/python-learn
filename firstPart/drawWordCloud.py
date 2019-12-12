import wordcloud
import jieba
from skimage import io
# import scipy
mask = io.imread("file/timg.jpg")
f = open("file/snow_4.txt","r",encoding='utf-8')
t = f.read()
f.close()
woldList = jieba.lcut(t)
# banList = ["只是","还是","不是","但是","就是","没有","这个","不过"]
# for x in woldList:
# 	if x in banList:
# 		woldList.remove(x)
		

txt = " ".join(woldList)
w = wordcloud.WordCloud(font_path = 'msyh.ttc', background_color = 'white',width = 1000,height = 700,mask = mask)
w.generate(txt)
w.to_file("cloudSnow_4.png")

# f = open("file/suggestion.txt","r",encoding='utf-8')
# t = f.read()
# f.close()
# ls = jieba.lcut(t)
# txt = " ".join(ls)
# # w = wordcloud.WordCloud(font_path = 'msyh.ttc', background_color = 'white',width = 1000,height = 700,max_words = 15)
# w.generate(txt)
# w.to_file("cloudSuggestion.png")