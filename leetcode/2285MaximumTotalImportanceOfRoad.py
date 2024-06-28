class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        nodes = [0 for x in range(n)]
        for left, right in roads:
            nodes[left] += 1
            nodes[right] += 1
        nodes.sort()
        ans = 0
        for x in range(n):
            ans += nodes[x] * (x+1)
        return ans