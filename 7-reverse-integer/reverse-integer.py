class Solution:
    def reverse(self, x: int) -> int:
            r=abs(x)
            s= str(r)
            l= len(s)
            y=""

            for i in range(-1,-l-1,-1):
                y=y+s[i]
        
            

            if ((-2147483647)<=int(y)<=(2147483647)):
                if x>0:
                    return int(y)
        
                else:
                    return int(y)*(-1)
            else:
                return 0
        

        