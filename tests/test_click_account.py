from data.data import Data
from locators import RegistrationLocators, EnterLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestClickAccount:
    def test_click_account(self, driver): # тест успешного входа в личный кабинет по клику на кнопку «Личный кабинет»
        
        # открываем главную страницу
        driver.get(Data.BURGERS_URL)
        # Находим кнопку "Личный кабинет", кликаем на нее
        burgers_enter = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(RegistrationLocators.BUTTON_PERSONAL_ACCOUNT)
        )
        burgers_enter.click()
         # находим поле Email и вводим логин - зарегистрированный email
        login_email_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(EnterLocators.NAME))
        login_email_input.send_keys(Data.EMAIL_REGISTERED)
        
        # находим поле Пароль и вводим зарегистрированный пароль
        login_password_input = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(EnterLocators.PASS))
        login_password_input.send_keys(Data.PASSWORD_REGISTERED)
        
        # нажимаем кнопку "Вход"
        enter_user = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(RegistrationLocators.ENTER))
        enter_user.click()
        # Находим кнопку "Личный кабинет", кликаем на нее еще раз, чтоыб перейти в личный кабинет
        burgers_enter = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(RegistrationLocators.BUTTON_PERSONAL_ACCOUNT))
        burgers_enter.click()
        # Проверяем, что появилась кнопка "Выход" в личном кабинете
        button_exit = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(EnterLocators.BUTTON_EXIT))
        assert button_exit.text == "Выход"