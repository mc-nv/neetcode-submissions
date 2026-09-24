class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dn = {}
        for i in nums:
            if i not in dn.keys():
                dn[i] = 1
            else:
                dn[i] += 1 
        
        sorted_dn = dict(sorted(dn.items(), key=lambda item: item[1], reverse=True))
        
        return list(sorted_dn.keys())[:k]