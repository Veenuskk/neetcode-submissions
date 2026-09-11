class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        for num in nums :
            c = 0
            for i in nums :
                if i == num :
                    c += 1
            if c > n//2 :
                return num