from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

import os




# Set up Chrome WebDriver (you need to download the WebDriver for your specific browser version)
driver = webdriver.Chrome()
# Navigate to LeetCode
driver.get("https://leetcode.com/accounts/login/")

# testing
print(driver.title)

# Log in (replace 'username' and 'password' with your credentials)
username = os.getenv("LEETCODE_USERNAME")
password = os.getenv("LEETCODE_PASSWORD")

time.sleep(5)  # Adjust this wait time as needed
username_input = driver.find_element(by=By.NAME, value="login")
username_input.send_keys(username)

password_input = driver.find_element(by=By.NAME, value="password")
password_input.send_keys(password)
password_input.send_keys(Keys.RETURN)

# Wait for the login process to complete
time.sleep(5)  # Adjust this wait time as needed

# Navigate to the submission page
driver.get("https://leetcode.com/problems/maximum-subarray/description/")
time.sleep(5)


# Resetting the code
reset_button = driver.find_element(by = By.XPATH, value = "/html/body/div[1]/div[2]/div/div/div[4]/div/div/div[8]/div/div[1]/div[2]/button[4]")
reset_button.click()
time.sleep(2)
# confirming the reset
confirm_reset = driver.find_element(by = By.XPATH, value = "/html/body/div[1]/div[2]/div/div/div[4]/div/div/div[8]/div/div[1]/div[2]/div/div/div/div[2]/div/div[2]/div/div/div[2]/button")
confirm_reset.click()
time.sleep(2)

# Submit the code
submit_button = driver.find_element(by = By.XPATH, value = "/html/body/div[1]/div[2]/div/div/div[3]/div/div/div[1]/div/div/div[2]/div/div[2]/div/div[3]/div[3]/div/button")
submit_button.click()

# Wait for the submit process to complete
time.sleep(10)  # Adjust this wait time as needed

# Close the browser
driver.close()
