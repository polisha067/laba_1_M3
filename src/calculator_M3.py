import re 
from clas import *
from const import *


def main():
    
    while True:
        user_input = input("\nВвод: ").strip()
        
        # пустой ввод
        if not user_input:
            print(f"Ошибка: {EMPTY}")
            continue
        
        # обрабатываем выражение
        try:
            result = calculat(user_input)
            print(f"Ответ: {result}")
        except CaError as e:
            print(f"Ошибка: {e.message}")


# функция для скобок
def scob(expression):
    parts = expression.split()
    left_count = 0
    right_count = 0
    
    for part in parts:
        if part == OPEN_SKOB:
            left_count += 1
        elif part == CLOSE_SKOB:
            right_count += 1
            # проверяем, что закрывающая скобка не идет раньше открывающей
            if right_count > left_count:
                raise CaError(SKOB_ORDER)
    
    # проверяем равенство количества скобок
    if left_count != right_count:
        raise CaError(SKOB_COUNT.format(left=left_count, right=right_count))


# сам калькулятор
def calculat(expression):
    # проверка скобок
    scob(expression)
    
    tokens = expression.split()
    stack = []
    i = 0
    
    while i < len(tokens):
        token = tokens[i]
        
        if is_number(token):
            stack.append(float(token))
        
        elif token == UNARY_MINUS:
            if len(stack) < MIN_STACK_SIZE_UNARY:
                raise CaError(NO_NUMBER)
            num = stack.pop()
            stack.append(-num)
        
        elif token == UNARY_PLUS:
            # Унарный плюс ничего не меняет
            pass
        
        elif token in BINARY_OPERATORS:
            if len(stack) < MIN_STACK_SIZE_BINARY:
                raise CaError(NUMBERS)
            
            num2 = stack.pop()
            num1 = stack.pop()
            
            if token == "+":
                result = num1 + num2
            elif token == "-":
                result = num1 - num2
            elif token == "*":
                result = num1 * num2
            elif token == "/":
                if num2 == 0:
                    raise CaError(ZERO)
                result = num1 / num2
            elif token == "**":
                result = num1 ** num2
            elif token == "//":
                if num2 == 0:
                    raise CaError(ZERO)
                result = num1 // num2
            elif token == "%":
                if num2 == 0:
                    raise CaError(ZERO)
                result = num1 % num2
            
            stack.append(float(result))
        
        elif token == OPEN_SKOB:
            
            balance = 1
            j = i + 1
            sub_tokens = []
            
            while j < len(tokens) and balance > 0:
                if tokens[j] == OPEN_SKOB:
                    balance += 1
                elif tokens[j] == CLOSE_SKOB:
                    balance -= 1
                
                if balance > 0:  
                    sub_tokens.append(tokens[j])
                
                j += 1
            
            if balance != 0:
                raise CaError(SKOB_INPUT)
            
            # рекурсивно вычисляем подвыражение в скобках
            sub_expression = ' '.join(sub_tokens)
            sub_result = calculat(sub_expression)
            stack.append(sub_result)
            
            # переходим на позицию после закрывающей скобки
            i = j - 1
        
        elif token == CLOSE_SKOB:
            raise CaError(SKOB_ORDER)
        
        else:
            raise CaError(INVALID.format(part=token))
        
        i += 1
    
    if len(stack) == EXPECTED_STACK_SIZE:
        return stack[0]
    elif len(stack) == 0:
        raise CaError(STACK_EMPTY)
    else:
        raise CaError(STACK_MANY.format(count=len(stack)))


def is_number(text):
    # проверяет является ли текст числом
    if re.match(NUMBER_PATTERN, text):
        return True
    else:
        return False

if __name__ == "__main__":
    main()
