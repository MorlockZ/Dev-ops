#from bs4 import BeautifulSoup
import requests
from pyquery import PyQuery as pq  #用来解析HTML文件的包 ，别名是pq
newsurl = 'https://m.hupu.com/bbs/20415703.html'   #需要解析的网址
res = requests.get(newsurl)   #火器营网址返回的htmlb编码
#print (res.text)
d = pq(res.text)     #把返回的编码放入pq并赋值给d
print (d.html())
nr = d('span').filter('.short-content').text()  #选择span标签并筛选.short-content文本（text）
f = open(r'e:\test.txt','w+')
f.write(nr)
f.close() 