# Screenshot using Selenium
# Automate routine work with Selenium
from selenium import webdriver
from PIL import Image
from time import sleep
from selenium.webdriver.common.by import By
import os

way = 'C:/Users/makar/Desktop/Documents/'


def main(website: str):
    browser = webdriver.Firefox()
    browser.get(website)
    return qr_code(browser)


def screenshot(element, name: str, browser):
    location = element.location
    size = element.size
    browser.get_full_page_screenshot_as_file(f'{way}Page.png')
    x = location['x']
    y = location['y']
    w = x + size['width']
    h = y + size['height']
    fill_img = Image.open(f'{way}Page.png')
    crop_img = fill_img.crop((x, y, w, h))
    crop_img.save(f'{way}{name}.png')
    os.remove(f'{way}Page.png')


def qr_code(browser):
    element = browser.find_element(By.XPATH, '//*[@id="get-app"]/div[2]/div[3]')
    name = 'QR-code'
    screenshot(element, name, browser)
    return auto(browser)


def auto(browser):
    button = browser.find_element(By.CLASS_NAME, 'nav-header__listItem  ')
    button.click()
    sleep(5)
    list_automobiles = {'JAC JS6': '//*[@id="bx_3218110189_16965"]/div',
                        'EXEED LX': '//*[@id="bx_3218110189_14412"]/div',
                        'Tesla Model S': '//*[@id="bx_3218110189_10086"]/div'}
    for key, value in list_automobiles.items():
        element = browser.find_element(By.XPATH, value)
        name = key
        screenshot(element, name, browser)
    return final(browser)


def final(browser):
    button = browser.find_element(By.XPATH, '//*[@id="header__actionsLink--faq"]')
    button.click()
    sleep(2)
    element = browser.find_element(By.XPATH, '/html/body/div[1]/main/div/div/div[1]/div/div[2]/img')
    name = 'Final'
    screenshot(element, name, browser)
    element = browser.find_element(By.XPATH, '/html/body/div[1]/main/div/div/div[1]/div/div[1]/div[2]/div').text.split('\n\n')
    for i in element:
        print(i)
    browser.quit()


if __name__ == '__main__':
    main('https://citydrive.ru')
