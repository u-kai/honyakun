# Honyakun


## ExcelTranslater
### How use
```python
from honyakun.excels.translater import ExcelTranslater
from honyakun.langs import Langs

e = ExcelTranslater("test.xlsx", "term1", Langs("jp"), Langs("en"))
e.translate_column("E", "F", 4, 30)
e.check("H", 4, 20)
```
- above code is open test.xlsx and translate term1.E4\~E30 and change term1.F4\~F30 use result of translate  
- where term1 is sheet name

## GTranslater

### How use

```python
from honyakun.g_translater import GTranslater
from honyakun.langs import Langs

g = GTranslater(Langs("en"), Langs("cn"))
result = g.translate("hello")
print(result)

```

- above code's result to be "你好"