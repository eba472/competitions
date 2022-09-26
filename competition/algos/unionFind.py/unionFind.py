from typing import List

# Leetcode #990: Satisfiability of Equality Equations
class unionFind:
    def __init__(self, n):
        self.count = n # Number of unions
        self.parents = [i for i in range(n)] # Initially all parents are itself 

    def find(self, i):
        if self.parents[i] != i: # Equal to itself means parent, otherwise go until reach parent
            self.parents[i] = self.find(self.parents[i])
        return self.parents[i]

    def union(self, i, j):
        rootI = self.find(i)
        rootJ = self.find(j)
        if rootI != rootJ:
            self.parents[rootI] = rootJ # Connect 2 unions by assigning the parent
            self.count -= 1

    def connected(self, i, j):
        return self.find(i) == self.find(j) # If parents are equal means connected

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        def util(c):
            return ord(c) - ord('a')
        uf = unionFind(26)

        for equ in equations:
            if equ[1] == '=':
                uf.union(util(equ[0]), util(equ[3]))

        for equ in equations:
            if equ[1] == '!':
                if uf.connected(util(equ[0]), util(equ[3])):
                    return False
        return True
