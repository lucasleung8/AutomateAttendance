## AutoColumn Google Sheet tool
## adds new column to 3 different spreadsheets
## By: Lucas Leung

# setup
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import datetime

# ---user configurable options---
cellLink = "https://docs.google.com/spreadsheets/d/17mWdVgPJ0xo1qb0GAQLTVXSLu1_jl8bqeM3H4McVFeI/edit#gid=0&range=D2" # paste in your link to the cell from the attendance spreadsheet
# driver = webdriver.Chrome() # assumes you use Chrome, uncomment whatever browser you use
driver = webdriver.Edge()
# driver = webdriver.Firefox()

# open link to cell
driver.get(cellLink)

# create datetime object from datetime class then format it nicely
currentDate = datetime.datetime.now().strftime("%b %d")

# create new column to left, with via Actions API/Action Chains
actions = ActionChains(driver)
actions.key_down(Keys.LEFT_ALT).key_down(Keys.LEFT_SHIFT)
actions.send_keys("i")
actions.send_keys("c")
time.sleep(1)
actions.send_keys("c")
actions.key_up(Keys.LEFT_ALT).key_up(Keys.LEFT_SHIFT)
actions.send_keys(currentDate)
actions.perform()

# delay
time.sleep(1)



# quit browser
driver.quit()
