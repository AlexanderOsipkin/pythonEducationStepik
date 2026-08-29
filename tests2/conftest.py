import pytest


@pytest.fixture()
def set_up():
    print("Вход в систему")
    yield  # все что выше - выполняется до теста, все что ниже - после теста
    print("Выход из системы")


@pytest.fixture()
def sum():
    print("Начало")
    yield
    print("Конец")
