import time
from airtest.core.api import *
from poco.drivers.std import StdPoco
from airtest.report.report import simple_report,LogToHtml
import os


'''
前置条件：连接设备，初始化Airtest
'''

__author__ = "user"
import logging
logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)
#连接设备
driver = connect_device('Android:nz6tobmzmvs4c689')
auto_setup(basedir=r"D:\TPauto\logs\Airtest_result",logdir=True, devices=["Android:nz6tobmzmvs4c689"])
# simple_report(filepath=r".\Poco_Demo.py",logpath=True,logfile=r"\test_report\log.txt",output=r"..\test_report\log.html")



driver.install_app(r'C:\Users\hkcmn5\Desktop\测试服\测试服-自动化包（Poco)\TestTP_auto.apk')#安装接入poco-SDK的APK
os.system("adb shell pm clear com.szbt.tkpine.yy")
driver.start_app('com.szbt.tkpine.yy')

time.sleep(15) #等待UI控件加载出来
poco = StdPoco(15004, driver)#初始化poco
poco("btn_guest").click()#点击游客登录
# poco("btn_close").click()#关闭弹窗1
# # poco("btn_close").click()#关闭弹窗2
# # poco("btn_close").click()#关闭弹窗3
# poco("txt_id").click()#点击个人信息
# poco("btn_close").click()#关闭弹窗2


'''
后置条件：生成测试报告
'''
#生成测试报告
simple_report(filepath=r"Poco_Demo.py", logpath=True, output=r"logs\Airtest_result\log\test.html")

