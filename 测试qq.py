import time
from selenium import webdriver

acount=input("账号")
passwd=input("密码")
context=input()
driver = webdriver.Firefox()  # 获取火狐驱动
driver.get("https://user.qzone.qq.com/2487429967/311")
# 因为表在iFrame里面,所以需要进入iFrame里面
driver.switch_to.frame("login_frame")  # 找到frame入口
driver.find_element_by_id("switcher_plogin").click()  # 点击登录
driver.find_element_by_id("u").send_keys(acount)  # 账号
driver.find_element_by_id("p").send_keys(passwd)  # 密码
driver.find_element_by_id("login_button").click()#点击登陆按钮
print("登录成功！")
time.sleep(5)
#这是switch_to中独有的方法，可以切换到上一层的frame，对于层层嵌套的frame很有用
driver.switch_to.default_content()
# driver.find_element_by_id("QM_Profile_Mood_A").click()
# print('点击说说成功！')
# time.sleep(5)



try:

    driver.switch_to.frame('app_canvas_frame')  # 进入iFrame
    time.sleep(0.5)
    try:
            driver.find_element_by_css_selector('div.textinput.textarea.c_tx3').click()
            # 因为第一个找到的class无法点击，所以我们找到可以点击然后光标进入编辑框的，然后模拟点击
            time.sleep(0.5)
            driver.find_element_by_css_selector('div.textinput.textarea.c_tx2.input_focus.textinput_focus').send_keys(
            context)
            print('文字输入成功')
            driver.find_element_by_css_selector('a.btn-post.gb_bt.evt_click').click()
            print('发送成功！')
    finally:
        print('OK！')
finally:
    print('End')


