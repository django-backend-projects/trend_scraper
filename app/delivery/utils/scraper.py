from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time


def scroll_to_bottom(browser, number):
    for c in range(1, number):
        time.sleep(1)  # Give time to loading the information
        try:
            element = browser.find_element(By.XPATH, f'/html/body/div[1]/div[3]/div[2]/div/div/div[3]/div[{c}]')
        except Exception:
            element = browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/div/div/div[3]/div[1]')
            break
        browser.execute_script("arguments[0].scrollIntoView();", element)


def go_till_order_list(browser, account):
    # select country and press submit
    try:
        print('======================  turkiyeni secir ==================')
        select = Select(browser.find_element(By.CSS_SELECTOR, ".country-select > select:nth-child(1)"))
        select.select_by_visible_text("Turkey")
        select_button = browser.find_element(By.CSS_SELECTOR, ".country-actions > button:nth-child(1)")
        select_button.click()
        time.sleep(2)
    except:
        try:
            action = ActionChains(browser)
            country = browser.find_element(By.CLASS_NAME, "country")
            action.move_to_element(country).perform()
            country_select = browser.find_element(By.CLASS_NAME, "country-select")
            action.move_to_element(country_select).click().perform()
            turkey = country_select.find_element(By.CLASS_NAME, "dropdown-item")
            action.move_to_element(turkey).click().perform()
            browser.find_element(By.XPATH, "//*[@id='header-wrapper']/div/div[2]/div[1]/div[2]/button").click()
        except:
            pass

    # login_button = browser.find_element(By.XPATH, "//*[@id='account-navigation-container']/div/div[1]/div[1]/p")
    # click login button
    login_button = browser.find_element(By.CLASS_NAME, "link-text")
    login_button.click()
    time.sleep(2)

    print('======================  login olur ==================')
    # get email and password inputs, and fill credentials
    user_email = browser.find_element(By.ID, "login-email")
    user_password = browser.find_element(By.ID, "login-password-input")
    user_email.send_keys(account.email)
    user_password.send_keys(account.password)

    # after filling credentials, submit the login button
    login_button2 = browser.find_element(By.CSS_SELECTOR, ".q-primary")
    login_button2.click()
    time.sleep(2)

    # click my orders button
    my_orders_button = browser.find_element(By.CSS_SELECTOR, ".account-user > p:nth-child(2)")
    my_orders_button.click()
    time.sleep(2)

    # and sort orders for last month
    last_month_button = browser.find_element(By.CSS_SELECTOR, ".sorting > div:nth-child(1)")
    last_month_button.click()
    last_month = browser.find_element(By.CSS_SELECTOR, "div.ty-select-option:nth-child(2)")
    last_month.click()
    time.sleep(2)


def scrape_orders(browser, orders, user_orders):
    for order in orders:
        order_statuses = order.find_elements(By.CLASS_NAME, "order-item-status")
        order_status_list = [order_status.find_elements(By.TAG_NAME, "span")[0].text for order_status in order_statuses]
        if 'Teslim Edildi' in order_status_list:
            order_header = order.find_element(By.CLASS_NAME, "order-header")
            order_dict = {
                'order_date': order_header.find_elements(By.CLASS_NAME, "order-header-info")[0].find_element(By.TAG_NAME, "b").text,
                'order_receiver': order_header.find_elements(By.CLASS_NAME, "order-header-info")[2].find_element(By.TAG_NAME, "b").text,
            }
            order_detail_url = order_header.find_element(By.TAG_NAME, "a").get_attribute("href")

            browser.execute_script("window.open('');")
            browser.switch_to.window(browser.window_handles[1])
            browser.get(order_detail_url)
            time.sleep(2)
            header_section = browser.find_elements(By.CLASS_NAME, "header-section")[1]
            order_number = header_section.find_elements(By.TAG_NAME, "span")[1].text
            order_dict['order_number'] = order_number
            teslimatlar = browser.find_elements(By.CLASS_NAME, "order-detail-shipment")
            order_dict['teslimatlar'] = []
            for teslimat in teslimatlar:
                teslimat_status = teslimat.find_element(By.CLASS_NAME, "shipment-content-status").find_element(By.TAG_NAME, "span").text
                if teslimat_status == 'Teslim Edildi':
                    product_url = teslimat.find_element(By.CLASS_NAME, "product-box-info").find_element(By.TAG_NAME, "a").get_attribute("href")
                    try:
                        browser.execute_script("window.open('');")
                        browser.switch_to.window(browser.window_handles[2])
                        browser.get(product_url)
                        time.sleep(1)
                        try:
                            product_category = browser.find_elements(By.CLASS_NAME, "product-detail-breadcrumb-item")[-2].text
                        except NoSuchElementException:
                            try:
                                product_category = browser.find_elements(By.CLASS_NAME, "product-detail-breadcrumb-item")[-1].text
                            except NoSuchElementException:
                                product_category = 'Bulunamadı'
                        browser.close()
                        browser.switch_to.window(browser.window_handles[1])
                    except:
                        product_category = 'Bulunamadı'
                        browser.close()
                        browser.switch_to.window(browser.window_handles[1])

                    teslimat_no = teslimat.find_element(By.CLASS_NAME, "shipment-number").text
                    teslimat_cargo = teslimat.find_elements(By.TAG_NAME, "span")[3].get_attribute("innerHTML")
                    if teslimat_cargo.startswith('<div'):
                        teslimat_cargo = "Trendyol Express"
                    product_price = teslimat.find_element(By.CLASS_NAME, "product-box-info-price-selling").text
                    product_count = len(teslimat.find_elements(By.CLASS_NAME, "shipment-content-product-box"))
                    teslimat_detay_url = teslimat.find_element(By.CLASS_NAME, "shipment-content-info").find_element(By.TAG_NAME, "a").get_attribute("href")
                    gonderi_takip_nu = 'Bulunamadı'
                    if browser.current_url != teslimat_detay_url:
                        try:
                            browser.execute_script("window.open('');")
                            browser.switch_to.window(browser.window_handles[2])
                            browser.get(teslimat_detay_url)
                            time.sleep(10)
                            browser.find_element(By.TAG_NAME, "html")

                            if teslimat_cargo == 'MNG Kargo':
                                captcha_word = browser.find_element(By.CLASS_NAME, "captcha").text
                                captcha_word_list = captcha_word.split()
                                final_captcha = ''.join(captcha_word_list)
                                input_field = browser.find_element(By.CSS_SELECTOR, "#captcha1 > input:nth-child(2)")
                                input_field.send_keys(final_captcha)
                                submit_button = browser.find_element(By.CLASS_NAME, "btn-confirm-captcha")
                                submit_button.click()
                                time.sleep(5)
                                try:
                                    # gonderi_takip_nu = browser.find_element(By.XPATH, "/html/body/main/section/div/div[2]/div/div/div/div[1]/div/div[1]/div[2]/div[2]").text
                                    gonderi_takip_nu = browser.find_element(By.XPATH, "/html/body/main/section/div/div[2]/div/div/div/div[1]/div/div[1]/div/div[3]/div/div[2]/div[2]").text
                                except NoSuchElementException:
                                    gonderi_takip_nu = 'Bulunamadı'
                            elif teslimat_cargo == 'Trendyol Express':
                                try:
                                    gonderi_takip_nu = browser.find_element(By.CSS_SELECTOR, "div.item:nth-child(2) > div:nth-child(2)").text
                                except NoSuchElementException:
                                    gonderi_takip_nu = 'Bulunamadı'
                            elif teslimat_cargo in ['Aras Kargo', 'Sürat Kargo', 'Sendeo Kargo']:
                                try:
                                    gonderi_takip_nu = browser.find_element(By.CLASS_NAME, "tracking-number").find_element(By.CLASS_NAME, "content").text
                                except NoSuchElementException:
                                    try:
                                        gonderi_takip_nu = browser.find_element(By.ID, "labelShipmentCode").text
                                    except NoSuchElementException:
                                        gonderi_takip_nu = 'Bulunamadı'
                            elif teslimat_cargo == 'PTT Kargo':
                                try:
                                    gonderi_takip_nu = browser.find_element(By.CLASS_NAME, "tracking-number").find_element(By.CLASS_NAME, "content").text
                                except NoSuchElementException:
                                    try:
                                        gonderi_takip_nu = browser.find_element(By.XPATH, "/html/body/form/div[2]/div/div/div/div[3]/div/fieldset/div/div/div/table/tbody/tr[1]/td[1]").text
                                    except NoSuchElementException:
                                        gonderi_takip_nu = 'Bulunamadı'
                            elif teslimat_cargo == 'Yurtiçi Kargo':
                                try:
                                    gonderi_takip_nu = browser.find_element(By.ID, "id").text
                                except NoSuchElementException:
                                    gonderi_takip_nu = 'Bulunamadı'
                            elif teslimat_cargo == 'UPS Kargo':
                                try:
                                    gonderi_takip_nu = browser.find_element(By.ID, "ctl00_MainContent_LabelTakipNo").text
                                except NoSuchElementException:
                                    gonderi_takip_nu = 'Bulunamadı'

                        except:
                            pass

                        browser.close()
                        browser.switch_to.window(browser.window_handles[1])

                        order_dict['teslimatlar'].append({
                            'teslimat_no': teslimat_no,
                            'cargo_company': teslimat_cargo,
                            'gonderi_num': gonderi_takip_nu,
                            'product_category': product_category,
                            'product_price': product_price,
                            'product_count': product_count
                        })

            browser.close()
            browser.switch_to.window(browser.window_handles[0])
            user_orders.append(order_dict)
            print(user_orders)



# def scrape_orders(browser, orders, user_orders):
#     for order in orders:
#         order_statuses = order.find_elements(By.CLASS_NAME, "order-item-status")
#         order_status_list = [order_status.find_elements(By.TAG_NAME, "span")[0].text for order_status in order_statuses]
#         if 'Teslim Edildi' in order_status_list:
#             order_header = order.find_element(By.CLASS_NAME, "order-header")
#             order_dict = {
#                 'order_date': order_header.find_elements(By.CLASS_NAME, "order-header-info")[0].find_element(By.TAG_NAME, "b").text,
#                 'order_receiver': order_header.find_elements(By.CLASS_NAME, "order-header-info")[2].find_element(By.TAG_NAME, "b").text,
#             }
#             order_detail_url = order_header.find_element(By.TAG_NAME, "a").get_attribute("href")
#
#             browser.execute_script("window.open('');")
#             browser.switch_to.window(browser.window_handles[1])
#             browser.get(order_detail_url)
#             time.sleep(2)
#             header_section = browser.find_elements(By.CLASS_NAME, "header-section")[1]
#             order_number = header_section.find_elements(By.TAG_NAME, "span")[1].text
#             order_dict['order_number'] = order_number
#             teslimatlar = browser.find_elements(By.CLASS_NAME, "order-detail-shipment")
#             order_dict['teslimatlar'] = []
#             for teslimat in teslimatlar:
#                 teslimat_status = teslimat.find_element(By.CLASS_NAME, "shipment-content-status").find_element(By.TAG_NAME, "span").text
#                 if teslimat_status == 'Teslim Edildi':
#                     product_url = teslimat.find_element(By.CLASS_NAME, "product-box-info").find_element(By.TAG_NAME, "a").get_attribute("href")
#                     try:
#                         browser.execute_script("window.open('');")
#                         browser.switch_to.window(browser.window_handles[2])
#                         browser.get(product_url)
#                         time.sleep(1)
#                         try:
#                             product_category = browser.find_elements(By.CLASS_NAME, "product-detail-breadcrumb-item")[-2].text
#                         except NoSuchElementException:
#                             try:
#                                 product_category = browser.find_elements(By.CLASS_NAME, "product-detail-breadcrumb-item")[-1].text
#                             except NoSuchElementException:
#                                 product_category = 'Bulunamadı'
#                         browser.close()
#                         browser.switch_to.window(browser.window_handles[1])
#                     except:
#                         product_category = 'Bulunamadı'
#                         browser.close()
#                         browser.switch_to.window(browser.window_handles[1])
#
#                     teslimat_no = teslimat.find_element(By.CLASS_NAME, "shipment-number").text
#                     teslimat_cargo = teslimat.find_elements(By.TAG_NAME, "span")[3].get_attribute("innerHTML")
#                     if teslimat_cargo.startswith('<div'):
#                         teslimat_cargo = "Trendyol Express"
#                     product_price = teslimat.find_element(By.CLASS_NAME, "product-box-info-price-selling").text
#                     product_count = len(teslimat.find_elements(By.CLASS_NAME, "shipment-content-product-box"))
#                     teslimat_detay_url = teslimat.find_element(By.CLASS_NAME, "shipment-content-info").find_element(By.TAG_NAME, "a").get_attribute("href")
#                     if teslimat_cargo != 'Yurtiçi Kargo':
#                         browser.execute_script("window.open('');")
#                         browser.switch_to.window(browser.window_handles[2])
#                         browser.get(teslimat_detay_url)
#                         time.sleep(2)
#                     gonderi_takip_nu = 'Bulunamadı'
#                     if teslimat_cargo == 'MNG Kargo':
#                         captcha_word = browser.find_element(By.CLASS_NAME, "captcha").text
#                         captcha_word_list = captcha_word.split()
#                         final_captcha = ''.join(captcha_word_list)
#                         input_field = browser.find_element(By.CSS_SELECTOR, "#captcha1 > input:nth-child(2)")
#                         input_field.send_keys(final_captcha)
#                         submit_button = browser.find_element(By.CLASS_NAME, "btn-confirm-captcha")
#                         submit_button.click()
#                         time.sleep(3)
#                         try:
#                             gonderi_takip_nu = browser.find_element(By.XPATH, "/html/body/main/section/div/div[2]/div/div/div/div[1]/div/div[1]/div/div[3]/div/div[2]/div[2]").text
#                         except NoSuchElementException:
#                             gonderi_takip_nu = 'Bulunamadı'
#                     elif teslimat_cargo == 'Trendyol Express':
#                         try:
#                             gonderi_takip_nu = browser.find_element(By.CSS_SELECTOR, "div.item:nth-child(2) > div:nth-child(2)").text
#                         except NoSuchElementException:
#                             gonderi_takip_nu = 'Bulunamadı'
#                     elif teslimat_cargo in ['Aras Kargo', 'Sürat Kargo', 'Sendeo Kargo']:
#                         try:
#                             gonderi_takip_nu = browser.find_element(By.CLASS_NAME, "tracking-number").find_element(By.CLASS_NAME, "content").text
#                         except NoSuchElementException:
#                             try:
#                                 gonderi_takip_nu = browser.find_element(By.ID, "labelShipmentCode").text
#                             except NoSuchElementException:
#                                 gonderi_takip_nu = 'Bulunamadı'
#                     elif teslimat_cargo == 'PTT Kargo':
#                         try:
#                             gonderi_takip_nu = browser.find_element(By.CLASS_NAME, "tracking-number").find_element(By.CLASS_NAME, "content").text
#                         except NoSuchElementException:
#                             try:
#                                 gonderi_takip_nu = browser.find_element(By.XPATH, "/html/body/form/div[2]/div/div/div/div[3]/div/fieldset/div/div/div/table/tbody/tr[1]/td[1]").text
#                             except NoSuchElementException:
#                                 gonderi_takip_nu = 'Bulunamadı'
#                     elif teslimat_cargo == 'Yurtiçi Kargo':
#                         try:
#                             gonderi_takip_nu = browser.find_element(By.ID, "id").text
#                         except NoSuchElementException:
#                             gonderi_takip_nu = 'Bulunamadı'
#                     elif teslimat_cargo == 'UPS Kargo':
#                         try:
#                             gonderi_takip_nu = browser.find_element(By.ID, "ctl00_MainContent_LabelTakipNo").text
#                         except NoSuchElementException:
#                             gonderi_takip_nu = 'Bulunamadı'
#                     if teslimat_cargo != 'Yurtiçi Kargo':
#                         browser.close()
#                         browser.switch_to.window(browser.window_handles[1])
#
#                     order_dict['teslimatlar'].append({
#                         'teslimat_no': teslimat_no,
#                         'cargo_company': teslimat_cargo,
#                         'gonderi_num': gonderi_takip_nu,
#                         'product_category': product_category,
#                         'product_price': product_price,
#                         'product_count': product_count
#                     })
#
#             browser.close()
#             browser.switch_to.window(browser.window_handles[0])
#             user_orders.append(order_dict)


# def scrape_and_save_packages(account):
#     options = webdriver.ChromeOptions()
#     browser = webdriver.Chrome(options=options)
#     # open the main url
#     browser.get("https://www.trendyol.com")
#     time.sleep(2)
#
#     user_orders = []
#
#     # login and go to my orders section
#     go_till_order_list(browser, account)
#
#     # scroll to bottom (first 50 orders)
#     # scroll_to_bottom(browser, 10)
#
#     orders = browser.find_elements(By.CLASS_NAME, "order")
#     print('order sayi: ', len(orders))
#
#     # scrape orders and each order`s packages and append user_orders list
#     scrape_orders(browser, orders, user_orders)
#
#     time.sleep(2)
#     browser.quit()
#
#     account.is_processing = False
#     account.save()
