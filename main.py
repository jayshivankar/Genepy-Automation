from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


ACCOUNT_EMAIL="jayyyy_5678"
ACCOUNT_PASSWORD="jay@135790"


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Create and configure the Chrome webdriver
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

# Navigate to genepy
driver.get("https://genepy.org/exercises/")
time.sleep(2)

# first sign in
sign_in_1= driver.find_element(By.XPATH,value='//*[@id="exercises"]/header/nav/ul/li[5]/a')
sign_in_1.click()
time.sleep(2)

# fill in username and password
username=driver.find_element(By.XPATH,value='//*[@id="id_username"]')
password=driver.find_element(By.XPATH,value='//*[@id="id_password"]')
username.send_keys(ACCOUNT_EMAIL)
password.send_keys(ACCOUNT_PASSWORD)
time.sleep(2)

# final sign in
sign_in_2=driver.find_element(By.XPATH,value='//*[@id="auth_login"]/main/form/button')
sign_in_2.click()


stop_scrolling = 0
while True:
    stop_scrolling += 1
    driver.execute_script("window.scrollBy(0,40)")  # Scroll down by 40 pixels
    time.sleep(0.5)  # Wait for 0.5 seconds
    if stop_scrolling > 80:  # Stop after 120 scrolls (~4800 pixels)
        break

time.sleep(3)