class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        def m_dict(a: str):
            d = {};

            for i in a:
                if i not in d.keys():
                    d[i] = 1
                else:
                    d[i] += 1
            return d

        ds = m_dict(s)
        dt = m_dict(t)

        return ds == dt