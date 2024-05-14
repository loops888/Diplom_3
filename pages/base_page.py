import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from faker import Faker

faker = Faker()


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Скроллим к элементу')
    def scroll_to_element(self, locator):
        element = self.find_element_with_waiting(locator)
        self.driver.execute_script("return arguments[0].scrollIntoView();", element)

    @allure.step('Кликаем по элементу')
    def click_on_element(self, locator):
        element = self.find_element_with_waiting(locator)
        self.driver.execute_script("arguments[0].click();", element)
        element = self.find_element_with_waiting(locator)
        ActionChains(self.driver).move_to_element(element).click(element).perform()

    @allure.step('Кликаем по элементу с доп.ожиданием')
    @allure.description(
        'Добавлен для окна восстановления пароля - по методу выше почему-то только в нем не находятся элементы, но для других окон через click_on_element работает стабильнее.')
    def click_on_expected_element(self, locator):
        element = self.find_element_with_waiting(locator)
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        element.click()

    @allure.step('Ищем элемент с ожиданием.')
    def find_element_with_waiting(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Получаем текст из элемента.')
    def get_text_from_element(self, locator):
        element = self.find_element_with_waiting(locator)
        return element.text

    @allure.step('Форматируем элемент.')
    def format_locator(self, locator, num):
        method, locator_final = locator
        locator_final = locator_final.format(num)
        return method, locator_final

    @allure.step('Заполняем элемент текстом.')
    def insert_text_in_field(self, locator, value):
        element = WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        element.send_keys(value)

    @allure.step('Получением значение определенного аттрибута.')
    def get_attribute_value(self, locator, attribute):
        element = self.find_element_with_waiting(locator)
        return element.get_attribute(attribute)

    @allure.step('Перетаскиваем элемент.')
    def drag_and_drop_element(self, source_locator, target_locator):
        source_element = self.find_element_with_waiting(source_locator)
        target_element = self.find_element_with_waiting(target_locator)
        action = ActionChains(self.driver)
        action.drag_and_drop(source_element, target_element).perform()
