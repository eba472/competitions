class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        num = self.findMinDivisibleNumber(p, q)
        howManyReflection = num // q
        if howManyReflection % 2 == 0:
            return 2
        
        if num // p % 2 == 0:
            return 0
        
        return 1
    
    def findMinDivisibleNumber(self, a, b):
        a_divs = self.findAllDivisors(a)
        b_divs = self.findAllDivisors(b)
        minDivisibleNumber = 1
        done = set([])
        for a_div in a_divs:
            if a_div in b_divs:
                minDivisibleNumber *= a_div ** max(a_divs[a_div], b_divs[a_div])
                done.add(a_div)
            else:
                minDivisibleNumber *= a_div ** a_divs[a_div]
                done.add(a_div)
        
        for b_div in b_divs:
            if b_div not in done:
                minDivisibleNumber *= b_div ** b_divs[b_div]
        return minDivisibleNumber
    
    def findAllDivisors(self, a):
        divs = {}
        i = 2
        while a != 1:
            if a % i == 0:
                divs[i] = divs.get(i,0) + 1
                a //= i
            else:
                i += 1
        return divs
        