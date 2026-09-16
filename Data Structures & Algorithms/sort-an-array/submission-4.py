import random
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        high = len(nums) - 1
        low = 0
        self.quicksort(nums , low , high)
        return nums

    def quicksort(self , nums , low , high) :
        if low < high :
            pi = self.partition(nums , low , high)
            self.quicksort(nums , low , pi - 1 )
            self.quicksort(nums , pi + 1 , high)

    def partition(self , nums , low , high ) :
        randompivot = random.randint(low , high)
        nums[high] , nums[randompivot] = nums[randompivot] , nums[high]
        pivot = nums[high]
        i = low - 1
        for j in range(low , high) :
            if nums[j] < pivot :
                i += 1
                nums[i] , nums[j] = nums[j] , nums[i]
        i += 1
        nums[i] , nums[high] = nums[high] , nums[i]
        return i