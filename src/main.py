from time import sleep

import bs4
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent

PATH_GOOGLE_CHROME = '/app/.apt/usr/bin/google-chrome'
PATH_CHROMEDRIVER = '/app/.chromedriver/bin/chromedriver'

# PATH_GOOGLE_CHROME = 'C:\Program Files (x86)\Google\Chrome\Application'
# PATH_CHROMEDRIVER = 'D:\\chromedriver'


def search(keywords):
    chrome_options = Options()
    chrome_options.headless = True
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument("--disable-extensions")

    ua = UserAgent()
    userAgent = ua.random
    print(f'{userAgent = }')
    chrome_options.add_argument(f'user-agent={userAgent}')

    driver = webdriver.Chrome(
        executable_path=PATH_CHROMEDRIVER,
        options=chrome_options
    )

    # driver.get('https://bankrot.fedresurs.ru/TradeList.aspx')
    driver.get('https://www.google.ru')
    print(driver.page_source)

    region_option = driver.find_element_by_xpath(
        '//select[@id="ctl00_cphBody_ucRegion_ddlBoundList"]'
        '/option[text()="Московская область"]'
    )
    region_option.click()

    keywords_option = driver.find_element_by_xpath(
        '//input[@id="ctl00_cphBody_tbTradeObject"]'
    )
    keywords_option.send_keys(keywords)

    search_button = driver.find_element_by_xpath(
        '//input[@id="ctl00_cphBody_btnTradeSearch"]'
    )
    search_button.click()
    sleep(1)

    bs = bs4.BeautifulSoup(driver.page_source, features='html.parser')
    trade_list = bs.find('table', id='ctl00_cphBody_gvTradeList')

    for trade in trade_list.find_all('tr')[1:]:
        trade_row = trade.find_all('td')
        if len(trade_row) > 5:
            trade_type_td: bs4.element.Tag = trade_row[5]
            if len(trade_type_td) > 1:
                link_a: bs4.element.Tag = trade_type_td.contents[1]
                href: str = link_a.get('href')
                if href:
                    id = href[href.index('=') + 1:]
                    print(id)

    driver.quit()


def main():
    for i in range(1):
        keywords = chr(ord('а') + i // 33) + chr(ord('а') + i % 33)
        search(keywords)
        print('-----------------------')


if __name__ == '__main__':
    main()
