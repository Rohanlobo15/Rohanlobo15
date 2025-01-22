class Solution:
    def myPow(self, x: float, n: int) -> float:

        def Pow(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1
            
            res = Pow(x, n//2)
            res = res * res

            if(n%2==1):
                return res*x
            
            return res

        PosN=abs(n)
        ans = Pow(x, PosN)

        if n >= 0:
            return ans
        
        return 1 / ans 
