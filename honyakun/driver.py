from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


def driver(option="--headless"):
    options = Options()
    options.add_argument(option)
    driver = webdriver.Chrome(executable_path=ChromeDriverManager.install(), chrome_options=options)
    return driver
