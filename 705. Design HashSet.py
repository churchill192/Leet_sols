class MyHashSet:

    def __init__(self):

        self.x = set()
        

    def add(self, key: int) -> None:
        self.x.add(key)
        

    def remove(self, key: int) -> None:
        if key in self.x:
            self.x.discard(key)

    def contains(self, key: int) -> bool:
        if key in self.x:
            return True
        else:
            return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)