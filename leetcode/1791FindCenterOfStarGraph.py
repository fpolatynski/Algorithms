class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        a1, b1 = edges[0]
        a2, b2 = edges[1]
        if a1 == a2 or a1 == b2:
            return a1
        else:
            return b1
