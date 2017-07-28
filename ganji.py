#进入赶集网网络安全工程师的页面，找到每个公司的网址，将每个公司在网页中对于的代码保存在company.txt中，进入每个公司对应的网址，抓取公司的名称，保存在company.txt中
import requests,bs4,re,types
url='http://sz.ganji.com/zpwlaqgongchengshi/'
req=requests.get(url)
try:
    req.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))
wr=open('d.html','wb')
for chunk in req.iter_content(10000):
    wr.write(chunk)
wr.close()
soup=bs4.BeautifulSoup(req.text,'lxml')
company=soup.select('.new-dl-company')
ur=soup.select('a')
urregex=re.compile(r'http://www.ganji.com/gongsi/(\d+)/')
mo=urregex.search('hello http://www.ganj')
print(mo==None)
mo=urregex.search('hello http://www.ganji.com/gongsi/kkk999/')
print(mo)
com=open('company.txt','w')
#for i in range(len(company)):
    #print(company[i].getText())
for i in range(len(ur)):
    #print(ur[i].get('href'))
    strr=ur[i].get('href')
    if isinstance(strr,(str))==True:
        com.write(strr+' ')

com.close()
text=open('company.txt','r')
judge=urregex.findall(text.read())
print(judge)
print(len(judge))
gj=open('ganjigs.txt','a')
for i in range(len(judge)):
    c1=judge[i]
    curl='http://www.ganji.com/gongsi/'+c1
    creq=requests.get(curl)
    soupp=bs4.BeautifulSoup(creq.text,'lxml')
    ccom=soupp.select('.c-title')
    #for i in range(len(ccom)):
    if len(ccom)!=0:
        #print(ccom[0].getText())
        gj.write(ccom[0].getText())
gj.close()
