from pages.Rostelecom import *

class AuthLocators:

    auth_phone = (By.XPATH, '//*[@id = "t-btn-tab-phone"]')

    auth_email = (By.XPATH, '//*[@id = "t-btn-tab-mail"]')

    auth_login = (By.XPATH, '//*[@id = "t-btn-tab-login"]')

    entry_form = (By.XPATH, '//*[@id = "username"]')

    password_form = (By.XPATH, '//*[@id = "password"]')

    auth_log = (By.XPATH, '//button[@id = "kc-login"]')

    auth_VK = (By.XPATH, '//*[@id = "oidc_vk"]')

    auth_ok = (By.XPATH, '//*[@id = "oidc_ok"]')

    auth_MAIL = (By.XPATH, '//*[@id = "oidc_mail"]')

    auth_Googl = (By.XPATH, '//*[@id = "oidc_google"]')

    auth_Yandex = (By.XPATH, '//*[@id = "oidc_ya"]')

    forgot_password = (By.XPATH, '//*[@id = "forgot_password"]')

    user_agreement = (By.XPATH, '//*[@class = "rt-footer-left__item-accent" and contains(text(), " Пользовательским соглашением ")]')

class AccountLocators:

    acc_password = (By.XPATH, '//*[@id = "password_change"]')

    acc_current_password = (By.XPATH, '//*[@id = "current_password"]')

    acc_password_close = (By.XPATH, '//*[@id = "change_password_close"]')

    acc_logout = (By.XPATH, '//*[@id = "logout-btn"]')

    acc_personal_account = (By.XPATH, '//*[@id = "lk-btn"]')

    acc_account = (By.XPATH, '//*[@class = "sc-bvFjSx iqOiiv"]')

    acc_logout_account = (By.XPATH, '//*[@class = "sc-dkPtRN lgHXyI sc-dlVxhl bLVPuw"]')

    acc_logout_account_form = (By.XPATH, '//*[@id = "address"]')

    acc_logout_account_form_button = (By.XPATH, '//*[@id = "otp_get_code"]')

    acc_logout_account_code = (By.XPATH, '//*[@id = "rt-code-0"]')

class RostelecombuttonLocators:

    acc_rostelecom_website = (By.XPATH, '//*[@id = "rt-btn"]')

    acc_rostelecom_internet_button = (By.XPATH, '//a[@data-drupal-link-system-path = "page/687" and contains(text(), "Интернет в квартиру")]')

    acc_rostelecom_news_button = (By.XPATH, '//a[@data-drupal-link-system-path = "events" and contains(text(), "Новости")]')

    acc_rostelecom_office_button = (By.XPATH, '//a[@data-drupal-link-system-path = "node/2549" and contains(text(), "Офисы продаж")]')

    acc_rostelecom_office_button_Tele2 = (By.XPATH, '//*[contains(text(), "Офисы Tele2")]')