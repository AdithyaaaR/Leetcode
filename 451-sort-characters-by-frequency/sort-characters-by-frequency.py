class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import Counter 
        x =Counter(s)
        y="".join([i*j for i,j in x.most_common()])
        return y