from calculator_M3 import *
from clas import *


def main() -> None:
    """
    Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
    :return: Данная функция ничего не возвращает
    """
    exp = input()
    try:
        print(calculat(exp))
    except CaError as e:
        print(f"Ошибка: {e.message}")


if __name__ == "__main__":
    main()
