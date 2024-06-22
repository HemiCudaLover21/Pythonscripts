from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from time import sleep

driver = webdriver.Firefox()
wait10 = WebDriverWait(driver,10)
actions = ActionChains(driver)

username = input("put your user:")
password = input("put your password:")
def LOGON_app1(username, password):
    driver.get("/")
    userfield = driver.find_element(By.XPATH,"")
    passfield = driver.find_element(By.XPATH,"")
    loginfield = driver.find_element(By.XPATH,"")
    userfield.send_keys(username)
    userfield.send_keys(Keys.TAB)
    passfield.send_keys(password)
    loginfield.click()
    


def LOGON_app2(username, password):
    driver.get("")
    userfield = driver.find_element(By.XPATH,"")
    passfield = driver.find_element(By.XPATH,"")
    loginfield = driver.find_element(By.XPATH,"")
    userfield.send_keys(username)
    userfield.send_keys(Keys.TAB)
    passfield.send_keys(password)
    loginfield.click()
def LOGON_app3(username, password):
    username += '@companydomain.net'
    driver.get("")
    userfield = driver.find_element(By.XPATH,"")
    passfield = driver.find_element(By.XPATH,"")
    loginfield = driver.find_element(By.XPATH,"")
    userfield.send_keys(username)
    userfield.send_keys(Keys.TAB)
    passfield.send_keys(password)
    loginfield.click()
    loginfield.click()
    loginfield.click()
LOGON_app1(username, password)
driver.execute_script("window.open('about:blank', 'secondtab');")
driver.switch_to.window("secondtab")
LOGON_app2(username, password)
driver.execute_script("window.open('about:blank', 'thirdtab');")
driver.switch_to.window("thirdtab")
LOGON_app3(username, password)
