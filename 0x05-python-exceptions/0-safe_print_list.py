def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x):
            print("{}.format(my_list[i]), end=""")
    except IndexError:
        print()
        return i