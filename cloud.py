import jieba
from matplotlib import pyplot as plt
from wordcloud import WordCloud
from PIL import Image
import numpy as np
import sqlite3


#准备词云所需的
con = sqlite3.connect('job_boss.db')
cur = con.cursor()
sql = 'select miaoshu from boss'
data = cur.execute(sql)
text = ""
for item in data:
    text =  text + item[0]
    #print(item[0])
#print(text)
cur.close()
con.close()

#分词
cut = jieba.cut(text)
string = ' '.join(cut)
print(len(string))


img = Image.open(r'.\static\assets\img\tree.jpg')   #遮罩
img_array = np.array(img)
wc = WordCloud(
    background_color='white',
    mask=img_array,
    font_path="msyh.ttc"    #字体所在位置：C:\Windows\Fonts
)

# pic = WordCloud().generate(string)
#
# plt.imshow(pic)
#
# plt.show()

wc.generate_from_text(string)


#绘制图片
fig = plt.figure(1)
plt.imshow(wc)
plt.axis('off')

plt.show()

#输出词云图片到文件
#plt.savefig(r'.\static\assets\img\word.jpg',dpi=500)

#















