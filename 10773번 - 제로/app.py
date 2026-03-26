#=====================================================================
#   10773번:    제로                   
#   @date:   2026-03-26              
#   @link:   https://www.acmicpc.net/problem/10773  
#   @Note:   폴더 내부에 있는 파일을 삭제하거나 변경하지 말아주세요.
#   @Test:   코드를 작성 후 "BOJ: 테스트"통해서 테스트를 해보세요.
#=====================================================================

import sys;

input = sys.stdin.readline
n = int(input())

num = []
res = 0

for _ in range(n):
    # 0이면 num[-1] 제거.
    # 아니면 append.
    userIn = int(input())
    if (userIn == 0): del num[-1]
    else: num.append(userIn)
    
for i in range(len(num)):
    res += num[i]
    
print(res)
