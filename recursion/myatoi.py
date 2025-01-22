import sys
class Solution:
    
    def rec(self, l: str) -> str:
        imax = 2147483647
        imin = -2**31
        rem = ''
        iddu = ''
        if len(l)!=0 and l[0].isdigit() :
            iddu = l[0]
            print(iddu)
            c = l[1:]
            ''.join(c)
            rem = self.rec(c)
        else:
            return -1
        
        
        if rem != -1:
            iddu = iddu+rem
        

        return iddu
        
    def myAtoi(self, s: str) -> int:
        imax = 2147483647
        imin = -2**31
        l = s.strip()
        if not l:
            return 0
        sign = 1
        if (l[0]=='-'):
            sign=-1
            l=l[1:]
        elif l[0]=='+':
            l=l[1:]
        
        if not l:
            return 0
        if (l[0]=="0"):
            l=l[1:]
        
        if(not l[0].isdigit()):
            return 0

        num = self.rec(l)
        
        if(int(num)*sign >= imax):
            return imax
        elif(int(num)*sign <=imin):
            return imin
        
        
        return int(num)*sign
