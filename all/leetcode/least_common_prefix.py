from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=lambda x: len(x))
        min_word = strs[0]
        for each_word in strs:
            # if len(each_word) < len(min_word):
            #     min_word = each_word
            while min_word:
                if each_word.startswith(min_word):
                    break
                min_word = min_word[:-1]
        return min_word


# assert Solution().longestCommonPrefix(['flow', 'flower', 'flight']) == 'fl'
print(Solution().longestCommonPrefix(["reflower", "flow", "flight"]))
