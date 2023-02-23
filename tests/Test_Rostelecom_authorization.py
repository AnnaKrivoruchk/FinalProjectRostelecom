import pytest
import selenium
from pages.base import BasePage
from pages.Rostelecom import AuthPage, InAccount, Rostelecombutton
from pages.locators import AuthLocators, AccountLocators, RostelecombuttonLocators
from setting import email, password, login, phone
from params import generate_invalid_string, invalid_mail, invalid_login, invalid_phone, LOGIN_URL


@pytest.mark.negative
@pytest.mark.logging
def test_authorization_invalid_phone_number(browser):
    # Авторизация по невалидному номеру телефона
    page = AuthPage(browser)
    page.choose_phone()
    page.entery_form(invalid_phone(phone))
    page.entery_pass(password)
    page.button_enter()
    assert page.find_element(AuthLocators.auth_log)

@pytest.mark.positive
@pytest.mark.logging
def test_authorization_valid_phone_number(browser):
    # Авторизация по валидному номеру телефона
    page = AuthPage(browser)
    page.choose_phone()
    page.entery_form(phone)
    page.entery_pass(password)
    page.button_enter()
    assert page.find_element(AccountLocators.acc_password)


@pytest.mark.negative
@pytest.mark.logging
def test_authorization_invalid_mail_minus_three(browser) :
# Авторизация по невалидной электронной почте
    page = AuthPage(browser)
    page.choose_email()
    page.entery_form(invalid_mail(email))
    page.entery_pass(password)
    page.button_enter()
    assert page.find_element(AuthLocators.auth_log)

@pytest.mark.negative
@pytest.mark.logging
def test_authorization_invalid_mail_thousand(browser) :
# Авторизация по невалидной электронной почте
    page = AuthPage(browser)
    page.choose_email()
    page.entery_form(generate_invalid_string(1000))
    page.entery_pass(password)
    page.button_enter()
    assert page.find_element(AuthLocators.auth_log)

@pytest.mark.positive
@pytest.mark.logging
def test_authorization_valid_mail(browser):
    # Авторизация по валидноq электронной почте
    page = AuthPage(browser)
    page.choose_email()
    page.entery_form(email)
    page.entery_pass(password)
    page.button_enter()
    assert page.find_element(AccountLocators.acc_password)


@pytest.mark.negative
@pytest.mark.logging
def test_authorization_invalid_login_minus_three(browser) :
# Авторизация по невалидному логину
    page = AuthPage(browser)
    page.choose_login()
    page.entery_form(invalid_login(login))
    page.entery_pass(password)
    page.button_enter()
    assert page.find_element(AuthLocators.auth_log)

@pytest.mark.negative
@pytest.mark.logging
def test_authorization_invalid_login_thousand(browser) :
# Авторизация по невалидному логину
    page = AuthPage(browser)
    page.choose_login()
    page.entery_form(generate_invalid_string(1000))
    page.entery_pass(password)
    page.button_enter()
    assert page.find_element(AuthLocators.auth_log)

@pytest.mark.positive
@pytest.mark.logging
def test_authorization_valid_login(browser):
    # Авторизация по валидному логину
    page = AuthPage(browser)
    page.choose_login()
    page.entery_form(login)
    page.entery_pass(password)
    page.button_enter()
    assert page.find_element(AccountLocators.acc_password)


@pytest.mark.positive
@pytest.mark.logging
def test_authorization_VK(browser):
    # Авторизация по через вконтакте
    page = AuthPage(browser)
    page.authVK()
    assert page.find_element(AccountLocators.acc_password)

@pytest.mark.positive
@pytest.mark.logging
def test_authorization_ok(browser):
    # Авторизация через вконтакте
    page = AuthPage(browser)
    page.authOK()
    assert page.find_element(AccountLocators.acc_password)

@pytest.mark.positive
@pytest.mark.logging
def test_authorization_mail(browser):
    # Авторизация через аккаунт мэил.ру
    page = AuthPage(browser)
    page.authMAIL()
    assert page.find_element(AccountLocators.acc_password)

@pytest.mark.positive
@pytest.mark.logging
def test_authorize_Google(browser):
    # Авторизация через аккаунт гугл
    page = AuthPage(browser)
    page.authGoogl()
    assert page.find_element(AccountLocators.acc_password)

@pytest.mark.positive
@pytest.mark.logging
def test_authorization_Yandex(browser):
    # Авторизация через аккаунт яндекс
    page = AuthPage(browser)
    page.authYandex()
    assert page.find_element(AccountLocators.acc_password)

@pytest.mark.positive
@pytest.mark.scenario
def test_scenario_user_agreement(browser):
    # Сценарий "Читаю пользовательское соглашение"
    page = AuthPage(browser)
    page.useragreement()
    assert page.get_relative_link() != LOGIN_URL

@pytest.mark.positive
@pytest.mark.scenario
def test_scenario_mail_is_not_a_login(browser):
    # Сценарий "Я думал почта - это логин"
    page = AuthPage(browser)
    page.choose_login()
    page.entery_form(email)
    page.entery_pass(password)
    assert page.find_element(AuthLocators.auth_email)
