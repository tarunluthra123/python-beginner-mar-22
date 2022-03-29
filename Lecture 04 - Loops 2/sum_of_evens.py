class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        ans = 0
        i = 2
        while i <= A:
            ans += i
            i += 2
        return ans
