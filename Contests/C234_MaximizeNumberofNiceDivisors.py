class Solution:
    def maxNiceDivisors(self, primeFactors: int) -> int:
        if primeFactors == 1:
            return 1
        else:
            bigNum = 10 ** 9 + 7
            if primeFactors % 2 == 0:
                num2s = int(primeFactors / 2)

                num3Pairs = int(num2s / 3)
                num2s = num2s - num3Pairs * 3
                # return ((2**num2s % bigNum) * 3**(num3Pairs*2 % bigNum)) % bigNum
                res = pow(2, num2s, bigNum) * pow(3, num3Pairs * 2, bigNum)
            else:
                num2s = int(primeFactors / 2) - 1
                num3Pairs = int(num2s / 3)
                num2s = num2s - num3Pairs * 3
                # return ((2**num2s % bigNum) * (3**(num3Pairs*2 + 1) % bigNum)) % bigNum
                res = pow(2, num2s, bigNum) * pow(3, num3Pairs * 2 + 1, bigNum)
            return res % bigNum

