## AutoColumn Google Sheet
## By: Lucas Leung

# setup
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

# ---user configurable options---
cellLink = "" # paste in your link to the cell from the attendance spreadsheet
# driver = webdriver.Chrome() # assumes you use Chrome, uncomment whatever browser you use
driver = webdriver.Edge()
# driver = webdriver.Firefox()

# open link to cell
driver.get(cellLink)

# create new column to left, with via Actions API/Action Chains
# other browsers: Alt + Shift + i, then c, then c
actions = ActionChains(driver)
actions.send_keys(Keys.ALT + Keys.LEFT_SHIFT + "i" + "c" + "c")
actions.perform()

# delay
time.sleep(1)

# quit browser
driver.quit()
