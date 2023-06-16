import os

import pytest
import yaml
from airtest.core.api import connect_device

from common.driver import App_key
from common.logMethod import Testlog

# print(d)    #[{'guest_btn': 'btn_guest'}]


f=open(r"data/Loginpage.yaml",encoding="UTF-8",)     #../data/Loginpage.yaml
d=yaml.safe_load(f)

TP=App_key()
log=Testlog(logname="印度03项目").Get_log()



@pytest.mark.parametrize("data",d)
def test_Login(data):
    TP.clear_app(package_name='com.szbt.tkpine.yy')
    TP.open_app('com.szbt.tkpine.yy')
    TP.poco_start()
    TP.click(data["guest_btn"])
    log.info("游客登录成功")



