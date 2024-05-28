import allure

from locators.recovery_page_locators import RecoveryPageLocators
from pages.base_page import BasePage


class RecoveryPage(BasePage):

    @allure.step('Переходим в окно восстановления пароля.')
    def go_to_recovery_window(self):
        self.click_on_element(RecoveryPageLocators.PASSWORD_RECOVERY_LINK)
        return self.get_text_from_element(RecoveryPageLocators.RECOVERY_BUTTON)

    @allure.step('Переходим в окно с предложением ввода кода восстановления.')
    def go_to_recovery_confirm_window(self):
        self.click_on_element(RecoveryPageLocators.RECOVERY_BUTTON)
        return self.get_text_from_element(RecoveryPageLocators.RECOVERY_CODE_FIELD)

    @allure.step('Изменяем видимость пароля, чтобы убрать маску с поля.')
    def change_password_visibility(self):
        self.click_on_element(RecoveryPageLocators.PASSWORD_VISIBILITY)
        return self.get_attribute_value(RecoveryPageLocators.RECOVERY_PASSWORD_FIELD, 'type')
