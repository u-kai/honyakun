from honyakun.driver import Driver
from honyakun.langs import Langs


class GTranslater():
    def __init__(self, from_lang: Langs, to_lang: Langs, option="--headless") -> None:
        self.driver = Driver(option=option)
        self.page_detail = GTranslatePageDetail()
        self.url = f"{self.page_detail.url}/#{self.__convert_lang(from_lang)}/{self.__convert_lang(to_lang)}"

    def translate(self, word: str) -> str:
        self.driver.set_page(f"{self.url}/{word}")
        selector = self.page_detail.translate_result_selector
        result = self.driver.get_element_by_css_selector(selector.element, selector.property, selector.property_value)
        return result.text

    def __convert_lang(self, lang: Langs) -> str:
        if lang.is_cn():
            return "zh-CN"
        return lang.lang()


class GTranslatePageDetail():
    def __init__(self) -> None:
        self.url = "https://translate.google.co.jp"
        self.translate_result_selector = Selector("span", "jsname", "W297wb")


class Selector():
    def __init__(self, element: str, property: str, property_value: str) -> None:
        self.element = element
        self.property = property
        self.property_value = property_value
