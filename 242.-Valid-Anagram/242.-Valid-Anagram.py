class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        t_dict, s_dict = {}, {}
        for i in range(len(s)):
            t_dict[t[i]] = 1 + t_dict.get(t[i], 0)
            s_dict[s[i]] = 1 + s_dict.get(s[i], 0)
        for c in s_dict:
            if s_dict[c] != t_dict.get(c, 0):
                return False
        return True
result = Soulution
