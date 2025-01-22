class Solution:
    def f(self, n: int)->int:
        mod = 10**9+7
        if n==1:
            return 20
        
        if n<=2:
            return 400
        
        if n%2 == 0:
            half = self.f(n//2)
            return (half*half)%mod
        else:
            half = self.f(n//2)
            return (half*half*20)%mod

    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9+7
        if n==1:
            return 5
        
        if n==2:
            return 20
        
        if n%2==0:
            return (self.f(n/2))%mod
        else:
            return (self.f((n-1)/2)*5)%mod
