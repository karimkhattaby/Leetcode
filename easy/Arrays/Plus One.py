class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits:
            if digits[-1] == 9:
                i = len(digits)-1
                while i >= 0:
                    if digits[i] == 9:
                        if i == 0:
                            digits[i] = 1
                            digits.append(0)
                        else:
                            digits[i] = 0
                    else:
                        digits[i] += 1
                        break
                    i-=1
            else:
                digits[-1] += 1
        return digits