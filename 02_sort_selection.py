def list_index_smallest(lst):
    smallest = lst[0]
    idxsmall = 0
    for i in range(1, len(lst)):
        if lst[i] < smallest:
            smallest = lst[i]
            idxsmall = i
    return idxsmall
# test
# lst = [3, 4, 1]
# print(list_index_smallest(lst))


def sort_selection(lst):
    lstNew = []
    for i in range(len(lst)):
        index_small = list_index_smallest(lst)
        lstNew.append(lst.pop(index_small))
    return lstNew
# test
lst = [3, 4, 1]
print(sort_selection(lst))
