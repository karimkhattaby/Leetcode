class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n < 0:
            return []
        if n == 0:
            return [""]
        
        permutations = []
        
        def gen_parens(lst, n1, n2):
            if n1 == 0 and n2 == 0:
                permutations.append(''.join(lst))
            s1 = ''
            s2 = ''
            if n1 > 0:
                s1 = gen_parens(lst+['('], n1-1, n2+1)
            if n2 > 0:
                s2 = gen_parens(lst+[')'], n1, n2-1)
            
        gen_parens([], n, 0)
        return permutations