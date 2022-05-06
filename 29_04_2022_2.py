# Hello!

def my_list_generator(n):
    my_list = []
    i = 1
    def my_list_inner(n):
        nonlocal n
        for i in range(n):
            if my_list == []:
                my_list.append(i)
                i += 1
                return my_list
            elif i < n:



    # if len(my_list) == n:
    #     return my_list
