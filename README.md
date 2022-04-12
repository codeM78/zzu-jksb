# 郑州大学健康状况上报平台自动打卡脚本

该脚本仅用于自动打卡郑州大学健康状况上报平台。

## 所需依赖
```
python==3.7
selenium
浏览器对应的驱动，如ChromeDriver
```

## 设置
本项目正在尝试使用GitHub提供的Actions进行定时打卡，这样**自己就不需要服务器了，直接白嫖GitHub的”服务器“多香啊！！！**<br>
等项目测试成功，就能通过actions直接定时每天打卡，香的一批<br>
最关键的是，GitHub支持了对密码账户等信息的封装，这样可以**保护使用者的信息安全，不被外泄。**<br>
请等待我的最新成果<br>
懵懂学习尝试ing<br>
**由于一直加载不上浏览器驱动，此版本含泪放弃，但是本地化仍然可以完美运行**  
## 请跳转https://github.com/codeM78/zzu_jksb-daily 完美白嫖GitHub服务器！**



如果用户下载到本地自行使用--请忽略本项目中的private_info.py<br>
需要用户再新建`private_info.py`文件，并在里面设置如下参数：
```
UID = "学号"
PWD = "平台密码"

MAIL_USER = "通知邮箱"
MAIL_PWD = "通知邮箱授权码"
MAIL_TO = "接受通知的邮箱"
```

如果想要做成多账户的，需要通过`User(uid, pwd, email)`来定义并添加到`users`数组中

