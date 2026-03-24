#=====================================================================
#   1436번:    영화감독 숌                   
#   @date:   2026-03-24              
#   @link:   https://www.acmicpc.net/problem/1436  
#   @Note:   폴더 내부에 있는 파일을 삭제하거나 변경하지 말아주세요.
#   @Test:   코드를 작성 후 "BOJ: 테스트"통해서 테스트를 해보세요.
#=====================================================================

import sys;

input = sys.stdin.readline

# 규칙을 찾는 게 힘들다.
# 하지만 N이 10,000보다 작기에 딱히 힘들지는 않다.

# 그럼 브루트 포스다.
# 와!

wanted_cnt = int(input())

cnt = 0;
num = 0;
while True:
    if cnt == 10000: break
    if "666" in str(num):
        cnt += 1
    if wanted_cnt == cnt: break
    num += 1

print(num)



