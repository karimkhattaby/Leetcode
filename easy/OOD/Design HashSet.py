class MyHashSet:

    def __init__(self):
        self.hashSet = {}

    def add(self, key: int) -> None:
        self.hashSet[key] = True

    def remove(self, key: int) -> None:
        if self.contains(key):
            del self.hashSet[key]

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return key in self.hashSet


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)