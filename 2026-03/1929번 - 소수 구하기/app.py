#=====================================================================
#   1929번:    소수 구하기                   
#   @date:   2026-03-29              
#   @link:   https://www.acmicpc.net/problem/1929  
#   @Note:   폴더 내부에 있는 파일을 삭제하거나 변경하지 말아주세요.
#   @Test:   코드를 작성 후 "BOJ: 테스트"통해서 테스트를 해보세요.
#=====================================================================
import math
import sys;
input = sys.stdin.readline

m, n = map(int, input().split())

'''
prime_numbers = []
# m부터 n까지 소수 판별을 해야 한다.
for i in range(m, n + 1, 1):
    isPrime = 1
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0: isPrime = 0
    
    if isPrime == 1: prime_numbers.append(i)

for p in prime_numbers: print(p)
'''

numbers = [1] * (n + 1) # 인덱스를 편하게 세기 위해 0부터 n까지 소수인지 아닌지의 여부가 담긴 리스트
# 1이면 소수, 0이면 소수가 아니라는 것이다.
numbers[0] = 0 # 0, 1은 소수가 아니므로 패스.
numbers[1] = 0 # 0, 1은 소수가 아니므로 패스.

for i in range(2, int(math.sqrt(n)) + 1):
    if numbers[i]: # numbers[i] == 1
        for j in range(i * 2, n + 1, i):
            numbers[j] = 0

for n in range(m, len(numbers)):
    if numbers[n] == 1: print(n)
    