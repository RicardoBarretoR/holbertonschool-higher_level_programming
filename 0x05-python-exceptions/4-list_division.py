#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """divides element by element 2 lists"""
    n_list = []
    for i in range(list_length):
        try:
            resul = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            resul = 0
        except ZeroDivisionError:
            print("division by 0")
            resul = 0
        except IndexError:
            print("out of range")
            resul = 0
        finally:
            n_list.append(resul)
    return n_list
