class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            nums1[:n] = nums2

        i = m - 1
        j = n - 1
        k = m + n - 1
        while i >= 0 and j >= 0:
            el1 = nums1[i]
            el2 = nums2[j]
            if el1 > el2:
                nums1[k] = el1
                i -= 1
            else:
                nums1[k] = el2
                j -= 1
            k -= 1

        while j >= 0:  # collect remaining elements in nums2 after nums1 is exhaused
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

        print(nums1)


sol = Solution()
sol.merge([2, 0], 1, [1], 1)
