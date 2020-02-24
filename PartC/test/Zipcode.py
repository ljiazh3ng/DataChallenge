from telnetlib import EC

from selenium import webdriver
import pandas as pd
import csv
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome('/Users/jiazhenglua/Desktop/GitHub/DataChallenge/PartC/test/chromedriver')


df = pd.read_csv("airports.csv")
df = df.loc[(df['type'] == 'small_airport') | (df['type'] == 'medium_airport')]
df = df[["name","latitude_deg","longitude_deg"]]
writer = csv.writer(open("output3.csv", "a", newline=''))
# writer.writerow(["Airport Name","Zipcode"])
print(df)

previous = 0
next = 0
driver.get('https://www.mapdevelopers.com/what-is-my-zip-code.php')
time.sleep(10)
for index, row in df.iterrows():
    name = row["name"]
    lat = row["latitude_deg"]
    lon = row["longitude_deg"]
    input = driver.find_element_by_id('address')
    input.click()
    input.clear()
    input.send_keys('%s %s' % (lat, lon))
    input.click()
    input.send_keys(Keys.TAB)
    input.send_keys(Keys.ENTER)
    time.sleep(0.5)
    # button_path = "button"
    wait = WebDriverWait(driver, 10)
    # button = wait.until(EC.element_to_be_clickable((By.XPATH, button_path))).click()
    element = wait.until(EC.visibility_of_element_located((By.XPATH,"//*[@id='display_zip']")))
    zipcode = driver.find_element_by_id("display_zip").text
    next = zipcode
    if zipcode:
        if next != previous:
            writer.writerow([name, zipcode])
            print(zipcode)
        else:
            writer.writerow([name, "None"])
            print(zipcode)
    else:
        writer.writerow([name, "None"])
        print(zipcode)
    previous = zipcode
    zipcode = None


