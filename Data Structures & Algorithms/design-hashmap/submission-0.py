class ListNode:
    def __init__(self, key = -1, value = -1, next_node = None):
        self.key = key
        self.val = value
        self.next = next_node

class MyHashMap:

    def __init__(self):
        self.size = 1000 #for each bucket
        self.buckets = [ListNode() for _ in range(self.size)]

    def _hash(self, key: int):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        
        #hashing: index = key % size
        index = self._hash(key)

        #put key
        head = self.buckets[index]
        curr = head
        while curr.next:
            if curr.next.key == key:
                curr.next.val = value
                return
            curr = curr.next

        #Not found so append
        curr.next = ListNode(key, value)
        

    def get(self, key: int) -> int:
        #get hash
        index = self._hash(key)

        #iterate through index to get key & value
        head = self.buckets[index]
        curr = head
        while curr.next:
            if curr.next.key == key:
                return curr.next.val
            curr = curr.next
        
        #not found
        return -1

        

    def remove(self, key: int) -> None:
        #find index
        index = self._hash(key)
        curr = self.buckets[index]
        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr.next
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

#Am going to work with bucket array with Linkedlist
#-> hash each key and then put it into a linkedlist
#Issue: O(n) time if keys all collide into one bucket

