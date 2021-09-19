# -*- coding:gbk -*-

import time
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from private_info import *
import mail

'''����д��log��־����ȡ��־��Ϣ--�п���˵��'''

# ����·��
driver_path = "../zhengzhou_community/chromedriver.exe"

# αװ User-Agent--ʹ�������Դ�αװͷ����ȻҲ�����Լ�����(���������)
# ����ͷ��  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.73"
user_agent = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.73"
)


def sign_in(uid, pwd):

    # set to no-window
    chrome_options = Options()
    # ���򿪴�������
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    # αװͷ��--��ע��
    chrome_options.add_argument('user-agent=%s'%user_agent)

    # simulate a browser to open the website
    browser = webdriver.Chrome(options=chrome_options
                                #����ǵ������Լ������������
                               ,executable_path=driver_path)
    # browser = webdriver.Chrome()
    # ���ӱ��������ʾΪ����ȫ���������Ӱ���������
    browser.get("https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/first0")

    # input uid and password
    # //*[@id="mt_5"]/div[2]/div[3]/input  //*[@id="mt_5"]/div[3]/div[3]/input
    print("Inputting the UID and Password of User {0}".format(uid))
    # ����ȥ��--�����ܲ��Ե�ʱ��Ƶ�����ʱ�����ˣ�����λ�������Ӹ���ѯ���쳣����--����һ�¡�
    while 1:
        start = time.time()
        try:
            browser.find_element_by_xpath('//*[@id="mt_5"]/div[2]/div[3]/input').send_keys(uid)
            browser.find_element_by_xpath('//*[@id="mt_5"]/div[3]/div[3]/input').send_keys(pwd)
            print('------Ԫ���Ѷ�λ------')
            end = time.time()
            break
        except:
            # Ƶ�����ʾͻᶨλ����Ԫ��
            print("��δ��λ��Ԫ��!")
    print('��λ�ķ�ʱ�䣺'+str(end-start))

    # click to sign in  �����¼
    browser.find_element_by_xpath("//*[@id='mt_5']/div[5]/div/input").click()
    time.sleep(3)

    # get middle info ��λiframe��ʹ��get������Ϣ
    real_mid_page_url = browser.find_element_by_xpath("//*[@id='zzj_top_6s']").get_attribute("src")
    browser.get(real_mid_page_url)

    print("Checking whether User {0} has signed in".format(uid))
    msg = browser.find_element_by_xpath("//*[@id='bak_0']/div[7]/span").text
    # �������������˳����ֱ�ӷ���msg
    if msg == "�������Ѿ������":
        return msg

    # ��������
    span_text = browser.find_element_by_xpath("//*[@id='bak_0']/div[13]/div[3]/div[4]/span").text
    if span_text == "�����":
        browser.find_element_by_xpath("//*[@id='bak_0']/div[13]/div[3]/div[4]").click()
    else:
        browser.find_element_by_xpath("//*[@id='bak_0']/div[13]/div[3]/div[6]").click()

    time.sleep(2)

    # click to fill in �����
    # ��������������������������룬��ʵ�����µ�����Ҳ�ܡ�α����--�򿨳ɹ�����Ȼ��Ϣ��ʾʧ�ܣ�
    # ����������
    browser.find_element_by_xpath('//*[@id="bak_0"]/div[8]/div[2]/div[2]/div[2]/select[1]/option[2]').click()
    time.sleep(1)
    # �����������
    browser.find_element_by_xpath('//*[@id="bak_0"]/div[8]/div[2]/div[2]/div[2]/div[2]/select/option[3]').click()


    # click to submit  �ύ���
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
    # # �����ʼ���Ϣ
    mail.mail(msg, MAIL_TO)

    # # For Multiple Users  ���û���
    # # �����˶�ʱ��������Ҫһֱ��������--һֱ��̨���С��������飩����ֱ�����ö�ʱ�ƻ�
    # while True:
    #     while True:
    #         now = datetime.datetime.now()
    #         # �޸Ķ�ʱ
    #         if now.hour == 6 and now.minute == 0:
    #             break
    #         time.sleep(30)
    #
    #     for user in users:
    #         msg = sign_in(user.uid, user.pwd)
    #         print("Emailing to User {0} for notification".format(user.uid))
    #         mail.mail(msg, user.email)
    #         print("Emailing is finished")
