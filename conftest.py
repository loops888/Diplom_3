import requests

from helpers import *

import pytest
from selenium import webdriver

import constants
from pages.login_page import LoginPage
from pages.main_page import MainPage


@pytest.fixture(scope='function', params=['chrome', 'firefox'])
def driver(request):
    if 'chrome' in request.param:
        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=options)

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

    main_page = MainPage(driver)
    login_page = LoginPage(driver)

    main_page.go_to_personal_account()
    login_page.print_user_email(email)
    login_page.print_user_password(password)
    login_page.confirm_user_authorization()
    main_page.wait_for_main_page()
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
