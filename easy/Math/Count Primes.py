class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        
        primes = [True] * n
        primes[0]=primes[1]=False
        i = 2
        
        while i < len(primes):
            if primes[i]:
                primes[2*i:n:i]=[False]*((n-1)//i-1)
            i+=1
        
        return sum(primes)