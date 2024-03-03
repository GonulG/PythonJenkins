import selenium

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.google.com")

textarea = driver.find_element(By.CLASS_NAME, "gLFyf")
textarea.send_keys("Insider")
textarea.send_keys(Keys.ENTER)

current_url = driver.current_url

if "google.com" in current_url:
    print("Test Başarılı")

else:
    print("Test Başarısız")
