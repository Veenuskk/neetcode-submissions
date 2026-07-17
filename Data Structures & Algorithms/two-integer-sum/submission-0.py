class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        ans = []
        for i in range(n - 1 , -1 , -1) :
            for j in range(i - 1 , -1 , -1) :
                if nums[i] + nums[j] == target and i != j :
                    return [j , i]
        return []