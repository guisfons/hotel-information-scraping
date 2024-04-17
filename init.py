import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.booking.com/")

close_popup = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@class="b9720ed41e cdf0a9297c"]'))
)
driver.execute_script("arguments[0].parentNode.removeChild(arguments[0]);", close_popup)

location_input = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id=":re:"]'))
)
location_input.click()

time.sleep(25)