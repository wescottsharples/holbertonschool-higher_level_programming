#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    ret_list = [0] * list_length
    for i in range(list_length):
        try:
            ret_list[i] = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            continue
        except ZeroDivisionError:
            print("division by 0")
            continue
        except IndexError:
            print("out of range")
            continue
        finally:
            pass
    return ret_list
