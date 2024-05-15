import allure

from locators.account_page_locators import AccountPageLocators
from pages.base_page import BasePage


class AccountPage(BasePage):
    @allure.step('Проверяем видимость профиля по клику на «Личный кабинет».')
    def go_to_personal_account_window(self):
        self.click_on_element(AccountPageLocators.PERSONAL_ACCOUNT_LINK)
        return self.get_text_from_element(AccountPageLocators.ACCOUNT_PROFILE_LINK)

    @allure.step('Проверяем видимость истории по клику на «История заказов» из личного кабинета.')
    def go_to_personal_orders_history(self):
        self.go_to_personal_account_window()
        self.click_on_element(AccountPageLocators.ACCOUNT_HISTORY_LINK)
        return self.get_attribute_value(AccountPageLocators.ACCOUNT_HISTORY_ACTIVE, 'aria-current')

    @allure.step('Проверяем выход из аккаунта.')
    def log_out_from_personal_account(self):
        self.go_to_personal_account_window()
        self.click_on_element(AccountPageLocators.ACCOUNT_EXIT_LINK)
        return self.get_text_from_element(AccountPageLocators.LOGIN_WINDOW)
