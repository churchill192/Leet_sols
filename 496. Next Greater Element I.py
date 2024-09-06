class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l = len(nums2)
        list1 = []

        for i in nums1:
            if i in nums2:
                j = nums2.index(i) + 1
                found = False
                for z in range(j, l):
                    if nums2[z] > i:
                        list1.append(nums2[z])
                        found = True
                        break
                if not found:
                    list1.append(-1)

        return(list1)