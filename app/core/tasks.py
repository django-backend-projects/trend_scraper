from __future__ import absolute_import, unicode_literals
from celery import shared_task

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import time

from core.models import Account
from delivery.models import Delivery, Package
from delivery.utils.scraper import go_till_order_list, scrape_orders

chrome_driver_path = '/home/safex/chromedriver'

USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"

@shared_task
def scrape_and_save_packages(account_id):
    print('======================  başladıq =========================')
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')
    options.add_argument("--disable-dev-shm-usage")
    ser = Service(executable_path="/usr/local/bin/chromedriver")
    browser = webdriver.Chrome(options=options, service=ser)
    # open the main url
    browser.get("https://www.trendyol.com")
    time.sleep(2)
    print('======================  trendyola girdi ==================')
    # login and go to my orders section
    account = Account.objects.get(id=account_id)
    go_till_order_list(browser, account)

    # scroll to bottom (first 50 orders)
    # scroll_to_bottom(browser, 10)

    orders = browser.find_elements(By.CLASS_NAME, "order")
    print('order sayi: ', len(orders))
    user_orders = []
    # scrape orders and each order`s packages and append user_orders list
    scrape_orders(browser, orders, user_orders)

    time.sleep(2)
    browser.quit()
    print('======================  gorek =========================')
    account.is_processing = False
    account.save()
    for item in user_orders:
        order_number = item['order_number']
        order_date = item['order_date']
        order_receiver = item['order_receiver']
        delivery, created = Delivery.objects.get_or_create(
            account=account, order_number=order_number,
            order_receiver=order_receiver, order_date=order_date
        )
        for package in item['teslimatlar']:
            package_no = package['teslimat_no']
            cargo_company = package['cargo_company']
            gonderi_num = package['gonderi_num']
            product_category = package['product_category']
            product_price = package['product_price']
            product_count = package['product_count']
            Package.objects.get_or_create(
                account=account,
                delivery=delivery, package_number=package_no,
                cargo_company=cargo_company, tracking_number=gonderi_num,
                category=product_category, price=product_price, product_count=product_count
            )
    print('======================  bitdi =========================')
    return f'Packages created for user {account}'


def login_to_asan(UserID, FIN, PassWord):
    print('======================  başladıq =========================')
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    # options.add_argument('--headless')
    options.add_argument("--disable-dev-shm-usage")
    ser = Service(executable_path="/home/taleh/Downloads/chromedriver/chromedriver")
    driver = webdriver.Chrome(options=options, service=ser)

    driver.get("https://asanlogin.my.gov.az/auth?origin=https:%2F%2Fe.customs.gov.az%2Fauth%2Fasan")
    time.sleep(4)
    print('======================  asan loginleshdi =========================')
    # must be click tag which it inneHTML is equal İdentifikasiya nömrəsi ilə 
    # //*[@id="wrapper"]/div/div/div/div/app-login-tabs/div/div[1]/div[1]/div/p[1]
    element_p_tag = driver.find_element(By.XPATH, '//*[@id="wrapper"]/div/div/div/div/app-login-tabs/div/div[1]/div[1]/div/p[1]')
    print('element_p_tag 1', element_p_tag)
    element_p_tag.click()
    time.sleep(4)
    # login 6ARPY3L
    # password Taleh123
    element1_login_input = driver.find_element(By.XPATH, '//*[@id="loginform"]/div[1]/div/div/input')
    element1_password_input = driver.find_element(By.XPATH, '//*[@id="loginform"]/div[2]/div/input')
    element1_login_input.send_keys(FIN)
    element1_password_input.send_keys(PassWord)
    time.sleep(2)

    # get send button
    element1_send_button = driver.find_element(By.XPATH, '//*[@id="wrapper"]/div/div/div/div/app-log-in/div[3]/div/div[2]/div')
    element1_send_button.click()
    time.sleep(4)

    # get local url + for-individuals
    driver.get('https://e.customs.gov.az/for-individuals/post-declaration')
    time.sleep(4)

    # js path document.querySelector("body > div.jss69.test-modal > div.MuiPaper-root.jss70.jss177.MuiPaper-elevation1.MuiPaper-rounded > div.jss71.jss176 > div:nth-child(1) > div.MuiCardHeader-root.jss224 > div > button > span > span")
    # element_js_path = driver.execute_script("return document.querySelector('body > div.jss69.test-modal > div.MuiPaper-root.jss70.jss177.MuiPaper-elevation1.MuiPaper-rounded > div.jss71.jss176 > div:nth-child(1) > div.MuiCardHeader-root.jss224 > div > button > span > span');")
    

    time.sleep(400)