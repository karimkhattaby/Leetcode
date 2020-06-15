class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # checking for null values
        if s1 is None or s1 == "":
          return True
        
        # for s1 to be part of s2,
        # this condition must be met s2 >= s1
        if len(s2) < len(s1):
          return False
        
        # create a counter of s1
        count1 = collections.Counter(s1)
        
        # loop through s2 characters
        # while slicing s2 into characters that match s1 length
        for i in range(0, len(s2)-len(s1)+1):
          # use a helper method to create a counter of the current substring
          if self.checker(count1, s2[i:i+len(s1)]):
            # in case of a match, return
            return True
        
        # if we reach this point then there was no match
        return False
        
    # helper method to create a counter of substring characters
    # and return if it matches s1 character count
    def checker(self, count1, s2):
      count2 = collections.Counter(s2)
      
      return count1 == count2