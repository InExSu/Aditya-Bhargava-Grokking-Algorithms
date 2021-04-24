def array_index_smallest(arr):
    smallest = arr[0]
    idxsmall = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            idxsmall = i
    return idxsmall
# test
# arr = [3, 4, 1]
# print(array_index_smallest(arr))


def sort_selection(arr):
    arrNew = []
    for i in range(len(arr)):
        index_small = array_index_smallest(arr)
        arrNew.append(arr.pop(index_small))
    return arrNew
# test
arr = [3, 4, 1]
print(sort_selection(arr))
