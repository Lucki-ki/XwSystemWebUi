import os

import pytest

if __name__ == '__main__':
    pytest.main(['-k', 'test_new_sate', '-s', '-q', '--alluredir', '../allure_result'])
    os.system('allure generate ./allure_result -o ../report --clean')