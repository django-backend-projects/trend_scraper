from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import time


chrome_driver_path = "/home/safex/chromedriver"

USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"


def login_to_asan(UserID, FIN, PassWord):
    print("======================  başladıq =========================")
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    # options.add_argument('--headless')
    options.add_argument("--disable-dev-shm-usage")
    ser = Service(executable_path="/home/taleh/Downloads/chromedriver/chromedriver")
    driver = webdriver.Chrome(options=options, service=ser)

    driver.get(
        "https://asanlogin.my.gov.az/auth?origin=https:%2F%2Fe.customs.gov.az%2Fauth%2Fasan"
    )
    time.sleep(4)
    print("======================  asan loginleshdi =========================")
    # must be click tag which it inneHTML is equal İdentifikasiya nömrəsi ilə
    # //*[@id="wrapper"]/div/div/div/div/app-login-tabs/div/div[1]/div[1]/div/p[1]
    element_p_tag = driver.find_element(
        By.XPATH,
        '//*[@id="wrapper"]/div/div/div/div/app-login-tabs/div/div[1]/div[1]/div/p[1]',
    )
    print("element_p_tag 1", element_p_tag)
    element_p_tag.click()
    time.sleep(4)
    # login 6ARPY3L
    # password Taleh123
    element1_login_input = driver.find_element(
        By.XPATH, '//*[@id="loginform"]/div[1]/div/div/input'
    )
    element1_password_input = driver.find_element(
        By.XPATH, '//*[@id="loginform"]/div[2]/div/input'
    )
    element1_login_input.send_keys(FIN)
    element1_password_input.send_keys(PassWord)
    time.sleep(2)

    # get send button
    element1_send_button = driver.find_element(
        By.XPATH, '//*[@id="wrapper"]/div/div/div/div/app-log-in/div[3]/div/div[2]/div'
    )
    element1_send_button.click()
    time.sleep(4)

    driver.get("https://e.customs.gov.az/for-individuals")
    time.sleep(4)

    # //*[@id="root"]/div[1]/div[1]/div[2]/div/div/section/div/div[2]/div/div[2]/div

    next_button = driver.find_element(
        By.XPATH, '//*[@id="root"]/div[1]/div[1]/div[2]/div/div/section/div/div[2]/div/div[2]/div'
    )
    next_button.click()





    # get local url + for-individuals
    # driver.get("https://e.customs.gov.az/for-individuals/post-declaration")
    time.sleep(4)

    # js path document.querySelector("body > div.jss69.test-modal > div.MuiPaper-root.jss70.jss177.MuiPaper-elevation1.MuiPaper-rounded > div.jss71.jss176 > div:nth-child(1) > div.MuiCardHeader-root.jss224 > div > button > span > span")
    # element_js_path = driver.execute_script("return document.querySelector('body > div.jss69.test-modal > div.MuiPaper-root.jss70.jss177.MuiPaper-elevation1.MuiPaper-rounded > div.jss71.jss176 > div:nth-child(1) > div.MuiCardHeader-root.jss224 > div > button > span > span');")

    time.sleep(400)


  

login_to_asan("123456", "1WMBK3Q", "Farhad1903")
