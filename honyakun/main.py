from honyakun.g_translater import GTranslater
from honyakun.langs import Langs


g = GTranslater(Langs("en"), Langs("cn"))
result = g.translate("hello")
print(result)
