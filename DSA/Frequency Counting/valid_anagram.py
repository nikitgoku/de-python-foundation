from typing import List
from loguru import logger

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Initialise a default dictionary
        char_map = {}
        # Traverse the first string
        for char in s:
            char_map[char] = char_map.get(char, 0) + 1

        # Traverse the second string
        for char in t:
            char_map[char] = char_map.get(char, 0) - 1

        # Check for non-zero values in the dictionary
        for val in char_map.values():
            if val != 0:
                return False

        return True


solution_object = Solution()
logger.info(f"Result Case 1: {solution_object.isAnagram('anagram', 'nagaram')}")            # Expected: True
logger.info(f"Result Case 2: {solution_object.isAnagram('rat', 'cat')}")                    # Expected: False
logger.info(f"Result Case 3: {solution_object.isAnagram('themorsecode', 'herecomesdot')}")  # Expected: True