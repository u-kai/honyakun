import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium import webdriver, common


class Driver:
    def __init__(self, option="--headless") -> None:
        options = Options()
        options.add_argument(option)
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=options)

    def set_page(self, url: str):
        self.driver.get(url)
        time.sleep(3)

    def get_page(self):
        return self.driver.page_source

    def get_element_by_css_selector(self, element: str, property_name: str, property_value: str):
        try:
            result = self.driver.find_element_by_css_selector(f"{element}[{property_name}='{property_value}']")
        except common.exceptions.NoSuchElementException as e:
            print(e)
            print("retry after 1sec...")
            time.sleep(1)
            result = self.driver.find_element_by_css_selector(f"{element}[{property_name}='{property_value}']")

        return result

    def get_element_by_class(self, class_value: str):
        try:
            result = self.driver.find_element_by_class_name(class_value)
        except common.exceptions.NoSuchElementException as e:
            print(e)
            print("retry after 1sec...")
            time.sleep(1)
            result = self.driver.find_element_by_class_name(class_value)

        return result
