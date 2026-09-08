class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        al=[]
        for i in s:
            if i.isalpha():
                al+=[i]
        f=[]
        for k in s:
            if k.isalpha():
                f.append(al.pop())
            else:
                f.append(k)
        x="".join(f)
        return x