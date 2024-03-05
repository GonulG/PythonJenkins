from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://useinsider.com/")

logo_element= driver.find_element(By.CSS_SELECTOR,'.navbar-brand')
print("LOGONUN HREF'İ BUDUR: " + logo_element.get_attribute('href'))

why_insider_link= driver.find_element(By.XPATH, '//a[contains(text(),"Why Insider")]')
print("LINK HREF BUDUR: " + why_insider_link.get_attribute('href'))


current_url = driver.current_url

if "google.com" in current_url:
    print("Test Başarılı, Google ana sayfasına gidildi")

else:
    print("Test Başarısız. Beklenen URL 'google.com' ancak Alınan URL : "  f'{current_url}')

driver.quit()

