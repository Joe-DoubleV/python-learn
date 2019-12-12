import wordcloud
import jieba
from skimage import io
# import scipy
mask = io.imread("file/timg.jpg")
f = open("file/nightComing.txt","r",encoding='utf-8')
t = f.read()
f.close()
ls = jieba.lcut(t)
txt = " ".join(ls)
w = wordcloud.WordCloud(font_path = 'msyh.ttc', background_color = 'white',width = 1000,height = 700,mask = mask)
w.generate(txt)
w.to_file("cloudNight.png")

# f = open("file/suggestion.txt","r",encoding='utf-8')
# t = f.read()
# f.close()
# ls = jieba.lcut(t)
# txt = " ".join(ls)
# # w = wordcloud.WordCloud(font_path = 'msyh.ttc', background_color = 'white',width = 1000,height = 700,max_words = 15)
# w.generate(txt)
# w.to_file("cloudSuggestion.png")