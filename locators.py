from selenium.webdriver.common.by import By


class RegistrationLocators:  # Для тестирования регистрации.
    # Кнопка "Личный кабинет" на главной странице
    BUTTON_PERSONAL_ACCOUNT = (By.XPATH, "//p[normalize-space()='Личный Кабинет']")

    # Личный кабинет/ссылка "Зарегистрироваться" для начала регистрации (кнопка/ссылка без границ)
    REGISTRATION_BUTTON = (By.LINK_TEXT, "Зарегистрироваться")

    # Поля формы регистрации:
    # Поле "Имя"  привязываемся в элементу input следующему за элементом label, который содержит текст "Имя", normalize-space() удаляет лишние пробелы
    NAME_INPUT = (By.XPATH, "//label[normalize-space()='Имя']/following-sibling::input")

    # Поле "Email" привязываемся в элементу input следующему за элементом label, который содержит текст "Email", normalize-space() удаляет лишние пробелы
    EMAILE_INPUT = (By.XPATH, "//label[normalize-space()='Email']/following-sibling::input")

    # поле "Пароль" привязываемся в элементу input следующему за элементом label, который содержит текст "Email", normalize-space() удаляет лишние пробелы
    PASS_INPUT = (By.XPATH, "//label[normalize-space()='Пароль']/following-sibling::input")

    # Форма регистрации. Кнопка "Зарегистрироваться"
    REGISTRATION = (By.XPATH, "//button[normalize-space()='Зарегистрироваться']")

    # Страница входа в аккаунт. Кнопка "Войти"
    ENTER = (By.XPATH, "//button[normalize-space()='Войти']")

    # кнопка "Оформить заказ" в личном кабинете (для подтверждения, что мы, действительно, попали в личный кабинет)
    ORDER = (By.XPATH, "//button[normalize-space()='Оформить заказ']")

    # ошибка при вводе некорректого пароля с текстом "Некорректный пароль"
    MISTAKE = (By.XPATH, "//p[normalize-space()='Некорректный пароль']")

    # кнопка "Войти в аккаунт" на главной странице
    LOG_IN_TO_THE_ACCOUNT = (By.XPATH, "//button[normalize-space()='Войти в аккаунт']")

class EnterLocators:  # Для тестирования входа и выхода.

    # Поле Email (логин для входа) на странице Входа в аккаунт
    NAME = (By.XPATH, "//label[normalize-space()='Email']/following-sibling::input")

    # Поле Пароль на странице Входа в аккаунт
    PASS = (By.XPATH, "//label[normalize-space()='Пароль']/following-sibling::input")

    # кнопка/ссылка "Войти" на странице регистрации
    BUTTON_ENTER_REGISTRATION = (By.LINK_TEXT, "Войти")

    # ссылка для входа через Восстановление пароля
    REGENERATE_PASSWORD_LINK = (By.LINK_TEXT, "Восстановить пароль")

    # надпись "Восстаноление пароля" для подтверждения перехода на страницу регистрации
    TITLE_REGENERATE = (By.XPATH, "//h2[contains(normalize-space(), 'Восстановление пароля')]")

    # кнопка "Восстановить" в форме восстаноления пароля
    BUTTON_RECOVER = (By.XPATH, "//button[normalize-space()='Восстановить']")

    # Поле для ввода кода, для  восстановления пароля
    CODE = (By.XPATH, "//label[normalize-space()='Введите код из письма']/following-sibling::input")

    # кнопка/ссылка "Войти" на странице восстановления пароля
    BUTTON_ENTER = (By.LINK_TEXT, "Войти")

    # Кнопка "Выйти" в личном кабинете
    BUTTON_EXIT = (By.XPATH, "//button[normalize-space()='Выход']")

class TestConstructor:  # Для тестирования Коструктора
    # Кнопка "Личный кабинет" на главной странице
    BUTTON_CONSTRUCTOR = (By.XPATH, "//p[normalize-space()='Конструктор']")

    # Кнопка/ссылка логотип Stellar Burgers
    BUTTON_STELLAR_BURGERS = (By.XPATH, "//div[contains(@class, 'header__logo')]//a[@href='/']")

    # Коструктор. Вкладка "Булки"
    BUNS = (By.XPATH,"//span[normalize-space()='Булки']")

    # Вкладка "Булки" в активном состоянии
    BUNS_ACTIVE = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current') and .//span[normalize-space()='Булки']]")
    # Конструктор. Вкладка "Соусы"
    SAUCES = (By.XPATH,"//span[normalize-space()='Соусы']")

    # Вкладка "Соусы" в активном состоянии
    SAUCES_ACTIVE = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current') and .//span[normalize-space()='Соусы']]")
    
    # Конструктор. Вкладка "Начинки"
    TOPPING = (By.XPATH,"//span[normalize-space()='Начинки']")
    #  Вкладка "Начинки" в активном состоянии
    TOPPING_ACTIVE = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current') and .//span[normalize-space()='Начинки']]")