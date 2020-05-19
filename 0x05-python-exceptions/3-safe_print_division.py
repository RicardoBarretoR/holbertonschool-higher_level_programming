#!/usr/bin/python3
def safe_print_division(a, b):
    """divides 2 integers and prints the result"""
    try:
        resul = a / b
    except (ZeroDivisionError, ValueError):
        resul = None
    finally:
        print("Inside result: {}".format(resul))
    return resul
