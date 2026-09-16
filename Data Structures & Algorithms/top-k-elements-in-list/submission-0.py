class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        temp = {}
        for num in nums :
            temp[num] = 1 + temp.get(num , 0)
        
        d = dict(sorted(temp.items() , key = lambda x : x[1] , reverse = True))
        res = []
        for i in range(k) :
            res.append(list(d.keys())[i])
        return res