from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
import time

load_dotenv()

driver = webdriver.Chrome()

driver.get("https://webapp4.asu.edu/myasu/?action=addclass&strm=2227")

username_field = driver.find_element(By.NAME, "username")
password_field = driver.find_element(By.NAME, "password")
submit_button = driver.find_element(By.NAME, "submit")

username = os.environ.get("username")
password = os.environ.get("password")

username_field.send_keys(username)
password_field.send_keys(password)

submit_button.click()

# time for authentication
time.sleep(20)

shopping_cart_item = driver.find_element(By.ID, "win2divSCC_LO_FL_WRK_SCC_GROUP_BOX_1$0")

shopping_cart_item.click()

time.sleep(2)

semester = driver.find_element(By.ID, "GRID_TERM_SRC5$0_row_0")

semester.click()

time.sleep(3)

checkboxes = driver.find_elements(By.CLASS_NAME, "ps-checkbox")
enroll_button = driver.find_element(By.ID, "DERIVED_SSR_FL_SSR_ENROLL_FL")

for idx, checkbox in enumerate(checkboxes):
  checkboxes = driver.find_elements(By.CLASS_NAME, "ps-checkbox")
  enroll_button = driver.find_element(By.ID, "DERIVED_SSR_FL_SSR_ENROLL_FL")
  to_click = checkboxes.copy()
  to_click.remove(checkboxes[idx])

  for click_checkbox in to_click:
    click_checkbox.click()

  enroll_button.click()

  time.sleep(2)

  driver.find_element(By.ID, "#ICYes").click()

  time.sleep(5)

  # go back to the shopping cart page
  shopping_cart_item = driver.find_element(By.ID, "win2divSCC_LO_FL_WRK_SCC_GROUP_BOX_1$0")
  shopping_cart_item.click()
  time.sleep(2)
