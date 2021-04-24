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
    # sum of listay elements recursive
    if len(list) == 1:
        return list[0]
    else:
        return list.pop(0) + sum_reCurs(list)

# list = [1, 2, 1]
# print(sum_reCurs(list))

def list_max_reCurs(list):
    # max in list recursion
    max = list[0]
    if len(list) = 1:
        if max < list[0]:
            return list[0]
        else:
            return max
    else:
        list.pop(0)
        tmp = list_max_reCurs(list)
        if max < tmp:
            return tmp
        else:
            return max
# ===
