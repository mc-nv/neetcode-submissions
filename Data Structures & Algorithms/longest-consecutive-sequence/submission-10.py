class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        mx = 1
        tmp = 1
        i = 0
        if len(nums) <= 1:
            return len(nums)

        while i < len(nums) - 1:

            if (nums[i] +1)  ==  nums[i+1]:
                tmp +=1
                mx = max(tmp,mx)
            elif ( nums[i] == nums[i+1]):
                mx = max(tmp,mx)
            else:
                tmp = 1
            i+= 1

        return mx
