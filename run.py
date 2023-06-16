import pytest
import os
import logging

if __name__ == '__main__':
    pytest.main(["-vs","testcases/test_login.py"])#"--alluredir","./allure-result"
    # os.system("allure generate ./allure-result -o ./reports --clean")
    # logging.shutdown()
