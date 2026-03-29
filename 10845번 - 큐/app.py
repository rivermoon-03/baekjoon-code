#=====================================================================
#   10845번:    큐                   
#   @date:   2026-03-29              
#   @link:   https://www.acmicpc.net/problem/10845  
#   @Note:   폴더 내부에 있는 파일을 삭제하거나 변경하지 말아주세요.
#   @Test:   코드를 작성 후 "BOJ: 테스트"통해서 테스트를 해보세요.
#=====================================================================

import sys;

input = sys.stdin.readline

n = int(input())
queue = []

for _ in range(n):
    c = list(input().split())
    if c[0] == "push":
        queue.append(c[1])
    elif c[0] == "pop":
        if len(queue) == 0: print(-1)
        else: print(queue.pop(0))
    elif c[0] == "size":
        print(len(queue))
    elif c[0] == "empty":
        if len(queue) == 0: print(1)
        else: print(0)
    elif c[0] == "front":
        if len(queue) == 0: print(-1)
        else: print(queue[0])
    elif c[0] == "back":
        if len(queue) == 0: print(-1)
        else: print(queue[-1])
        
    