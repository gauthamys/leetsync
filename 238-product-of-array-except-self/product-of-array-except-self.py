class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0] * n
        prefix = [1] + prefix
        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        postfix = [0] * n
        postfix += [1]
        for i in range(n - 1, -1, -1):
            postfix[i] = postfix[i + 1] * nums[i]
        prefix.pop(0)
        postfix.pop()
        res = []
        for i in range(n):
            left = 1 if i == 0 else prefix[i - 1]
            right = 1 if i == n - 1 else postfix[i + 1]

            res.append(left * right)
        return res