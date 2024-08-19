class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        def maxCrossingSum(nums, left, mid, right):
            # Inclui elementos do lado esquerdo do meio
            left_sum = float('-inf')
            total = 0
            for i in range(mid, left - 1, -1):
                total += nums[i]
                left_sum = max(left_sum, total)

            # Inclui elementos do lado direito do meio
            right_sum = float('-inf')
            total = 0
            for i in range(mid + 1, right + 1):
                total += nums[i]
                right_sum = max(right_sum, total)

            # Retorna a soma máxima que cruza o meio
            return left_sum + right_sum

        def maxSubArrayHelper(nums, left, right):
            if left == right:
                return nums[left]

            mid = (left + right) // 2

            return max(maxSubArrayHelper(nums, left, mid),
                       maxSubArrayHelper(nums, mid + 1, right),
                       maxCrossingSum(nums, left, mid, right))

        return maxSubArrayHelper(nums, 0, len(nums) - 1)
