from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

emails = [
    'jeffersoncampos_1@yahoo.com.br',
    'nayarafp_87@yahoo.com.br',
    'thy_hcas@yahoo.com.br',
]

for email in emails:
    driver = webdriver.Chrome('C:/Users/Guerine/Downloads/chromedriver_win32/chromedriver.exe')
    driver.get('https://docs.google.com/forms/d/e/1FAIpQLSdvn3MpY93-ool9snKDorF3uBUfDSNU2WbhNvllYA2jl4lgBQ/viewform')
    time.sleep(1)
    count = 0

    textboxes = driver.find_elements_by_class_name(
        "quantumWizTextinputPaperinputInput")

    for value in textboxes:
        value.send_keys(email)
        count += 1

    radiobutton = driver.find_elements_by_tag_name('label')
    count2 = 0
    for value in radiobutton:
        count2 += 1

    r = random.randint(1, 100)
    if r > 1:
        radiobutton[count2-1].click()
    else:
        choose = [1, 2, 5, 7]
        s = random.randint(0, 3)
        radiobutton[choose[s]].click()
    #time.sleep(1)

    submit = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
    submit.click()

    another_response = driver.find_element_by_xpath(
        '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    another_response.click()

    driver.close()
    driver.quit()