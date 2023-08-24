from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups: dict[tuple, List[str]] = dict()

        for string in strs:
            count_arr = [0] * 26
            for c in string:
                count_arr[ord(c) - ord("a")] += 1

            count_tup = tuple(count_arr)
            if count_tup not in groups:
                groups[count_tup] = [string]
            else:
                groups[count_tup].append(string)

        return list(groups.values())