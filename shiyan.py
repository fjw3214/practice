# _*_coding=utf8 _*_
import time
from selenium import webdriver
import io,sys
import requests
from lxml import etree
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding="utf8") #改变标准输出的默认

def main_cont():
    arr=[]
    num = 30002
    while (num < 30041):
        url = "https://www.mindhave.com/jingdianyulu/{}.html".format(num)
        num = num + 1
        text = get_requests(url)
        txt=get_content(text)
        for i in txt:
            arr.append(i)
    return arr
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
def get_content(text):
     try:
         html = etree.HTML(text)
         txt=html.xpath('//p/text()')
     except Exception as e:
         return
     return txt

def auto_send(context):
    acount = 2487429967
    passwd = 'wobushi666'
    driver = webdriver.Firefox()  # 获取火狐驱动
    driver.get("https://user.qzone.qq.com/2487429967/311")
    driver.switch_to.frame("login_frame")  # 找到frame入口
    driver.find_element_by_id("switcher_plogin").click()  # 点击登录
    driver.find_element_by_id("u").send_keys(acount)  # 账号
    driver.find_element_by_id("p").send_keys(passwd)  # 密码
    driver.find_element_by_id("login_button").click()  # 点击登陆按钮
    print("登录成功！")
    time.sleep(5)
    driver.switch_to.default_content()
    try:
        driver.switch_to.frame('app_canvas_frame')  # 进入iFrame
        time.sleep(0.5)
        try:
            # driver.find_element_by_css_selector('div.textinput.textarea.c_tx3').click()
           # driver.find_element_by_xpath(".//*[@class='textinput textarea c_tx3']").click()
            time.sleep(0.5)
            print('@')
            driver.find_element_by_css_selector(
                'div.textinput.textarea.c_tx2.input_focus.textinput_focus').send_keys(
                context)
            print('文字输入成功')
            driver.find_element_by_css_selector('a.btn-post.gb_bt.evt_click').click()
            print('发送成功！')
        except Exception as e:
            print(e)
    finally:
        print('End')
        driver.close()


#$1_content_content

#could not be scrolled into view:
# 可见元素定位原因，某些情况元素的visibility为hidden或者display属性为none，
# 我们在页面看不到但是实际是存在页面的一些元素，这时候用 is_displayed（） 来判断

if __name__=='__main__':
    arr = main_cont()
    for i in arr:
        context = str(i)
        print(context)
        auto_send(context)
