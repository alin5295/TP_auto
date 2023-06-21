import logging

import pytest
import os

from common.read_data import read_yaml

if __name__ == '__main__':
    pytest.main(["-vs","testcases/test_login.py","--alluredir","./allure-result","--clean-alluredir"])#,"--alluredir","./allure-result"
    os.system("allure generate ./allure-result -o ./test_report --clean")
    logging.shutdown()
