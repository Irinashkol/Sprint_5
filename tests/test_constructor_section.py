from data.data import Data
from locators import RegistrationLocators, TestConstructor
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestAssemblyTheBurger:
    def test_constructor_buns(self, driver): # проверяет переход к разделу «Булки»
        
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
        # проверяем, что после перехода на главную страницу конструктора по умолчанию активна вкладка "Булки"
        buns_active = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestConstructor.BUNS_ACTIVE))

        class_active = buns_active.get_attribute("class")
        # проверяем, что в класс соответствует активному
        assert "tab_tab_type_current" in class_active

    def test_constructor_sauces(self, driver): # проверяет переход к разделу «Соусы»

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
        # находим вкладку соусы и кликаем на нее
        sauces = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(TestConstructor.SAUCES))
        sauces.click()
        class_active_sauces = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestConstructor.SAUCES_ACTIVE)) 
        # Проверяем, что элемент отобразился на странице
        assert class_active_sauces.is_displayed()

    def test_constructor_topping(self, driver): # проверяет переход к разделу «Начинки»

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
        # находим вкладку соусы и кликаем на нее
        topping = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(TestConstructor.TOPPING))
        topping.click()
        class_active_topping = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestConstructor.TOPPING_ACTIVE)) 
        # Проверяем, что элемент отобразился на странице
        assert class_active_topping.is_displayed()

    
    