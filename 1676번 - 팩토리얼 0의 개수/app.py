#=====================================================================
#   1676번:    팩토리얼 0의 개수                   
#   @date:   2026-03-24              
#   @link:   https://www.acmicpc.net/problem/1676  
#   @Note:   폴더 내부에 있는 파일을 삭제하거나 변경하지 말아주세요.
#   @Test:   코드를 작성 후 "BOJ: 테스트"통해서 테스트를 해보세요.
#=====================================================================

import sys;

input = sys.stdin.readline

def factorial(n):
    if n == 0: return 1
    return n * factorial(n-1)

n = str(factorial((int((input())))))

zero_pos = 0
for i in range(len(n) - 1, 0, -1):
    if n[i] != '0': break
    zero_pos += 1

print(zero_pos)