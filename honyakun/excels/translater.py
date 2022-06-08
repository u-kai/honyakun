from honyakun.excels.wrapper import ExcelWrapper
from honyakun.g_translater import GTranslater
from honyakun.langs import Langs


class ExcelTranslater():
    def __init__(self, filename: str, sheet_name: str, from_lang: Langs, to_lang: Langs) -> None:
        self.excel = ExcelWrapper(filename, sheet_name)
        self.to_lang = to_lang
        self.from_lang = from_lang
        self.g_translate = GTranslater(self.from_lang, self.to_lang)

    def translate_column(self, from_column: str, to_column: str, start: int, end: int) -> None:
        texts = self.excel.read_column_texts(from_column, start, end)
        translates = []
        for text in texts:
            if text is None:
                translates.append(None)
                continue
            translate = self.g_translate.translate(text)
            print(translate)
            translates.append(translate)
        self.excel.write_column_texts(to_column, start, translates)
        self.excel.save()
        return

    def change_lang(self, from_lang: Langs, to_lang: Langs) -> None:
        self.from_lang = from_lang
        self.to_lang = to_lang
        self.g_translate = GTranslater(self.from_lang, self.to_lang)
        return

    def change_sheet(self, sheet_name: str) -> None:
        self.excel.change_sheet(sheet_name)
        return

    def check(self, from_column: str, start: int, end: int) -> None:
        print(self.excel.read_column_texts(from_column, start, end))
