#מוצא את שער הדולר העדכני
import time
from selenium import webdriver
browser = webdriver.Chrome()
browser.get('https://www.boi.org.il/he/markets/exchangerates/pages/default.aspx')
text = browser.find_element_by_css_selector('#BoiCurrencyExchangeRatesTab > table.BoiExchangeRateSearchTable.ng-table.responsive > tbody > tr:nth-child(2) > td.small-padding.tdno3 > div.tableTRText').text
print(text)
#IDX
browser.get('https://terminal.id-x.co.il/#/')
elem = browser.find_element_by_css_selector('#root > div > button').click()
time.sleep(5)
browser.find_element_by_css_selector('#email').send_keys('petafemto')