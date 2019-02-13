# https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/

# Given a string, find the length of the longest substring without repeating characters.


class Solution:
    def lengthOfLongestSubstring(self, s: 'str') -> 'int':
        max_size_so_far = 0
        start_index = 0
        hash_table = {}

        for index, letter in enumerate(s):
            if letter not in hash_table or hash_table[letter] < start_index:
                length_count = index + 1 - start_index
                max_size_so_far = max(length_count, max_size_so_far)
                hash_table[letter] = index
            else:
                start_index = hash_table[letter] + 1
                hash_table[letter] = index

        return max_size_so_far
