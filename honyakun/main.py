from honyakun.driver import Driver

driver = Driver()
driver.set_page("https://translate.google.co.jp/", "#en/ja/hello")
#result = driver.get_element_by_css_selector("span", "class", "Q4iAWc")
result = driver.get_element_by_class("Q4iAWc")

print(result.text)
