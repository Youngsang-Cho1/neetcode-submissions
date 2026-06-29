class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity= capacity
        self.length= 0
        self.data= []

    def get(self, i: int) -> int:
        return self.data[i]

    def set(self, i: int, n: int) -> None:
        self.data[i]=n

    def pushback(self, n: int) -> None:
        if self.capacity == self.getSize():
            self.resize()
        self.data.append(n)

    def popback(self) -> int:
        elem= self.data.pop()
        return elem
        
 
    def resize(self) -> None:
        self.capacity*=2

    def getSize(self) -> int:
        counter=0
        for i in range (len(self.data)):
            counter+=1
        return counter

    def getCapacity(self) -> int:
        return self.capacity

