import csv
import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv

load_dotenv()

username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")




#writer = csv.writer(open(parameters.result_file, 'w'))
#writer.writerow(['name', 'job_title', 'schools', 'location', 'ln_url'])

driver = webdriver.Chrome()
driver.get('https://www.linkedin.com')
sleep(5)

driver.find_element(By.LINK_TEXT, "Sign in").click()
sleep(3)

username_input = driver.find_element(By.NAME,'session_key')
username_input.send_keys(username)
sleep(0.5)


password_input = driver.find_element(By.NAME,'session_password')
password_input.send_keys(password)
sleep(0.5)

# click on the sign in button

driver.find_element(By.XPATH, "//button[text()='Sign in']").click()


sleep(5)

search_query = 'coach'
search_input = driver.find_element(By.NAME,'q')
search_input.send_keys(search_query)
sleep(1)


search_input.send_keys(Keys.RETURN)
sleep(3)



driver.quit()



