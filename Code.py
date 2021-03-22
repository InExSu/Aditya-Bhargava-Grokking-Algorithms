# ===
def search_binary(list, item):
    
    low_ = 0
    high = len(list) - 1
    
    while low_ <= high:
    
        index = low_ + high
        value = list[index]
    
        if value == item:
            return index
    
        if value > item:
            high = index - 1
        else:
            low_ = index + 1
    
    return None
    
list1 = [1, 3, 5, 7, 9]
    
print(search_binary(list1,5))
print(search_binary(list1,-1))

# ===
