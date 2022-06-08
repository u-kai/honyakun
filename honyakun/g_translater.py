from honyakun.driver import Driver
from honyakun.langs import Langs


class GTranslater():
    def __init__(self, from_lang: Langs, to_lang: Langs, option="--headless") -> None:
        self.driver = Driver(option=option)
        self.url = f"https://translate.google.co.jp/#{self.__convert_lang(from_lang)}/{self.__convert_lang(to_lang)}"

    def translate(self, word: str) -> str:
        self.driver.set_page(f"{self.url}/{word}")
        result = self.driver.get_element_by_css_selector("span", "jsname", "W297wb")
        return result.text

    def __convert_lang(self, lang: Langs) -> str:
        if lang.is_cn():
            return "zh-CN"
        return lang.lang()
