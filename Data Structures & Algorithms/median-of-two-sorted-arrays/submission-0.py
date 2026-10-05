class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # nums1
        a = nums1 + nums2
        # print(a)
        a.sort()
        am = len(a) //2
        l = a[:am] 
        r = a[am:]
        if len(l) == len(r):
            # print("{} > {}".format(l,l[-1]))
            # print("{} > {}".format(r,r[0]))
            res = float(( l[-1] + r[0] ) / 2)
            # print( "( {} + {} ) / {}".format(l[-1], r[0] , res))
            # print(res)
            return res

        return a[am] 