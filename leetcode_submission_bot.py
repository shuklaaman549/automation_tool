from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument('--headless')  # Run Chrome in headless mode
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--window-size=1920,1080')
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")

# Set up Chrome WebDriver
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(10)  # Implicit wait for elements to load

# Navigate to LeetCode
driver.get("https://leetcode.com/accounts/login/")

# Testing
print(driver.title)

# Log in (replace 'username' and 'password' with your credentials)
username = os.getenv("LEETCODE_USERNAME")
password = os.getenv("LEETCODE_PASSWORD")

# Wait for the username input field to be present
username_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "login"))
)
username_input.send_keys(username)

# Wait for the password input field to be present
password_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "password"))
)
password_input.send_keys(password)
password_input.send_keys(Keys.RETURN)

# Wait for the login process to complete
time.sleep(5)

# Navigate to the submission page
driver.get("https://leetcode.com/problems/maximum-subarray/description/")
time.sleep(5)

# Resetting the code
reset_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div/div/div[4]/div/div/div[8]/div/div[1]/div[2]/button[4]"))
)
reset_button.click()

# Confirming the reset
confirm_reset = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div/div/div[4]/div/div/div[8]/div/div[1]/div[2]/div/div/div/div[2]/div/div[2]/div/div/div[2]/button"))
)
confirm_reset.click()

# Submit the code
submit_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div/div/div[3]/div/div/div[1]/div/div/div[2]/div/div[2]/div/div[3]/div[3]/div/button"))
)
submit_button.click()

# Wait for the submit process to complete
time.sleep(10)

# Take a screenshot for debugging
driver.save_screenshot('screenshot.png')

# Close the browser
driver.close()
