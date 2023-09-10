# from __future__ import absolute_import, unicode_literals
# from celery import shared_task

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.chrome.options import Options
# import time

# from core.models import Account
# from delivery.models import Delivery, Package
# from delivery.utils.scraper import go_till_order_list, scrape_orders

# chrome_driver_path = '/home/safex/chromedriver'

# USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"

# @shared_task
# def scrape_and_save_packages(account_id):
#     print('======================  başladıq =========================')
#     options = webdriver.ChromeOptions()
#     options.add_argument('--no-sandbox')
#     options.add_argument('--headless')
#     options.add_argument("--disable-dev-shm-usage")
#     ser = Service(executable_path="/usr/local/bin/chromedriver")
#     browser = webdriver.Chrome(options=options, service=ser)
#     # open the main url
#     browser.get("https://www.trendyol.com")
#     time.sleep(2)
#     print('======================  trendyola girdi ==================')
#     # login and go to my orders section
#     account = Account.objects.get(id=account_id)
#     go_till_order_list(browser, account)

#     # scroll to bottom (first 50 orders)
#     # scroll_to_bottom(browser, 10)

#     orders = browser.find_elements(By.CLASS_NAME, "order")
#     print('order sayi: ', len(orders))
#     user_orders = []
#     # scrape orders and each order`s packages and append user_orders list
#     scrape_orders(browser, orders, user_orders)

#     time.sleep(2)
#     browser.quit()
#     print('======================  gorek =========================')
#     account.is_processing = False
#     account.save()
#     for item in user_orders:
#         order_number = item['order_number']
#         order_date = item['order_date']
#         order_receiver = item['order_receiver']
#         delivery, created = Delivery.objects.get_or_create(
#             account=account, order_number=order_number,
#             order_receiver=order_receiver, order_date=order_date
#         )
#         for package in item['teslimatlar']:
#             package_no = package['teslimat_no']
#             cargo_company = package['cargo_company']
#             gonderi_num = package['gonderi_num']
#             product_category = package['product_category']
#             product_price = package['product_price']
#             product_count = package['product_count']
#             Package.objects.get_or_create(
#                 account=account,
#                 delivery=delivery, package_number=package_no,
#                 cargo_company=cargo_company, tracking_number=gonderi_num,
#                 category=product_category, price=product_price, product_count=product_count
#             )
#     print('======================  bitdi =========================')
#     return f'Packages created for user {account}'


# # ----------------------------------------------------------------------------------

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC
# import time

# from selenium.webdriver.support.ui import WebDriverWait


# chrome_driver_path = "/home/safex/chromedriver"

# USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"


# def login_to_asan(DecID, FIN, PassWord):
#     print("======================  başladıq =========================")
#     options = webdriver.ChromeOptions()
#     options.add_argument("--no-sandbox")
#     # options.add_argument('--headless')
#     options.add_argument("--disable-dev-shm-usage")
#     ser = Service(executable_path="/home/taleh/Downloads/chromedriver/chromedriver")
#     driver = webdriver.Chrome(options=options, service=ser)

#     driver.get(
#         "https://asanlogin.my.gov.az/auth?origin=https:%2F%2Fe.customs.gov.az%2Fauth%2Fasan"
#     )
#     # driver.maximize_window()
#     time.sleep(4)
#     print("======================  asan loginleshdi =========================")
#     element_p_tag = driver.find_element(
#         By.XPATH,
#         '//*[@id="wrapper"]/div/div/div/div/app-login-tabs/div/div[1]/div[1]/div/p[1]',
#     )
#     print("element_p_tag 1", element_p_tag)
#     element_p_tag.click()
#     time.sleep(4)
#     # login 6ARPY3L
#     # password Taleh123
#     element1_login_input = driver.find_element(
#         By.XPATH, '//*[@id="loginform"]/div[1]/div/div/input'
#     )
#     element1_password_input = driver.find_element(
#         By.XPATH, '//*[@id="loginform"]/div[2]/div/input'
#     )
#     element1_login_input.send_keys(FIN)
#     element1_password_input.send_keys(PassWord)
#     time.sleep(3)
#     # assign_order(UserID, ShipinfgID)
    
# def assign_order(UserID, DecID):
#      # get send button
#     element1_send_button = driver.find_element(
#         By.XPATH, '//*[@id="wrapper"]/div/div/div/div/app-log-in/div[3]/div/div[2]/div'
#     )
#     element1_send_button.click()
#     time.sleep(4)

#     driver.get("https://e.customs.gov.az/for-individuals")
#     time.sleep(4)

#     # //*[@id="root"]/div[1]/div[1]/div[2]/div/div/section/div/div[2]/div/div[2]/div

#     next_button = driver.find_element(
#         By.XPATH,
#         '//*[@id="root"]/div[1]/div[1]/div[2]/div/div/section/div/div[2]/div/div[2]/div',
#     )
#     next_button.click()
#     time.sleep(4)

#     items = driver.find_elements(By.CLASS_NAME, "jss275")
#     for index, item in enumerate(items):
#         track_span = item.find_element(By.CLASS_NAME, "MuiTypography-body1").text
#         track_number = track_span.split(":")[1].strip()
#         if DecID == track_number:
#             if index != 0:
#                 svg_icon = item.find_element(By.TAG_NAME, "svg")
#                 svg_icon.click()
#                 time.sleep(2)
#             body_ul = item.find_element(By.CLASS_NAME, "MuiList-dense")
#             body_ul_items = body_ul.find_elements(By.TAG_NAME, "li")
#             print("invoys", body_ul_items[2].text)
#             invoys_price = body_ul_items[2].text

#             time.sleep(4)
#             confirm_button = item.find_element(
#                 By.CLASS_NAME, "MuiButton-containedPrimary"
#             )
#             confirm_button.click()
#             time.sleep(2)

#             next_button2 = driver.find_element(
#                 By.CLASS_NAME, "MuiButton-containedPrimary"
#             )
#             next_button2.click()
#             time.sleep(2)

#             next_button3 = driver.find_element(
#                 By.CLASS_NAME, "MuiButton-containedPrimary"
#             )
#             next_button3.click()

#             time.sleep(2)
#             next_button4 = driver.find_element(By.CLASS_NAME, "MuiButton-contained")
#             next_button4.click()

#             time.sleep(2)
#             form_tag = driver.find_element(By.TAG_NAME, "form")
#             form_inputs = form_tag.find_elements(
#                 By.CLASS_NAME, "MuiOutlinedInput-input"
#             )
#             popups = form_tag.find_elements(
#                 By.CLASS_NAME, "MuiOutlinedInput-inputAdornedEnd"
#             )
#             first_popup = popups[0]
#             first_popup.send_keys("Paltar")
#             paltar_option = WebDriverWait(driver, 3).until(
#                 EC.element_to_be_clickable(
#                     (By.XPATH, "//*[contains(text(), 'Paltar')]")
#                 )
#             )
#             paltar_option.click()
#             time.sleep(2)

#             second_popup = popups[1]
#             second_popup.send_keys("Digər")
#             diger_option = WebDriverWait(driver, 3).until(
#                 EC.element_to_be_clickable(
#                     (By.XPATH, "//*[contains(text(), 'Digər')]")
#                 )
#             )
#             diger_option.click()
#             time.sleep(2)


#             third_popup = popups[2]
#             third_popup.send_keys("Türk lirəsi")
#             turk_lirasi_option = WebDriverWait(driver, 3).until(
#                 EC.element_to_be_clickable(
#                     (By.XPATH, "//*[contains(text(), 'Türk lirəsi')]")
#                 )
#             )
#             turk_lirasi_option.click()
            

#             invoys_price_input = form_inputs[2]
#             invoys_price_input.send_keys(invoys_price)

#             invoys_price_input = form_inputs[2]
#             invoys_price_input.send_keys(invoys_price)
#             time.sleep(3)

#             quantity_select_input = form_inputs[5]
#             quantity_select_input.send_keys("1")
#             time.sleep(3)

#             next_button5 = form_tag.find_element(
#                 By.CLASS_NAME, "MuiButton-containedPrimary"
#             )
#             next_button5.click()

#             time.sleep(2)
#             # class jss445
#             checkbox_input = driver.find_element(By.CLASS_NAME, "jss445")
#             checkbox_input.click()

#             time.sleep(2)
#             confirm_button = driver.find_element(By.CSS_SELECTOR, 'button[test-id="approve"]')
#             confirm_button.click()

#             time.sleep(3)
#             driver.quit()

#         else:
#             print("not found")

#             # must be select Türk lirəsi option



from celery import shared_task
from core.utils.excell_task import login_to_asan
from core.models import FailedDeclar


@shared_task
def rerun_fail_dec():
    qs = FailedDeclar.objects.filter(is_active=True)
    if qs.exists():
        for item in qs:
            login_to_asan(item.dec_id, item.fin_code, item.password)


@shared_task
def run_apply_declarations(dec_num, fin_code, password):
    login_to_asan(dec_num, fin_code, password)