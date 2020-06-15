class RandomizedSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data_map = {}
        self.data_list = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.data_map:
          return False
        self.data_map[val] = len(self.data_list)
        self.data_list.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.data_map:
          return False
        
        idx = self.data_map[val]
        self.data_list[idx] = self.data_list[-1]
        self.data_map[self.data_list[idx]] = idx
        
        del self.data_map[val]
        del self.data_list[-1]
        
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.data_list)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()