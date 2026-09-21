class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        L = 0

        for i in range(len(nums)) :
            if i - L > k :
                window.remove(nums[L])
                L += 1
            if nums[i] in window :
                return True
            window.add(nums[i])
        return False
