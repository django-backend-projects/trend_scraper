import contextlib
import json
import os

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time
import pickle


def get_users():
    cookies_path = os.path.join(os.path.abspath(f'{__file__}/../'), 'cookies')
    print('======================  başladıq =========================')
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    # options.add_argument('--headless')
    options.add_argument("--disable-dev-shm-usage")
    ser = Service(executable_path="/usr/local/bin/chromedriver")
    browser = webdriver.Chrome(options=options, service=ser)
    # Try to load the cookies for the account
    try:
        with open(f"{cookies_path}/cookies.pkl", "rb") as f:
            cookies = pickle.load(f)
            for cookie in cookies:
                browser.add_cookie(cookie)
    except Exception as e:
        print('exception', e)
        # open the main url
        browser.get("https://backend.safex.az/auth/login")
        time.sleep(2)
        print('======================  safex-e girdi ==================')
        print('======================  login olur ==================')
        # get email and password inputs, and fill credentials
        user_email = browser.find_element(By.NAME, "email")
        user_password = browser.find_element(By.NAME, "password")
        user_email.send_keys("yunis9161@gmail.com")
        user_password.send_keys("12345678")

        # after filling credentials, submit the login button
        login_button2 = browser.find_element(By.CSS_SELECTOR, ".mdc-button--raised")
        login_button2.click()
        time.sleep(3)
        # Save the cookies
        if not os.path.exists(f"{cookies_path}"):
            os.makedirs(f"{cookies_path}")
        with open(f"{cookies_path}/cookies.pkl", "wb") as f:
            pickle.dump(browser.get_cookies(), f)
        print('yoxladi ===============================================================')
    browser.get("https://backend.safex.az/shipments/for-customs-declaration-with-account")
    time.sleep(5)


get_users()