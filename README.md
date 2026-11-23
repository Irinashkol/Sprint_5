Проект Sprint_5

Для тестов с уже зарегитрированными данными логин irina_shkolnikova_59_123@yandex.ru и пароль QWErty098!, имя и короткий пароль вынесены в файл data.py

Регистрация тесты class TestLogin файл test_registration.py

1) test_registration  проверяет возможность регистрации аккаунта при введении корректных данных

2) test_registration_short_password_mistake.py проверяет что возникает ошибка с текстом:"Некорректный пароль" при попытке зарегистрироваться с паролем длиной менее 6ти знаков

Вход тесты class TestLoginEnter файл test_enter_log_in_to_the_account.py

3) test_enter_log_in_to_the_account проверяет вход по кнопке «Войти в аккаунт» на главной странице

4) test_enter_personal_cabinet проверяет вход через кнопку «Личный кабинет»

5) test_enter_in_registration_form проверяет вход через кнопку в форме регистрации

6) test_enter_regenerate  проверяет вход через кнопку/ссылку "Войти" в форме восстановления пароля

Переход в личный кабинет тест class TestClickAccount файл test_click_account.py

7) test_click_account проверяет переход по клику на «Личный кабинет»

 Переход из личного кабинета в конструктор class TestConstructorEnter файл test_transition_constructor.py

8) test_transition_constructor проверяет переход по клику на «Конструктор»

9) test_transition_constructor_logotip проверяет переход по клику на логотип Stellar Burgers

 Выход из аккаунта тест class TestAccountExit файл test_account_exit.py

10) test_account_exit проверяет выход по кнопке «Выйти» в личном кабинете.

Раздел «Конструктор» тесты class TestAssemblyTheBurger файл test_constructor_section.py.

11) test_constructor_buns проверяет переход к разделу «Булки»
12) test_constructor_sauces проверяет переход к разделу «Соусы»
13) test_constructor_topping проверяет переход к разделу «Начинки»