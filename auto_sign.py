# -*- coding:utf-8 -*-

import time
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from private_info import *
import mail

'''可以写个log日志，获取日志信息--有空再说吧'''

# 驱动路径
driver_path = "./chromedriver"

# 伪装 User-Agent--使用驱动自带伪装头，当然也可以自己设置(设置与否都行)
# 更换头部  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.73"
user_agent = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.73"
)


def sign_in(uid, pwd):

    # set to no-window
    chrome_options = Options()
    # 不打开窗口设置
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    # 伪装头部--可注释
    chrome_options.add_argument('user-agent=%s'%user_agent)

    # simulate a browser to open the website
    browser = webdriver.Chrome(options=chrome_options
                                #这里记得配置自己的浏览器驱动
                               ,executable_path=driver_path)
    # browser = webdriver.Chrome()
    # 连接被浏览器提示为不安全，浏览器添加白名单即可
    browser.get("https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/first0")

    # input uid and password
    # //*[@id="mt_5"]/div[2]/div[3]/input  //*[@id="mt_5"]/div[3]/div[3]/input
    print("Inputting the UID and Password of User {0}".format(uid))
    # 进不去了--（可能测试的时候频繁访问被检测了），定位不到，加个轮询和异常处理--缓解一下。
    while 1:
        start = time.time()
        try:
            browser.find_element_by_xpath('//*[@id="mt_5"]/div[2]/div[3]/input').send_keys(uid)
            browser.find_element_by_xpath('//*[@id="mt_5"]/div[3]/div[3]/input').send_keys(pwd)
            print('------元素已定位------')
            end = time.time()
            break
        except:
            # 频繁访问就会定位不到元素
            print("还未定位到元素!")
    print('定位耗费时间：'+str(end-start))

    # click to sign in  点击登录
    browser.find_element_by_xpath("//*[@id='mt_5']/div[5]/div/input").click()
    time.sleep(3)

    # get middle info 定位iframe并使用get请求到信息
    real_mid_page_url = browser.find_element_by_xpath("//*[@id='zzj_top_6s']").get_attribute("src")
    browser.get(real_mid_page_url)

    print("Checking whether User {0} has signed in".format(uid))
    msg = browser.find_element_by_xpath("//*[@id='bak_0']/div[7]/span").text
    # 如果今日填报过就退出填报，直接返回msg
    if msg == "今日您已经填报过了":
        return msg

    # 点击本人填报
    span_text = browser.find_element_by_xpath("//*[@id='bak_0']/div[13]/div[3]/div[4]/span").text
    if span_text == "本人填报":
        browser.find_element_by_xpath("//*[@id='bak_0']/div[13]/div[3]/div[4]").click()
    else:
        browser.find_element_by_xpath("//*[@id='bak_0']/div[13]/div[3]/div[6]").click()

    time.sleep(2)

    # click to fill in 填充表格
    # 适配填报健康码绿码和疫苗接种两针，其实不做新的适配也能’伪‘打卡--打卡成功（虽然信息提示失败）
    # 健康码绿码
    browser.find_element_by_xpath('//*[@id="bak_0"]/div[8]/div[2]/div[2]/div[2]/select[1]/option[2]').click()
    time.sleep(1)
    # 疫苗接种两针
    browser.find_element_by_xpath('//*[@id="bak_0"]/div[8]/div[2]/div[2]/div[2]/div[2]/select/option[3]').click()


    # click to submit  提交表格
    print("Signing in for User {0}".format(uid))
    browser.find_element_by_xpath('//*[@id="bak_0"]/div[8]/div[2]/div[2]/div[2]/div[6]/div[4]/span').click()
    time.sleep(2)

    final_text = browser.find_element_by_xpath("//*[@id='bak_0']/div[2]/div[2]/div[2]/div[2]").text

    # quit the browser
    print("Singing in for User {0} is finished".format(uid))
    browser.quit()
    return final_text


if __name__ == "__main__":

    # For Single User
    pass
    msg = sign_in(UID, PWD)
    # # 发送邮件信息
    mail.mail(msg, MAIL_TO)

    # # For Multiple Users  多用户打卡
    # # 设置了定时，但是需要一直开启服务--一直后台运行。（不建议）不如直接设置定时计划
    # while True:
    #     while True:
    #         now = datetime.datetime.now()
    #         # 修改定时
    #         if now.hour == 6 and now.minute == 0:
    #             break
    #         time.sleep(30)
    #
    #     for user in users:
    #         msg = sign_in(user.uid, user.pwd)
    #         print("Emailing to User {0} for notification".format(user.uid))
    #         mail.mail(msg, user.email)
    #         print("Emailing is finished")
