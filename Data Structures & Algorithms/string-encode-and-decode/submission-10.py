class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            # Append length of string, the '#' delimiter, and the string itself
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = i
            # Move j forward until we find the '#' delimiter
            while s[j] != '#':
                j += 1
            
            # The length of the next string is the integer before the '#'
            length = int(s[i:j])
            
            # The actual string starts right after '#' and spans 'length' characters
            start = j + 1
            end = start + length
            res.append(s[start:end])
            
            # Move i to the start of the next encoded string
            i = end
            
        return res