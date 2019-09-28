#מוצא את שער הדולר העדכני
from selenium import webdriver
browser = webdriver.Chrome()
browser.get('https://www.boi.org.il/he/markets/exchangerates/pages/default.aspx')
text = browser.find_element_by_css_selector('#BoiCurrencyExchangeRatesTab > table.BoiExchangeRateSearchTable.ng-table.responsive > tbody > tr:nth-child(2) > td.small-padding.tdno3 > div.tableTRText').text
print(text)