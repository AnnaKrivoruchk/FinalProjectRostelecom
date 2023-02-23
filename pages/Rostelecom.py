
from pages.base import BasePage
from selenium.webdriver.common.by import By
from pages.locators import AuthLocators, AccountLocators, RostelecombuttonLocators

import time,os

class AuthPage(BasePage):
    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        url = os.getenv('LOGIN_URL') or 'https://b2c.passport.rt.ru/'
        driver.get(url)
        self.phone = driver.find_element(*AuthLocators.auth_phone)
        self.email = driver.find_element(*AuthLocators.auth_email)
        self.login = driver.find_element(*AuthLocators.auth_login)
        self.entry_log = driver.find_element(*AuthLocators.entry_form)
        self.entry_password = driver.find_element(*AuthLocators.password_form)
        self.auth_button = driver.find_element(*AuthLocators.auth_log)
        self.VK = driver.find_element(*AuthLocators.auth_VK)
        self.ok = driver.find_element(*AuthLocators.auth_ok)
        self.MAIL = driver.find_element(*AuthLocators.auth_MAIL)
        self.Googl = driver.find_element(*AuthLocators.auth_Googl)
        self.Yandex = driver.find_element(*AuthLocators.auth_Yandex)

        self.forgot = driver.find_element(*AuthLocators.forgot_password)
        self.agreement = driver.find_element(*AuthLocators.user_agreement)

    def choose_phone(self):
        self.phone.click()
        time.sleep(1)

    def choose_email(self):
        self.email.click()
        time.sleep(1)

    def choose_login(self):
        self.login.click()
        time.sleep(1)

    def entery_form(self, value):
        self.entry_log.send_keys(value)
        time.sleep(2)

    def entery_pass(self, value):
        self.entry_password.send_keys(value)
        time.sleep(2)

    def button_enter(self):
        self.auth_button.click()
        time.sleep(1)

    def authVK(self):
        self.VK.click()
        time.sleep(1)

    def authOK(self):
        self.ok.click()
        time.sleep(1)

    def authMAIL(self):
        self.MAIL.click()
        time.sleep(1)

    def authGoogl(self):
        self.Googl.click()
        time.sleep(1)

    def authYandex(self):
        self.Yandex.click()
        time.sleep(1)

    def forgotpassword(self):
        self.forgot.click()
        time.sleep(1)

    def useragreement(self):
        self.agreement.click()
        time.sleep(1)

class InAccount(BasePage):
    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        url = 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials'
        driver.get(url)

        self.change_password = driver.find_element(*AccountLocators.acc_password)
        self.current_password = driver.find_element(*AccountLocators.acc_current_password)
        self.close_password = driver.find_element(*AccountLocators.acc_password_close)
        self.logout = driver.find_element(*AccountLocators.acc_logout)
        self.personal_account = driver.find_element(*AccountLocators.acc_personal_account)
        self.account = driver.find_element(*AccountLocators.acc_account)
        self.personal_logout_account = driver.find_element(*AccountLocators.acc_logout_account)
        self.personal_logout_account_form = driver.find_element(*AccountLocators.acc_logout_account_form)
        self.personal_logout_account_button = driver.find_element(*AccountLocators.acc_logout_account_form_button)
        self.account_code = driver.find_element(*AccountLocators.acc_logout_account_code)

    def changepassword(self):
        self.change_password.click()
        time.sleep(1)

    def currentpassword(self, value):
        self.current_password.send_keys(value)
        time.sleep(2)
        self.current_password.clear_element()
        time.sleep(1)

    def closepassword(self):
        self.close_password.click()
        time.sleep(1)

    def logoutacc(self):
        self.logout.click()
        time.sleep(1)

    def personalaccount(self):
        self.personal_account.click()
        time.sleep(1)

    def account_data(self):
        self.account.fimd_element_to_be_clickable().click()
        time.sleep(1)

    def logoutaccount(self):
        self.personal_logout_account.click()
        time.sleep(1)

    def logoutaccount_form(self, value):
        self.personal_logout_account_form.send_keys(value)
        time.sleep(1)

    def code_account_button(self):
        self.personal_logout_account_button.click()
        time.sleep(1)

    def code(self, value):
        self.account_code.send_keys(value)
        time.sleep(1)

class Rostelecombutton(BasePage):
    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        self.website = driver.find_element(*RostelecombuttonLocators.acc_rostelecom_website)
        self.internet = driver.find_element(*RostelecombuttonLocators.acc_rostelecom_internet_button)
        self.news = driver.find_element(*RostelecombuttonLocators.acc_rostelecom_news_button)
        self.office = driver.find_element(*RostelecombuttonLocators.acc_rostelecom_office_button)
        self.office_Tele2 = driver.find_element(*RostelecombuttonLocators.acc_rostelecom_office_button_Tele2)

    def website_button(self):
        self.website.click()
        time.sleep(1)

    def internet_button(self):
        self.internet.click()
        time.sleep(1)

    def news_button(self):
        self.news.click()
        time.sleep(1)

    def office_button(self):
        self.office.click()
        time.sleep(1)

    def office_Tele2_button(self):
        self.office_Tele2.click()
        time.sleep(1)