from calculator_M3 import calculat
from calculator_M3 import main

def main() -> None:
    """
    Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
    :return: Данная функция ничего не возвращает
    """
    exp = input()
    print(calculat(exp))


if __name__ == "__main__":
    main()
