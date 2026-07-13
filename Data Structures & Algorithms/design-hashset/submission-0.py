class MyHashSet:

    def __init__(self):
        #Need to initalize extra space: Need O(1) lookup -> list
        self.struct = set()

    def add(self, key: int) -> None:
        if key not in self.struct:
            self.struct.add(key)
        


    def remove(self, key: int) -> None:
        if key in self.struct:
            self.struct.remove(key)

        

    def contains(self, key: int) -> bool:
        if key in self.struct:
            return True
        else:
            return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)