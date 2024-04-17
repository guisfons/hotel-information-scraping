import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from openpyxl import Workbook

driver = webdriver.Chrome()
driver.get('https://www.booking.com/')

close_popup = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@class="b9720ed41e cdf0a9297c"]'))
)
driver.execute_script("arguments[0].parentNode.removeChild(arguments[0]);", close_popup)

location = input("Type the desired location: ")

location_input = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id=":re:"]'))
)
location_input.click()
location_input.send_keys(location)

time.sleep(1)

search_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@class="a83ed08757 c21c56c305 a4c1805887 f671049264 d2529514af c082d89982 cceeb8986b"]'))
)
search_button.click()

close_calendar = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="b2searchresultsPage"]/div[3]/div/div/header'))
)
close_calendar.click()

hotel_titles = driver.find_elements(By.CSS_SELECTOR, '[data-testid="title"]')
hotels_info_array = []

if hotel_titles:
    # Iterate over the found elements
    for hotel_title in hotel_titles:
        hotel_info = {'title': hotel_title.text, 'email': '', 'telephone': ''}
        hotels_info_array.append(hotel_info)
        time.sleep(1)
else:
    print('No hotel titles found.')

wb = Workbook()
ws = wb.active

headers = ['Hotel Title', 'Email', 'Telephone']
ws.append(headers)

# Write the titles into the Excel file
for hotel in hotels_info_array:
    row = [hotel.get('title', ''), hotel.get('email', ''), hotel.get('telephone', '')]
    ws.append(row)

# Save the Excel file
wb.save('./docs/'+location+'_hotel_titles.xlsx')

# time.sleep(25)