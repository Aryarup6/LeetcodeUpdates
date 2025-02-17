class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        pre, post = [0] * n, [0] * n
        ans = 0
        pre[0], post[-1] = height[0], height[-1]
        for i in range(1, n):
            pre[i] = max(height[i], pre[i-1])
            post[n-1-i] = max(height[n-i-1], post[n-i])
        for i in range(1, n-1):
            if min(pre[i-1], post[i+1]) > height[i]:
                ans += min(pre[i-1], post[i+1]) - height[i]
        return ans