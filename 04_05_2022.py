"""створити функцію, що приймає два списки,
що повертає список значень, які містяться
тільки в одному зі списків"""


print("Bu! ")


def join_lists(list_1, list_2, joined_list=[]):
    for i in list_1:
        if i in list_2:
            continue
        else:
            joined_list.append(i)
    for i in list_2:
        if i in list_1:
            continue
        else:
            joined_list.append(i)
    list_1.clear()
    for i in joined_list:
        if i not in list_1:
            list_1.append(i)
    return list_1



print(join_lists([1, 2, 2, 3, 6, 6], [6, 2, 3, 5, 5, 5, 7, 7]))







