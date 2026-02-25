class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = []
        def merge(self, left, right):
            result = []
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1

            result.extend(left[i:])
            result.extend(right[j:])

            return result
        
        def mergeSort(self, arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            left = mergeSort(self, arr[:mid])
            right = mergeSort(self, arr[mid:])

            return merge(self, left, right)

        nums1 = mergeSort(self, nums)
        for i in range(len(nums1)-1):
            if nums1[i] == nums1[i+1]:
                res.append(nums1[i])
                temp = nums1.copy()
                temp.pop(i+1)
                break
        if nums1[0] != 1:
            res.append(1)
            return res
        elif nums1[-1] != len(nums1):
            res.append(len(nums1))
            return res
        else:
            for i in range(len(temp)-1):
                if temp[i+1] != temp[i]+1:
                    res.append(temp[i]+1)
        return res
                