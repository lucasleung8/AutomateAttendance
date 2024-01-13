# setup
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import datetime

# ---user configurable options--- #

ics4uLink = "https://docs.google.com/spreadsheets/d/17mWdVgPJ0xo1qb0GAQLTVXSLu1_jl8bqeM3H4McVFeI/edit#gid=0&range=D2" # paste in your link to the cell from the attendance spreadsheet
tej34mLink = "https://docs.google.com/spreadsheets/d/1kPNp01St8eahSrfadigF5NHyBvvdxaplhzLufCYWfpU/edit#gid=0&range=D1" # paste in your link to the cell from the attendance spreadsheet
# driver = webdriver.Chrome() # assumes you use Chrome, uncomment whatever browser you use
driver = webdriver.Edge()
# driver = webdriver.Firefox()

delay = 2 # seconds passing after column created

# ---user configurable options--- #

# create datetime object from datetime class then format nicely
currentDate = datetime.datetime.now().strftime("%b %d")
actions = ActionChains(driver)

# create new column to left, with via Actions API/Action Chains
# stores actions then performs them
# ics4u
# open link to cell
driver.get(ics4uLink)
actions.key_down(Keys.LEFT_ALT).key_down(Keys.LEFT_SHIFT)
actions.send_keys("i").send_keys("c")
# time.sleep(0.5)
actions.send_keys("c")
actions.key_up(Keys.LEFT_ALT).key_up(Keys.LEFT_SHIFT)
actions.send_keys(currentDate).send_keys(Keys.RETURN)
actions.perform()

# delay
time.sleep(delay)

# clear actions object
actions.reset_actions()

# tej34m
driver.get(tej34mLink)
actions.key_down(Keys.LEFT_ALT).key_down(Keys.LEFT_SHIFT)
actions.send_keys("i").send_keys("c")
# time.sleep(0.5)
actions.send_keys("c")
actions.key_up(Keys.LEFT_ALT).key_up(Keys.LEFT_SHIFT)
actions.send_keys(currentDate).send_keys(Keys.RETURN)
actions.perform()

# delay
time.sleep(delay)

# quit browser
driver.quit()
