# dict이용 간결하게 했음.
class Solution:
    def isValid(self, s):
        if len(s)%2==1:
            return False

        stack = [0]
        dict = {"[":"]", "{":"}", "(":")"}
        
        for char in s:
            if char in dict:
                stack.append(dict[char])
            else:
                if stack.pop()!=char:
                    return False
        return stack == [0]

# class Solution(object):
#     def isValid(self, s):
#         if len(s)%2==1:
#             return False
#         stack=[]
#         for i in s[:]:
#             if i=="(":
#                 stack.append(")")
#             elif i=="[":
#                 stack.append("]")
#             elif i=="{":
#                 stack.append("}")
#             else:
#                 if stack==[]:
#                     return False
#                 elif stack.pop()!=i:
#                     return False
#         if stack==[]:
#             return True
#         else:
#             return False