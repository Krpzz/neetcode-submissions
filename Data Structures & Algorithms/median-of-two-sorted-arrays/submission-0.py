class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        middle = total // 2 + 1

        i = 0
        j = 0
        count = 0

        previous = 0
        current = 0

        while count < middle:
            previous = current

            if i >= len(nums1):
                current = nums2[j]
                j += 1

            elif j >= len(nums2):
                current = nums1[i]
                i += 1

            elif nums1[i] < nums2[j]:
                current = nums1[i]
                i += 1

            else:
                current = nums2[j]
                j += 1

            count += 1

        if total % 2 == 0:
            return (previous + current) / 2.0
        else:
            return current
        