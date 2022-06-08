from honyakun.excels.translater import ExcelTranslater
from honyakun.langs import Langs


e = ExcelTranslater("test.xlsx", "term1", Langs("jp"), Langs("en"))

e.translate_column("E", "F", 4, 5)
e.change_lang(Langs("en"), Langs("cn"))
e.translate_column("F", "G", 4, 5)
e.check("H", 4, 20)
