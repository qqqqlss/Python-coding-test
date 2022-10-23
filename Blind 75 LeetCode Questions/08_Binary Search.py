class Solution(object):
    def search(self, arr, value):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        first, last = 0, len(arr)-1

        while first <= last:
            mid = (first + last) // 2
            if arr[mid] == value:
                return mid
            if arr[mid] > value:
                last = mid - 1
            else:
                first = mid + 1
        return -1