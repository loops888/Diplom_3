import requests

from data import *

import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import constants
from locators.login_page_locators import LoginPageLocators
from locators.main_page_locators import MainPageLocators


@pytest.fixture(scope='function', params=['chrome', 'firefox'])
def driver(request):
    global driver
    if 'chrome' in request.param:
        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=options)
        driver.get(constants.Constants.URL)

    elif 'firefox' in request.param:
        options = webdriver.FirefoxOptions()
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        driver = webdriver.Firefox(options=options)
        driver.get(constants.Constants.URL)

    yield driver
    driver.quit()


@pytest.fixture
def login(driver, generate_user_register_and_delete_by_api):
    email = generate_user_register_and_delete_by_api[0]
    password = generate_user_register_and_delete_by_api[1]
    driver.find_element(*LoginPageLocators.PERSONAL_ACCOUNT_LINK).click()
    driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(email)
    driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(password)
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(
        MainPageLocators.MAIN_PAGE))
    return driver


@pytest.fixture
def generate_user_register_and_delete_by_api():
    data = generate_info_for_registration()

    payload = {
        'email': data[0],
        'password': data[1],
        'name': data[2]
    }
    registration_response = requests.post(f'{constants.Constants.URL + constants.Constants.CREATE_USER}', json=payload)
    registration_info = []
    if registration_response.status_code == 200:
        registration_info.append(data[0])
        registration_info.append(data[1])
        registration_info.append(data[2])

    yield registration_info

    payload = {
        'email': data[0],
        'password': data[1]
    }
    login_response = requests.post(f'{constants.Constants.URL + constants.Constants.LOGIN_USER}', json=payload)
    token = login_response.json()['accessToken']
    headers = {
        "Authorization": token
    }
    requests.delete(f'{constants.Constants.URL + constants.Constants.INFO_USER}', headers=headers)
