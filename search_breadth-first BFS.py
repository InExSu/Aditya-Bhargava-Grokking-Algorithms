from collections import deque

def person_is_seller(name):
    return name[-1] == 'm' #последий элемент

def search(name):
    search_queue = deque()
    search_queue += graph["you"]
    searched = []
    while search_queue: # Пока очередь пуста
        person = search_queue.popleft() # из очереди извлечь первого
        if person_is_seller(person): # он?
            print(person, "BINGO!")
            return True
        else:
            search_queue += graph[person] # добавить следующий уровень
            searched.append(person)
    return False # Если дошло до сюда, значит НЕ найдено        

graph = {}
graph["you"] = [ "alice","bob","claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

search("you")