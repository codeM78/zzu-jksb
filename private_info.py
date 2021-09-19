import os

if __name__ == '__main__':
    
    UID = os.environ["UID"]
    PWD = os.environ["PWD"]

    MAIL_USER = os.environ["MAIL_USER"]
    # 这里是授权码--不是账户密码
    MAIL_PWD = os.environ["MAIL_PWD"]
    MAIL_TO = os.environ["MAIL_TO"]
