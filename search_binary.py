# ===
step = 0
    
def search_binary(list, item):
    
    global step
    
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
    
print(search_binary(list1,5), step)
print(search_binary(list1,2), step)

# ===
