class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        res = strs[0]
        for i in range(1, len(strs)):
            j = 0
            temp = ""
            comp = strs[i]
            while j < len(res) and j < len(comp):
                if comp[j] == res[j]:
                    temp += comp[j]
                    j += 1
                else:
                    break
            res = temp

        return res    