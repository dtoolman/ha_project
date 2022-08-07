from xml.dom.xmlbuilder import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

options = webdriver.ChromeOptions()
prefs = {"download.default_directory" : "/some/path"}
options.add_experimental_option("prefs",prefs)
# options.headless = True
driver = webdriver.Chrome(options=options)

driver.get("https://membershipworks.com/admin/#myaccount")

# Save the current URL
current_url = driver.current_url

# Log in to MembershipWorks
email_field = driver.find_element(By.NAME, "eml")
pass_field = driver.find_element(By.NAME, "pwd")
email_field.clear()
email_field.send_keys("breitling.nw@gmail.com")
pass_field.clear()
pass_field.send_keys("THAPassword")
pass_field.send_keys(Keys.RETURN)

# After the URL changes, navigate to the order form
# TODO: Potentially figure out a way to only use the API and not Selenium. As of now, I can't quite figure out authentication though
WebDriverWait(driver, 15).until(EC.url_changes(current_url))
print(driver.get_cookies())
driver.get("https://api.membershipworks.com/v1/csv?SF=Fk8z6IyS8I-STaST9_c2YVwWvrTS4VzFpY7zxYgTAhLisFDfosN9glIkkyUMRn5y&_rt=946706400&frm=618575991ea12250a05d87dd")

time.sleep(2)

driver.quit()