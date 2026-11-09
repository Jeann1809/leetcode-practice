class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums_set = set(nums)
        max_count = 0

        for num in nums_set:
            if num - 1 in nums_set:
                continue

            count = 1
            while num + 1 in nums_set:
                num += 1
                count += 1

            max_count = max(count, max_count)

        return max_count