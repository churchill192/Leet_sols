class MyHashMap:

    def __init__(self):
        self.x = {}
        

    def put(self, key: int, value: int) -> None:
        self.x[key] = value
        

    def get(self, key: int) -> int:
        if key in self.x:
            return self.x[key]
        else:
            return -1
        

    def remove(self, key: int) -> None:
        if key in self.x:

            self.x.pop(key)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)