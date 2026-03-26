#=====================================================================
#   10828번:    스택                   
#   @date:   2026-03-25              
#   @link:   https://www.acmicpc.net/problem/10828  
#   @Note:   폴더 내부에 있는 파일을 삭제하거나 변경하지 말아주세요.
#   @Test:   코드를 작성 후 "BOJ: 테스트"통해서 테스트를 해보세요.
#=====================================================================

import sys;

input = sys.stdin.readline
stack = []

n = int(input())
for _ in range(n):
    command = input().split() # 나누기!
    # push X, pop, size, empty, top
    if command[0] == "push":
        stack.append(command[1])
    elif command[0] == "pop":
        print(stack.pop(-1)) if len(stack) > 0 else print(-1)
    elif command[0] == "size":
        print(len(stack))
    elif command[0] == "empty":
        print(1) if len(stack) == 0 else print(0)
    elif command[0] == "top":
        print(stack[-1]) if len(stack) > 0 else print(-1)
    else:
        exit()
    
    
