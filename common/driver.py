import logging
import time
import os
import poco
import subprocess
import pysnooper
from poco.drivers.std import StdPoco
from airtest.core.api import connect_device
from common.logMethod import log, Testlog

# connect a device first, then initialize poco object
# drvier = connect_device('Android:nz6tobmzmvs4c689')
# poco = StdPoco(10054, drvier)
#
# drvier.install_app(r'C:\Users\hkcmn5\Desktop\测试服\测试服-自动化包\TestTP_auto.apk')
# drvier.start_app('com.szbt.tkpine.yy')



# 设置日志等级，用于过滤掉airtest的日志
# import logging
# logger = logging.getLogger("airtest")
# logger.setLevel(logging.ERROR)

class App_key(object):
    '''
    封装类：ADB操作+Airtest的设备实例+Poco的元素常用操作
    '''
    def __init__(self):
        '''
        :param device_name:设备名  【设备名通过adb devices获取】
        '''
        self.driver = connect_device('Android:')
    # 获取设备信息
    def get_devices(self):
        '''获取设备信息'''
        device_list = subprocess.run(f"adb devices", shell=True,
                                     stdout=subprocess.PIPE).stdout.decode()  # subprocess模块:用于在子进程中执行系统命令。
        index = device_list.index("List of devices attached")  # index：统计字符串的索引
        devices_info = device_list[index + len("List of devices attached"):].strip()  # strip：去除字符
        devices_data = devices_info.split()  # split：切割，返回的是list
        devices = []  # 创建空列表，用来存放数据
        for i in range(0, len(devices_data), 2):  #range：可创建一个整数列表
            # 列表嵌套字典
            device = {
                "serial number": devices_data[i],
                "connection status": devices_data[i + 1]
            }
            devices.append(device)  # append：在尾部增加
        for device in devices:
            # print(f"识别的设备号为：{device['serial number']}     连接状态：{device['connection status']}")
            log.info(f"识别的设备号为：{device['serial number']} ，连接状态：{device['connection status']}")

    # 初始化Poco (需要游戏启动后才可以初始化）
    def poco_start(self):
        '''在游戏启动后初始化Poco'''
        time.sleep(7)
        self.poco = StdPoco(15004, self.driver)

    # 安装APK
    def install_app(self, apk_path):
        '''
        安装APP
        :param apk_path: 安装包的路径  【写路径需要前面加 r进行转义】
        '''
        self.driver.install_app(apk_path)

    # 打开APP
    def open_app(self, package_name):
        '''
        打开APP
        :param package_name:  包名   【包名以com开头】
        '''
        self.driver.start_app(package_name)

    #清除APP数据
    def clear_app(self,package_name):
        '''
        清理APP的缓存
        :param package_name: 包名   【包名以com开头】
        :return:
        '''
        self.driver.clear_app(package_name)
        return

    # 寻找元素
    def find_element(self, element):
        ele = self.poco(element)
        try:
            ele.exists()
            log.info(f"定位到元素：{ele}".replace("UIObjectProxy of ",""))#replace:字符串的替换
        except Exception as e:
            log.error(f"无法定位到元素：{ele}".replace("UIObjectProxy of ",""))
        return ele

    # 点击元素
    def click(self,ele=None):
        if self.poco(ele).exists():
            try:
                self.poco(ele).wait(3).click()
                log.info(f"点击元素：{ele}".replace("UIObjectProxy of ",""))
            except Exception as e:
                log.error(f"点击元素：{ele}失败".replace("UIObjectProxy of ",""))
        else:
            try:
                self.poco(ele).wait(3).click()
            except Exception as e:
                log.error(f"元素：{ele}无法定位".replace("UIObjectProxy of ",""))
            finally:
                self.poco(ele).wait(3).click()
                log.info(f"点击元素：{ele}".replace("UIObjectProxy of ",""))



# App = App_key()
# App.get_devices()
# App.install_app(r"D:\TPauto\util\TestTP_auto.apk")
# os.system("adb -s nz6tobmzmvs4c689 shell pm clear com.szbt.tkpine.yy")
# App.clear_app(package_name='com.szbt.tkpine.yy')
# App.open_app(package_name='com.szbt.tkpine.yy')
# App.poco_start()
# App.find_element("btn_guest").click()
# App.click("btn_close")
# App.click("btn_close")
# App.click("close")
# App.click("btn_userinfo")
