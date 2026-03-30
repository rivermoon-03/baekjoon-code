#=====================================================================
#   11050번:    이항 계수 1                   
#   @date:   2026-03-23              
#   @link:   https://www.acmicpc.net/problem/11050  
#   @Note:   폴더 내부에 있는 파일을 삭제하거나 변경하지 말아주세요.
#   @Test:   코드를 작성 후 "BOJ: 테스트"통해서 테스트를 해보세요.
#=====================================================================

import sys;
input = sys.stdin.readline

n, m = map(int, input().split())
sum = 1

for i in range(n, n - m, -1):
    sum *= i

for j in range(m, 0, -1):
    sum /= j

print(int(sum))
