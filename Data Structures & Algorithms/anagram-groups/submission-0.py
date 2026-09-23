class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ds = {}

        for i in strs:
            key ="".join(sorted(i))

            if key not in ds.keys():
                ds[key] = [i]
            else:
                ds[key].append(i)
            
        return list(ds.values())
        
