import allure
from faker import Faker

faker = Faker()


@allure.step('Генерируем данные для регистрации пользователя.')
def generate_info_for_registration():
    email = faker.email()
    password = faker.password()
    name = faker.name()
    return email, password, name
