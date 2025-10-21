# Константы для операторов
BINARY_OPERATORS = ["+", "-", "*", "/", "**", "//", "%"]
UNARY_MINUS = "~"
UNARY_PLUS = "^"
OPEN_SKOB = "("
CLOSE_SKOB = ")"

# ошибки
EMPTY = "нехватка данных"
NO_NUMBER = "нет числа для унарного минуса"
NUMBERS = "нехватка чисел(мин 2 числа)"
ZERO = "деление на ноль запрещено"
SKOB_ORDER = "неверный порядок скобок: ')' перед '('"
SKOB_COUNT = "неверное использование скобок: открывающих {left}, закрывающих {right}"
SKOB_INPUT = "'(' - неподходящий ввод"
INVALID = "'{part}' - неподходящий ввод"
STACK_EMPTY = "пустой стек"
STACK_MANY = "в стеке {count} числа"

# Константы для чисел
MIN_STACK_SIZE_UNARY = 1
MIN_STACK_SIZE_BINARY = 2
EXPECTED_STACK_SIZE = 1

# Константы для регулярных выражений
NUMBER_PATTERN = r'^[+-]?\d*\.?\d+$'
