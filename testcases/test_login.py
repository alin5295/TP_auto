import os
import time

import pytest
import yaml
from airtest.core.api import connect_device

from common.driver import App_key
from common.logMethod import Testlog
from common.read_data import read_yaml

TP=App_key()#实例化App_key
log=Testlog(logname="印度03项目").Get_log()#用例的日志输出
d=read_yaml(file_path=r"data/Loginpage.yaml")#读取yaml的测试文件



@pytest.mark.parametrize("data",d)
def test_Login(data):
    TP.clear_app(package_name='com.szbt.tkpine.yy')
    TP.open_app('com.szbt.tkpine.yy')
    TP.poco_start()
    TP.find_element(data["guest"]).click()
    log.info("游客登录成功")
    time.sleep(3)
    # log.info("===正在清理数据缓存====")
    # TP.clear_app(package_name='com.szbt.tkpine.yy')
    # TP.open_app('com.szbt.tkpine.yy')
    # TP.poco_start()
    # TP.find_element(data["username_btn"]).click()
    # time.sleep(5)
    # TP.find_element(data["9_btn"]).click()
    # TP.find_element(data["5_btn"]).click()
    # TP.find_element(data["2_btn"]).click()
    # TP.find_element(data["9_btn"]).click()
    # TP.find_element(data["5_btn"]).click()
    # TP.find_element(data["5_btn"]).click()
    # TP.find_element(data["2_btn"]).click()
    # TP.find_element(data["9_btn"]).click()
    # TP.find_element(data["9_btn"]).click()
    # TP.find_element(data["9_btn"]).click()
    # TP.find_element(data["phonelogin_btn"]).click()
    # TP.find_element(data["otp_btn"]).click()
    # time.sleep(3)
    # TP.find_element(data["password_btn"]).click()
    # TP.find_element(data["1_btn"]).click()
    # TP.find_element(data["2_btn"]).click()
    # TP.find_element(data["3_btn"]).click()
    # TP.find_element(data["4_btn"]).click()
    # TP.find_element(data["5_btn"]).click()
    # TP.find_element(data["6_btn"]).click()
    # time.sleep(3)
    # TP.find_element(data["phonelogin_btn"]).click()
