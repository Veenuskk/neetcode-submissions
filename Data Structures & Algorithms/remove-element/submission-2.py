class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        temp = []
        for i in nums :
            if i == val :
                continue
            else :
                temp.append(i)

        for i in range(len(temp)) :
            nums[i] = temp[i]

        return len(temp)