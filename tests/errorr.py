import logging
from src.calculator_M3 import *
from src.clas import *


def error() -> None:
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(name)s: %(message)s')
    error_cases = [
        "2 +",            # нехватка чисел
        "5 5 * +",        # лишний оператор или операнд
        " ",              # пустой ввод
        "&",              # неподходящий символ
        "2 5 ++",         # двойной оператор
        "2 + 2 + 5",      # привычный ввод вместо Польской нотации
        "5 / 0",          # деление на ноль
        "5 5 5 +",        # лишнее число
        ") 2 (",          # неправильный порядок скобок )(
        "( 2 ) )",        # лишняя закрывающая скобка
        "( ( 2 +",        # лишняя открывающая скобка
    ]

    for expr in error_cases:
        print(f"\n{expr}")
        try:
            result = calculat(expr)
            print(f"Ответ: {result}")
        except CaError as e:
            print(f"Ошибка: {e.message}")


if __name__ == "__main__":
    error()
