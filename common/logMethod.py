import logging
import ctypes

FOREGROUND_WHITE = 0x0007
FOREGROUND_BLUE = 0x01 # text color contains blue.
FOREGROUND_GREEN= 0x02 # text color contains green.
FOREGROUND_RED = 0x04 # text color contains red.
FOREGROUND_YELLOW = FOREGROUND_RED | FOREGROUND_GREEN
STD_OUTPUT_HANDLE= -11
std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
def set_color(color, handle=std_out_handle):
 bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
 return bool

class Testlog:
    def __init__(self,logname):  #构造方法，初始化自动调用
        """
        创建日志器
        """
        self.log=logging.getLogger(logname)


    def console_log(self):
        """
        控制台处理器
        """
        self.console_handler=logging.StreamHandler()
        self.console_handler.setFormatter(self.Get_formatter()[0])
        return self.console_handler

    def file_log(self):
        """
        文件处理器
        """
        self.file_handler=logging.FileHandler("logs/TP_log.txt", mode="w", encoding="utf-8")#"../logs/TP_log.txt"
        self.file_handler.setFormatter(self.Get_formatter()[1])  #类中间调用方法
        self.file_handler.close() #代码块执后行自动关闭log文件
        return self.file_handler

    def Get_formatter(self):
        """
        处理器打印的格式
        """
        self.console_fmt = logging.Formatter(fmt="【%(levelname)s】 %(asctime)s 【%(name)s】--%(filename)s--第%(lineno)d行:%(message)s")
        self.file_fmt = logging.Formatter(fmt="【%(levelname)s】 %(asctime)s--【%(name)s】--%(filename)s--第%(lineno)d行--%(message)s")
        return self.console_fmt,self.file_fmt  #返回的是元组，通过索引取值实现两个处理器的打印个事

    def Get_log(self):
        """
        日志器添加处理器
        """
        self.log.addHandler(self.file_log())
        self.log.addHandler(self.console_log())
        self.log.setLevel(logging.INFO)  # 设置日志级别为 INFO
        return self.log


log=Testlog(logname="印度03项目").Get_log()
