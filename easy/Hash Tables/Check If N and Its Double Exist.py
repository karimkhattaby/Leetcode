class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        HT = {}
        
        for i in range(len(arr)):
            if arr[i]*2 in HT or arr[i]/2 in HT:
                return True
            
            HT[arr[i]] = True
        
        return False