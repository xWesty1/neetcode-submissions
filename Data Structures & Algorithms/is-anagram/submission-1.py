class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        s_dict = {}
        t_dict = {}

        for i in s:
            if i in s_dict.keys():
                s_dict[i] += 1
            else:
                s_dict[i] = 1
        
        for j in t:
            if j in t_dict.keys():
                t_dict[j] += 1
            else:
                t_dict[j] = 1

        for k in s_dict:
            if k not in t_dict:
                return False
            elif s_dict[k] != t_dict[k]:
                return False
        return True