#导入wordcloud模块
from wordcloud import  WordCloud
from scipy.misc import imread

#读取一个txt文件
text = open('C:\\Users\\\yuan.zhai\\Desktop\\小甜心(1604425524).txt','r', encoding='UTF-8').read()
#读入背景图片
bg_pic = imread('C:\\Users\\\yuan.zhai\\Desktop\\222.png')
#生成词云
wordcloud = WordCloud(font_path="C:\\Windows\\Fonts\\simfang.ttf",mask=bg_pic,background_color='white',scale=1.5,max_words=2002200).generate(text)
#保存图片
wordcloud.to_file('test.jpg')