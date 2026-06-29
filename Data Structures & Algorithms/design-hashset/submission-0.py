class MyHashSet:

    def __init__(self):
        self.hashes = []
        
    def add(self, key: int) -> None:
        if key not in self.hashes:
            self.hashes.append(key)
        
    def remove(self, key: int) -> None:
        if key in self.hashes:
            self.hashes.remove(key)
        print(self.hashes)
        
    def contains(self, key: int) -> bool:
        if key in self.hashes:
            return True
        return False

        

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)