# _*_coding=utf8 _*_
import os,io,sys
import shutil
import requests
from lxml import etree
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding="utf8") #改变标准输出的默认
global pf
global arr
pf= False  # 决定是否写入文件

path=''
arr=[]
if pf:
    path = "E:\\文字语录\\"
    if os.path.exists(path):
        shutil.rmtree(path)
    os.mkdir(path)





def main_cont(url):
    global arr
    text = get_requests(url)
    txt=get_content(text, path, pf)
    for i in txt:
        arr.append(i)
#请求网络-获取服务器响应的数据
def get_requests(url):
    headers={
        "User - Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
    }
    html = requests.get(url,headers=headers)
    if html.status_code==200:
        return html.text
    else:
        return None
# 第二步解析数据，保存数据
def get_content(text,path,pf):
     try:
         html = etree.HTML(text)
         name = html.xpath('//h1/text()')
         # 分割字符串
         name = str(name)
         # print(name)
         aname = name.split("'")
         print(aname[1])
         txt=html.xpath('//p/text()')
     except Exception as e:
         return

     if pf:
         try:  # 写入文件
             with open(path + aname[1] + '.txt', 'w') as f:
                 for i in txt:
                     if i:
                         f.write(i)
         except Exception as e:
             return
     return txt
def Print():
    num = 30002
    while (num < 30041):
        url = "https://www.mindhave.com/jingdianyulu/{}.html".format(num)

        num = num + 1
        main_cont(url)
        # string=main_cont(url)
        # for i in string:
        #     print(i)

    with open('1.txt','w',encoding='utf8') as f:
        for i in arr:
             i=str(i).replace('\t\u3000\u3000','')
             i=i.replace('\xa0\xa0\xa0\xa0','')
             f.write(i)


if __name__== '__main__':
    Print()









