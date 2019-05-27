from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

# Your router login credentials
myUsername = ""
myPassword = ""
loginUrl = 'http://192.168.0.1/login.htm'

# initialize selenium webdriver 
# opens chrome browser to "loginUrl"
driver = webdriver.Chrome()

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
showBtn.click()

devicesTable = wait.until(EC.visibility_of_element_located((By.ID, "tblConnectDevice")))
time.sleep(4) # necessary to wait for the table to load completely (i think)
for row in devicesTable.find_elements_by_xpath('./tbody/tr'):
    col = row.find_elements(By.TAG_NAME, "td")
    print(col[0].text)

# close all browsers
driver.quit()