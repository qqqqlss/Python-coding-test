import collections

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if sorted(s)==sorted(t):
            return True
        else:
            return False
    #######################
    def isAnagram(self, s, t):
        return collections.Counter(s) == collections.Counter(t)
    ########################
    def isAnagram(self, s, t):
        dic = {}
        
        for i in s:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        
        for j in t:
            if j not in dic:
                return False
            else:
                dic[j] -= 1
        
        for val in dic.values():
            if val != 0:
                return False
        
        return True