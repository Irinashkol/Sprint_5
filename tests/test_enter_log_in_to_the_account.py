from data.data import Data
from locators import RegistrationLocators, EnterLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from generators import generate_random_credentials

class TestLoginEnter:
    def test_enter_log_in_to_the_account(self, driver): # тест успешного входа в личный кабинет через кнопку «Войти в аккаунт» на главной странице
        # открываем главную страницу
        driver.get(Data.BURGERS_URL)
         # Находим кнопку "Войти в аккаунт», кликаем на нее
        log_in_enter = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(RegistrationLocators.LOG_IN_TO_THE_ACCOUNT))
        log_in_enter.click()
        # заполняем поле 'Email' (вводим уже ранее зарегистрированный email)
        email_input = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(RegistrationLocators.EMAILE_INPUT))
        email_input.send_keys(Data.EMAIL_REGISTERED)

        # заполняем поле "Пароль" (вводим уже ранее зарегистрированный пароль)
        password_input = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(RegistrationLocators.PASS_INPUT))
        password_input.send_keys(Data.PASSWORD_REGISTERED)
        # кликаем на кнопку "Войти"
        enter_user = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(RegistrationLocators.ENTER))
        enter_user.click()
        # проверяем наличие кнопки "Оформить заказ"
        order = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegistrationLocators.ORDER))
        assert order.text == "Оформить заказ"
        
    def test_enter_personal_cabinet(self, driver): # тест успешного входа в личный кабинет через кнопку «Личный кабинет» на главной странице
    
        # открываем главную страницу
        driver.get(Data.BURGERS_URL)

        # Находим кнопку "Личный кабинет", кликаем на нее
        burgers_enter = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(RegistrationLocators.BUTTON_PERSONAL_ACCOUNT))
        burgers_enter.click()

        # заполняем поле 'Email' (вводим уже ранее зарегистрированный email)
        email_input = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(RegistrationLocators.EMAILE_INPUT))
        email_input.send_keys(Data.EMAIL_REGISTERED)

        # заполняем поле "Пароль" (вводим уже ранее зарегистрированный пароль)
        password_input = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(RegistrationLocators.PASS_INPUT))
        password_input.send_keys(Data.PASSWORD_REGISTERED)

        # кликаем на кнопку "Войти"
        enter_user = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(RegistrationLocators.ENTER))
        enter_user.click()
        
        # проверяем наличие кнопки "Оформить заказ"
        order = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegistrationLocators.ORDER))
        assert order.text == "Оформить заказ"

    def test_enter_in_registration_form(self, driver):# тест успешного входа в личный кабинет через кнопку Войти в форме регистрации

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
        # находим кнопку/ссылку "Войти", нажимаем на нее
        button_enter_registration = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(EnterLocators.BUTTON_ENTER_REGISTRATION))
        button_enter_registration.click()

        # находим поле Email и вводим уже зарегистрированный логин - email
        login_email_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(EnterLocators.NAME))
        login_email_input.send_keys(Data.EMAIL_REGISTERED)

        # находим поле Пароль и вводим уже зарегистрированный пароль
        login_password_input = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(EnterLocators.PASS))
        login_password_input.send_keys(Data.PASSWORD_REGISTERED)

        # нажимаем кнопку "Вход"
        enter_user = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(RegistrationLocators.ENTER))
        enter_user.click()
        
        # проверяем, что вошли в аккаунт наличием кнопки "Оформить заказ"
        order = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegistrationLocators.ORDER))
        assert order.text == "Оформить заказ"

    def test_enter_regenerate(self, driver): # проверяет вход через кнопку "Войти" в форме восстановления пароля
        
        # открываем главную страницу
        driver.get(Data.BURGERS_URL)
        # Находим кнопку "Войти в аккаунт», кликаем на нее
        log_in_enter = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(RegistrationLocators.LOG_IN_TO_THE_ACCOUNT))
        log_in_enter.click()
        # заполняем поле 'Email' (вводим уже ранее зарегистрированный email)
        email_input = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(RegistrationLocators.EMAILE_INPUT))
        email_input.send_keys(Data.EMAIL_REGISTERED)
        # Находим ссылку "Восстановить пароль" и кликаем на нее
        regenerate_password_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(EnterLocators.REGENERATE_PASSWORD_LINK))
        regenerate_password_link.click() 
        # Проверяем, что попали на страницу Восстановления пароля
        
        title_regeration = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(EnterLocators.TITLE_REGENERATE))
        assert title_regeration.text == "Восстановление пароля"
        # находим кнопку/ссылку "Войти" и нажимаем
        regenerate_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(EnterLocators.BUTTON_ENTER))
        regenerate_link.click()
        
        # заполняем поле 'Email' (вводим уже ранее зарегистрированный email)
        email_input = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(RegistrationLocators.EMAILE_INPUT))
        email_input.send_keys(Data.EMAIL_REGISTERED)
        
        # заполняем поле "Пароль" (вводим уже ранее зарегистрированный пароль)
        password_input = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(RegistrationLocators.PASS_INPUT))
        password_input.send_keys(Data.PASSWORD_REGISTERED)
        
        # кликаем на кнопку "Войти"
        enter_user = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(RegistrationLocators.ENTER))
        enter_user.click()
                
        # проверяем наличие кнопки "Оформить заказ"
        order = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegistrationLocators.ORDER))
        assert order.text == "Оформить заказ"