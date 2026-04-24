#!/usr/bin/python3
import logging

logging.basicConfig(
    filename="calculator.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",  
)


def add(a, b):
    logging.info(f"Adding {a} + {b}")
    return a+b

def divide(a, b):
    try:
        result=a/b
        logging.info(f"Dividing {a}/{b}")
        return result
    except ZeroDivisionError:
        logging.error("Attempted Division by zero", exc_info=True)
        return None
    
def main():
    logging.info("Calculator started")

    print("1. Add\n 2.Divide")
    choice=input("Choose option: ")

    a=float(input("Enter first number: "))
    b=float(input("Enter Second number:"))

    if choice == "1":
        print("Result: ", add(a,b))
    elif choice=="2":
        print("Result: ", divide(a,b))
    else:
        logging.warning("Invalid choice entered")

if __name__=="__main__":
    main()

"""
(2_Open-claw_Agents)logging>python calc_logging.py
1. Add
 2.Divide
Choose option: 2
Enter first number: 32
Enter Second number:0
Result:  None

(2_Open-claw_Agents)logging>more app.log
2026-03-22 17:53:21,517 - INFO - Info message
2026-03-22 17:53:21,517 - WARNING - Warning message
2026-03-22 17:53:21,517 - ERROR - Error Message
"""