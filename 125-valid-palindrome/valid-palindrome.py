class Solution:
    def isPalindrome(self, s: str) -> bool:
       
        result=""     
        for i in s.lower():
            if i.isalnum():
                result+=i
        x=result[::-1]
        if (x==result):
            return True
        else:
            return False  