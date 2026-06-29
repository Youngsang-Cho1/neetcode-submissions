class MyHashMap:

    def __init__(self):
        self.hashmap = []
        

    def put(self, key: int, value: int) -> None:
        for idx, i in enumerate(self.hashmap):
            if i[0] == key:
                self.hashmap[idx] = [key, value]
                return
        self.hashmap.append([key, value])

    def get(self, key: int) -> int:
        for i in self.hashmap:
            if i[0] == key:
                return i[1]
        return -1
        
    def remove(self, key: int) -> None:
        temp = []
        for idx, i in enumerate(self.hashmap):
            if i[0] == key:
                del self.hashmap[idx]
        
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)