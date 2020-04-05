from selenium import webdriver
import bs4


CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('headless')

chrome_options.binary_location = 'heroku: /app/.apt/usr/bin/google-chrome'
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)
driver = webdriver.Chrome('D:/chromedriver.exe', options=chrome_options)


text = '''
Вы можете предлагать свои подборки с музыкой, главное, чтобы они были в рамках приличия (не содержали откровенную нецензурную брань и ругательства, не нарушали правил сообщества и игры), а также использовались качественные скриншоты или арты по TERA.
'''

driver.get(f"https://translate.yandex.ru/?lang=ru-en&text={text}")

# if len(text) > 100:
#     driver.get(f"https://translate.yandex.ru/?lang=en-ru&text={text}")
# else:
#     driver.get(f"https://translate.yandex.ru/?lang=en-ru")
#     input_area = driver.find_element_by_id('fakeArea')
#     input_area.send_keys(text)


result = ''
for i in range(100):
    bs = bs4.BeautifulSoup(driver.page_source, features='lxml')
    translate: bs4.element.Tag = bs.find('span', attrs={'data-complaint-type': 'fullTextTranslation'})
    if translate:
        children = translate.children
        if children:
            for word in children:
                result += word.text
            print(result)
            break



