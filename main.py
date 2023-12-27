import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")

option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)

# Open a specific profile
option.add_argument(r"--user-data-dir=C:\Users\ASUS\AppData\Local\Google\Chrome\User Data")
option.add_argument(r"--profile-directory=Default")

driver = webdriver.Chrome(options=option)
driver.get("https://tinder.com/app/recs")
time.sleep(2)

click_script = "arguments[0].click()"

try:
    cookie = driver.find_element(By.XPATH, '//*[@id="q-637390230"]/div/div[2]/div/div/div[1]/div[1]/button')
    driver.execute_script(click_script, cookie)
    print("Allowed cookies...\n")
    time.sleep(3)
except selenium.common.exceptions.NoSuchElementException:
    print("cookie not needed...\n")

login = driver.find_element(By.LINK_TEXT, "Log in")
driver.execute_script(click_script, login)
time.sleep(3)

# options are in another frame
driver.switch_to.frame(0)
print("Frame switched...\n")

# Login with Google
ggl_btn = driver.find_element(By.XPATH, '//*[@id="container"]/div')
driver.execute_script(click_script, ggl_btn)
print("Logging in with Google...\n")

# For log in using Facebook
# try:
#     more_opt = driver.find_element(By.XPATH,
#                                    '//*[@id="q1929195990"]/main/div/div/div[1]/div/div/div[2]/div[2]/span/button')
#     driver.execute_script(click_script, more_opt)
# except selenium.common.exceptions.NoSuchElementException:
#     print("more option are already there...\n")

# Login with facebook if google account not linked with chrome
# fb_btn = driver.find_element(By.XPATH, '//*[@id="q1929195990"]/main/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]')
# driver.execute_script(click_script, fb_btn)

# switch to main frame
driver.switch_to.default_content()
print("Back to default content...\n")
time.sleep(3)

main_window = driver.window_handles[0]
popup_window = driver.window_handles[1]
driver.switch_to.window(popup_window)
print(f"Switched to {driver.title}\n")

acnt_btn = driver.find_element(By.XPATH, '//*[@id="credentials-picker"]/div[1]')
driver.execute_script(click_script, acnt_btn)
print("Logged in with Google\n")

# To log in with facebook ---
# input_email = driver.find_element(By.ID, "email")
# input_pass = driver.find_element(By.ID, "pass")
#
# input_email.send_keys(EMAIL)
# input_pass.send_keys(PASSWORD)
# input_pass.send_keys(Keys.ENTER)

try:
    driver.switch_to.window(main_window)
    print(f"Switched to {driver.title}\n")
except selenium.common.exceptions.NoSuchWindowException:
    print(f"Switched to {driver.title}\n")

time.sleep(3)

try:
    allow_location = driver.find_element(By.XPATH, '//*[@id="q1929195990"]/main/div/div/div/div[3]/button[1]')
    driver.execute_script(click_script, allow_location)
    input("Please allow location in chrome popup... Then press ENTER")
    print("Allowed Location...\n")
except selenium.common.exceptions.NoSuchElementException:
    print("Location Permission already given\n")
time.sleep(2)


try:
    allow_notification = driver.find_element(By.XPATH, '//*[@id="q1929195990"]/main/div/div/div/div[3]/button[1]')
    driver.execute_script(click_script, allow_notification)
    input("Please allow notification in chrome popup... Then press ENTER")
    print("Allowed Notification...\n")
except selenium.common.exceptions.NoSuchElementException:
    print("Notification Permission already given\n")
time.sleep(5)

print(driver.title)
driver.switch_to.default_content()
print("Starting MisMatching...\n")

i = 3
while i != 0:
    buttons = driver.find_elements(By.CLASS_NAME, "button ")
    driver.execute_script(click_script, buttons[1])
    print("Mismatched...")
    time.sleep(1)
    i -= 1
print("Completed MisMatching\n")
