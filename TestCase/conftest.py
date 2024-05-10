import datetime
import os
import time


import pytest
import pytest_html
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

driver = None
@pytest.fixture()
def driver(request):
    global driver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    time.sleep(3)
    driver.maximize_window()
    # yield driver
    # driver.quit()

    return driver


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == "call" or report.when=="setup":
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

             # Define the filename with the timestamp
            filename = f"screenshot_{timestamp}.png"

            # Define the full path of the screenshot file
            file = os.path.join("C:/Users/sawal/PycharmProjects/BYWMS/Screenshots",filename)
            driver.get_screenshot_as_file(file)


            extra_html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                         'onclick="window.open(this.src)" align="right"/></div>' % file
            extra.append(pytest_html.extras.html(extra_html))

        report.extras =extra















#########################################accurate code

# import datetime
# import os
# import time
#
#
# import pytest
# import pytest_html
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service as ChromeService
#
# @pytest.fixture(scope='class',autouse=True)
# def driver(request):
#     global driver
#     driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#     time.sleep(3)
#     driver.maximize_window()
#     # yield driver
#     # driver.quit()
#
#     return driver


# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item):
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, 'extra', [])
#     if report.when == "call" or report.when=="setup":
#         xfail = hasattr(report, "wasxfail")
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
#
#              # Define the filename with the timestamp
#             filename = f"screenshot_{timestamp}.png"
#
#             # Define the full path of the screenshot file
#             file = os.path.join("C:/Users/sawal/PycharmProjects/BYWMS/Screenshots",filename)
#             driver.get_screenshot_as_file(file)
#
#
#             extra_html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
#                          'onclick="window.open(this.src)" align="right"/></div>' % file
#             extra.append(pytest_html.extras.html(extra_html))
#
#         report.extras =extra
