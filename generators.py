
import random
from faker import Faker

faker = Faker()

def generate_random_credentials(): # создаем переменные email и password

    random_number = random.randint(100, 999) # создаем рандомное трехзначное число для email

    email = f"irina_shkolnikova_59_{random_number}@ya.ru"

    password = faker.password(length=10, special_chars=True, digits=True)
    return email, password