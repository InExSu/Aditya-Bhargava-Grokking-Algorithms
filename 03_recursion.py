def countdown(i):
    # print with reCursion
    print(i)
    if i < 1:
        return
    else:
        countdown(i-1)
# test
# countdown(3)


def sum_reCurs(list):
    # sum of list elements recursive
    if len(list) == 1:
        return list[0]
    else:
        return list.pop(0) + sum_reCurs(list)

# list = [1, 2, 1]
# print(sum_reCurs(list))


def list_max_reCurs(list):
    # max in list recursion
    if len(list) < 2:
        return list[0]
    else:
        if list[0] > list[1]:
            list.pop(1)
        else:
            list.pop(0)
        return list_max_reCurs(list)


# print(list_max_reCurs([5, 2, 4]))

def sort_quick(list):
    if len(list) < 2:
        return list
    else:
        pivot_ = list[0]
        # массив элементов меньше опорного
        less__ = [i for i in list[1:] if i <= pivot_]
        # массив элементов больше опорного
        greate = [i for i in list[1:] if i > pivot_]
        return sort_quick(less__) + [pivot_] + sort_quick(greate)

# print(sort_quick([5,3,6,2]))        
# ===
