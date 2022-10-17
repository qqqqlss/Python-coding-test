#https://leetcode.com/problems/two-sum/
#정답 시간 복잡도 O(2N)
class Solution(object):
	def twoSum(self, nums, target):
		buffer_dictionary = {}
		for i in range(len(nums)):
			if nums[i] in buffer_dictionary:
				return [buffer_dictionary[nums[i]], i] #if a number shows up in the dictionary already that means the necesarry pair has been iterated on previously
			else: # else is entirely optional
				buffer_dictionary[target - nums[i]] = i 
				# we insert the required number to pair with should it exist later in the list of numbers
########################################################################################
#오답 시간 복잡도 O(n^2/2)
class Solution(object):
    def twoSum(self, nums, target):

        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i]+nums[j]==target:
                    return [j,i]
nums=[2,7,11,15]
target=9
print(Solution().twoSum(nums,target))