# ===
def search_binary(list, item):
    
    step = 0
    
    low_ = 0
    high = len(list) - 1
    
    while low_ <= high:
    
        step += 1
    
        index = (low_ + high) // 2
        value = list[index]
    
        if value == item:
            return index
    
        if value > item:
            high = index - 1
        else:
            low_ = index + 1
    
    return None
    
list1 = [1, 3, 5, 7, 9, 11, 13, 15, 16, 17, 18]
    
print(search_binary(list1, 11))
print(search_binary(list1, 2))

# ===
