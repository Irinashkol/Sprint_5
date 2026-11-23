from data.data import Data
from locators import RegistrationLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from generators import generate_random_credentials

class TestLogin:
    def test_registration(self, driver):
        
        # тест успешного входа в личный кабинет
        # создаем переменные email, password из файла generators через функцию generate_random_credentials()
        email, password = generate_random_credentials()
        # открываем главную страницу
        driver.get(Data.BURGERS_URL)
        # Находим кнопку "личный кабинет", кликаем на нее
        burgers_enter = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(RegistrationLocators.BUTTON_PERSONAL_ACCOUNT)
        )
        burgers_enter.click()
        # находим на странице ссылку "Зарегистрироваться" кликаем на нее
        registration = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(RegistrationLocators.REGISTRATION_BUTTON)
        )
        registration.click()

        # заполняем поле "Имя"
        name_input = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(RegistrationLocators.NAME_INPUT)
        )
        name_input.send_keys(Data.NAME_REGISTRERED)

        # заполняем поле 'Email'
        email_input = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(RegistrationLocators.EMAILE_INPUT)
        )
        email_input.send_keys(email)

        # заполняем поле "Пароль"
        password_input = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(RegistrationLocators.PASS_INPUT)
        )
        password_input.send_keys(password)

        #  нажимаем кнопку "Зарегистрироваться"
        registration_user = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(RegistrationLocators.REGISTRATION)
        )
        registration_user.click()

        # проверяем наличие кнопки "Войти"
        enter_user = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(RegistrationLocators.ENTER)
        )
        assert enter_user.text == "Войти"

    def test_short_password_mistake(self, driver): # проверяет что возникает ошибка с текстом:"Некорректный пароль" при попытке зарегистрироваться с паролем длиной менее 6ти знаков
        # создаем переменные email, password из файла generators через функцию generate_random_credentials()
        email = generate_random_credentials()
        # тест успешного входа в личный кабинет
        # открываем главную страницу
        driver.get(Data.BURGERS_URL)
        # Находим кнопку "личный кабинет", кликаем на нее
        burgers_enter = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(RegistrationLocators.BUTTON_PERSONAL_ACCOUNT)
        )
        burgers_enter.click()
        # находим на странице ссылку "Зарегистрироваться" кликаем на нее
        registration = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(RegistrationLocators.REGISTRATION_BUTTON)
        )
        registration.click()

        # заполняем поле "Имя"
        name_input = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(RegistrationLocators.NAME_INPUT)
        )
        name_input.send_keys(Data.NAME_REGISTRERED)

        # заполняем поле 'Email'
        email_input = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(RegistrationLocators.EMAILE_INPUT)
        )
        email_input.send_keys(email)

        # заполняем поле "Пароль" паролем QWE8! длиной менее 6ти символов.
        password_input = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(RegistrationLocators.PASS_INPUT)
        )
        password_input.send_keys(Data.PASSWORD_SHORT)

        #  нажимаем кнопку "Зарегистрироваться"
        registration_user = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(RegistrationLocators.REGISTRATION)
        )
        registration_user.click()

        # проверяем наличие ошибки с текстом "Некорректный пароль"
        mistake_user = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(RegistrationLocators.MISTAKE)
        )
        assert mistake_user.text == "Некорректный пароль"