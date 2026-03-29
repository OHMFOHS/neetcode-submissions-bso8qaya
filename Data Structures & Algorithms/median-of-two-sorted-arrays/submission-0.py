from math import inf
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1

        while True:
            i = (l + r) // 2
            j = half - i - 2
            
            Aleft = A[i] if i >= 0 else -inf #如果左边有元素，最大值是 A[i], 如果没有是-inf
            Aright = A[i+1] if (i + 1) < len(A) else inf #如有右边第一个有元素， 是 A[i+1], 否则是 inf
            Bleft = B[j] if j >= 0 else -inf
            Bright = B[j+1] if (j + 1) < len(B) else inf

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright: #too many elements on A
                r = i - 1
            else:
                l = i + 1
