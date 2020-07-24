class Solution:
    def countAndSay(self, n: int) -> str:
        s = ['1']
        while n > 1:
            ans = []
            c = s[0]
            count = 1
            for i in range(1,len(s)):
                if s[i] == c:
                    count += 1
                else:
                    ans.append(str(count))
                    ans.append(c)
                    c = s[i]
                    count = 1
            ans.append(str(count))
            ans.append(c)
            n-=1
            s = ans
        return ''.join(s)