def test_calculator():
   
    test_cases = [
        "2 4 +",            #2+4 = 6
        "5 5 *",            #5*5 = 25  
        "10 5 /",           #10/5 = 2
        "2 10 **",          #2**10 = 1024
        "2 3 4 * +",        #2+(3*4) = 14
        "1 2 3 + 4 * + 5 -", #1+((2+3)*4)-4 = 16
        "( 5 2 - ) 10 +",     # (5-2)+10 = 13
        "2 2.5 +",            #2+2.5 = 4.5
        "2 ^ 2 +"             #2+2 = 4 унарный плюс
        "5 ~ 2 +"             # -5+2 = 3
    ]
    
    for test in test_cases:
        print(f"\n{test}")
        result = calculat(test)
        if result is not None:
            print(f"Ответ: {result}")

if __name__ == "__main__":
    test_calculator()
