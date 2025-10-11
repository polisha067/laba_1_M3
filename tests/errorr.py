from train import *


def error():
   
    error_cases = [
        "2 +",           
        "5 5 * +",             
        " ",           
        "&",          
        "2 5 ++",        
        "2 + 2 + 5", 
        "5 // 0",    
        " 4 3 3 +",           
             
    ]
    
    for error in error_cases:
        print(f"\n{error}")
        result = calculat(error)
        if result is not None:
            print(f"Ответ: {result}")

if __name__ == "__errorr__":
    error()
