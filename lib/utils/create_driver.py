import pytest
from selenium.webdriver import Chrome
def get_browser_instane():
    browser=pytest.config.option.browser.lower()
    url=pytest.config.option.url.lower()
    if browser=='chrome':
        driver=Chrome("//Users//mtimmappa//PycharmProjects//qspidernew//chromedriver")
    elif browser=="firefox":
        pass
    elif browser=="ie":
        pass
    else:
        pytest.fail("---!!!!!invalid browser option!!!!!----")

    driver.maximize_window()
    driver.implicitly_wait(30)
    if url == 'prod':
        driver.get("https://www.intellicare--web")
    else:
        driver.get("https://intellicare-web.tegile.com/Zebi-AS/app/index.html")
    return driver

