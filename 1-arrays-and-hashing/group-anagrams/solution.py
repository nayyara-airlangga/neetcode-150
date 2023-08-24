from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups: dict[str, List[str]] = dict()

        for i, string1 in enumerate(strs):
            has_anagram = False
            string1_chars_count = dict()

            for char in string1:
                if char in string1_chars_count:
                    string1_chars_count[char] += 1
                else:
                    string1_chars_count[char] = 1

            for j, string2 in enumerate(strs):
                if len(string1) != len(string2) or (string1 == string2 and i == j):
                    continue

                not_anagram = False
                string2_chars_count = dict()

                for char in string2:
                    if char in string2_chars_count:
                        string2_chars_count[char] += 1
                    else:
                        string2_chars_count[char] = 1

                for char in string1_chars_count:
                    if char not in string2_chars_count:
                        not_anagram = True
                        break
                    elif string1_chars_count[char] != string2_chars_count[char]:
                        not_anagram = True
                        break
                
                if not_anagram:
                    continue
                    
                for char in string2_chars_count:
                    if char not in string1_chars_count:
                        not_anagram = True
                        break
                    elif string1_chars_count[char] != string2_chars_count[char]:
                        not_anagram = True
                        break
                
                if not_anagram:
                    continue

                has_anagram = True

                if len(groups) == 0:
                    groups[string1] = [string1, string2]
                    continue
    
                group_exists = False
                for group in list(groups.values()):
                    if string1 in group:
                        group_exists = True
                        if string2 not in group or (string1 == string2):
                            group.append(string2)
                            break
                    elif string2 in group:
                        group_exists = True
                        if string1 not in group:
                            group.append(string1)
                            break

                if not group_exists:
                    groups[string1] = [string1, string2]

            if not has_anagram:
                groups[string1] = [string1]


        return list(groups.values())