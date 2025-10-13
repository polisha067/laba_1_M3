import re 

def main():
    
    
    while True:

        user_input = input("\nВвод: ").strip()
        
        # пустой ввод
        if not user_input:
            print("нехватка данных")
            continue
        
        # обрабатываем выражение
        result = calculat(user_input)
        
        if result is not None:
            print(f"Ответ: {result}")
        else:
            print("Не выполнено")


# функция для скобок
def scob(stack) :
    
    left = list(filter(lambda x: x == '(', stack))
    right = list(filter(lambda x: x == ')', stack))
    
    if len(left) != len(right):
        print(f"ошибка: - неподходящий ввод")
        return None
    else:
        pass




#сам калькулятор
#он принимает строку и возвращает ответ или ошибку

def calculat(expression):

    
    # разбиваем строку на части по пробелам
    parts = expression.split()
    

    stack = []
    
    
    i = 0
    
    # обработка
    while i < len(parts):
        part = parts[i]
        
        
        if is_number(part):
       
            num = float(part)
            stack.append(num)
        
        
        # обрвботка унарного минуса
        elif part == "~":
            if len(stack) < 1:
                print("Ошибка: нет числа для унарным минусом")
                return None
           
            num = stack.pop()
            result = -num
            stack.append(result)
            print(f"унарный минус в выражении: ~{num} = {result}")

       
        # обработка, а точнее НЕобработка унарного плюса, пропуск его в выражении    
        elif part == "^":
            print(f"унарный плюс '^'")
            
            
        elif part in ["+", "-", "*", "/", "**", "//", "%"]:
            
            
            
            if len(stack) < 2:
                print("Нехватка чисел(мин 2 числа)")
                return None
            
            
            
            # два последних числа из стека
            num2 = stack.pop()  # сверху стека (последний)
            num1 = stack.pop()  # следующий
            
            
            
            # основные операции
            if part == "+":
                result = num1 + num2
                
            elif part == "-":
                result = num1 - num2
                
            elif part == "*":
                result = num1 * num2
                
            elif part == "/":
                
                if num2 == 0:
                    print("На ноль не делим нникогда")
                    return None
                
                result = num1 / num2
                
            elif part == '**':
                result = num1 ** num2

            
            elif part == "//":

                if num2 == 0:
                    print("На ноль не делим нникогда")
                    return None
                
                result = num1 // num2

            elif part == "%":
                
                if num2 == 0:
                    print("На ноль не делим нникогда")
                    return None
                
                result = num1 % num2
            

            stack.append(float(result))
           
        elif part == '(':
            
            el_skobka = []
            j = 1
            k = 1 # вхождение в подстроку (
            l = 0 # вхождение в подстроку )
            
            while parts[i + j] != ')' and k != l:
                el_skobka.append(parts[i + j])
                j += 1
                if parts[i + j] == ')':
                    l += 1
                elif parts[i + j] == '(':
                    k += 1
            
            if l == k:
                stack.append(calculat(' '.join(el_skobka)))
            else:
                print(f"Ошибка: '{part}' - неподходящий ввод")
                return None
            i += j
            
        else:
            print(f"Ошибка: '{part}' - неподходящий ввод")
            return None
        
        i += 1
    
    
    
    if len(stack) == 1:
        return stack[0]
    
    elif len(stack) == 0:
        print("Ошибка: пустой стек")
        return None
    
    else:
        print(f"Ошибка: В стеке {len(stack)} числа")
        return None


def is_number(text):
    
    #проверяет является ли текст числом
    #возвращает True если число, False если нет
    
    
    pattern = r'^[+-]?\d*\.?\d+$'
    
    
    if re.match(pattern, text):
        return True
    else:
        return False

if __name__ == "__main__":
     main()
