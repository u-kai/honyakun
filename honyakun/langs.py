"""_summary_

    lang is follow below
        ja
        en
        cn
"""


class Langs():
    def __init__(self, lang: str) -> None:
        self.value = lang

    def is_ja(self) -> bool:
        return self.value == "ja"

    def is_cn(self) -> bool:
        return self.value == "cn"

    def is_en(self) -> bool:
        return self.value == "en"

    def lang(self) -> str:
        if self.is_ja() or self.is_cn() or self.is_en():
            return self.value
        raise RuntimeError
