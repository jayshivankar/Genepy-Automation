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
    driver.execute_script("window.scrollBy(0,4000)")  # Scroll down by 80 pixels
    time.sleep(0.5)  # Wait for 0.5 seconds
    if stop_scrolling > 1:  # Stop after 40 scrolls (~4000 pixels)
        break

time.sleep(3)

# solve exception problem
exceptions_problem = driver.find_element(By.XPATH,value='//*[@id="exercises"]/main/table/tbody/tr[37]/td[4]')
exceptions_problem.click()
time.sleep(10)
# Locate the div containing the elements
div_element=driver.find_element(By.XPATH,value='//*[@id="instructions"]')

# Extract text from paragraph and heading tags inside the div
content=[]
for tags in ["p"]:
    elements=div_element.find_elements(By.TAG_NAME,tags)
    for elem in elements:
        content.append(elem.text)
text_content = "\n".join(content)


# Create and configure the Chrome webdriver for chatgpt
driver_2 = webdriver.Chrome(options=chrome_options)
driver_2.maximize_window()
# open chatgpt
driver_2.get("https://chatgpt.com/")
time.sleep(3)
question1_paste=driver_2.find_element(By.XPATH,value='//*[@id="prompt-textarea"]/p')
question1_paste.send_keys(text_content)
time.sleep(3)
enter_key=driver_2.find_element(By.XPATH,value='//*[@id="composer-background"]/div[2]/div[2]')
enter_key.click()