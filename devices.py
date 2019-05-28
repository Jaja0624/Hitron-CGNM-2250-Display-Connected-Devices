from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import ElementClickInterceptedException
import time
import datetime

# Your router login credentials
myUsername = ""
myPassword = ""

# modem/router ip
loginUrl = 'http://192.168.0.1/login.htm'


# path to your chromedriver executable
chromedriverPath = 'C:\Windows\chromedriver.exe'

options = Options()
options.add_argument("--headless") 

# initialize selenium chromedriver
driver = webdriver.Chrome(options=options, executable_path=chromedriverPath)

# opens chrome browser to "loginUrl"
driver.get(loginUrl)

wait = WebDriverWait(driver, 15)

username = wait.until(EC.visibility_of_element_located((By.NAME, "user[login]")))
username.clear()
username.send_keys(myUsername)

password = wait.until(EC.visibility_of_element_located((By.NAME, "user[password]")))
password.clear()
password.send_keys(myPassword)

loginBtn = wait.until(EC.visibility_of_element_located((By.ID, "btnLogin")))
loginBtn.click()

wait.until(EC.visibility_of_element_located((By.ID, "clientsDiv")))

# url with show btn for connected devices
devicesUrl = 'http://192.168.0.1/index.htm#basic_lan/m/2/s/0'

driver.get(devicesUrl)

# find and press the show btn
showBtn = wait.until(EC.visibility_of_element_located((By.ID, "btnShowConnectedDevice")))
try:
    showBtn.click()
except ElementClickInterceptedException:
    time.sleep(3)
    showBtn.click()

devicesTable = wait.until(EC.visibility_of_element_located((By.ID, "tblConnectDevice")))

currentTime = datetime.datetime.now()
with open("prev.txt", "w") as file:
    file.write((str(currentTime)) + "\n")
    print(str(currentTime))
    for row in devicesTable.find_elements_by_xpath('./tbody/tr'):
        device = row.find_elements(By.TAG_NAME, "td")
        file.write(device[0].text + "\n")
        print(device[0].text) # host name

# close all browsers
driver.quit()