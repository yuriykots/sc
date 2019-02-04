# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# Example:
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


class Solution:
    # Time Complexity: 0(n^2)
    # Space Complexity: 0(1)
    def two_sum_brute_force(self, nums, target):
        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    # As we process array elements one by one we can add them to the hash table.
    # And then we will check if target element is in the hash table
    def two_sum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_table_object = {}

        for idx, element in enumerate(nums):
            if element in hash_table_object:
                return [hash_table_object[element], idx]
            else:
                hash_table_object[target - element] = idx


mySolution = Solution()
print('two_sum_brute_force')
print(mySolution.two_sum_brute_force([2, 6, 8, 9, 1, 11, 15], 9))

print('two_sum_hash_object_result')
print(mySolution.two_sum([2, 6, 8, 9, 1, 11, 15], 9))

