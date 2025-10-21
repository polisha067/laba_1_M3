from src.calculator_M3 import *
from src.clas import *


def my_tests() -> None:
    """
    Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
    :return: Данная функция ничего не возвращает
    """

    test_cases = [
        "2 4 +",               # 2+4=6
        "5 5 *",               #5*5=25
        "10 2 /",              #10/2=5
        "2 3 **",              #2**3=8
        "2 3 4 * +",           #2+3*4=14
        "( 5 2 - ) 10 +",      #(5-2)+10=13
        "2 2.5 +",             #2+2.5=4.5
        "2 ^ 2 +",             #+2+2=4
        "5 ~ 2 +",             #-5+2=-3
    ]

    passed = 0
    for expr, expected in test_cases:
        try:
            result = calculat(expr)
            ok = abs(result - expected) < 1e-9
            status = "OK" if ok else "FAIL"
            print(f"{status}: {expr} => {result} (ожидалось {expected})")
            if ok:
                passed += 1
        except CaError as e:
            print(f"FAIL: {expr} => Ошибка: {e.message}")

    print(f"\nуспешно: {passed}/{len(test_cases)}")


if __name__ == "__main__":
    my_tests()
