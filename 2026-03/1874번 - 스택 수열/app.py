#=====================================================================
#   1874번:    스택 수열                   
#   @date:   2026-03-30              
#   @link:   https://www.acmicpc.net/problem/1874  
#   @Note:   폴더 내부에 있는 파일을 삭제하거나 변경하지 말아주세요.
#   @Test:   코드를 작성 후 "BOJ: 테스트"통해서 테스트를 해보세요.
#=====================================================================

import sys;

input = sys.stdin.readline
def main():
    stack = []
    ans = []
    cursor = 1 # 수열은 1부터 시작.
    
    n = int(input())
    for _ in range(n):
        num = int(input())
        while cursor <= num:
            stack.append(cursor)
            ans.append("+")
            cursor += 1
            # 입력받은 수가 스택에 채워질 때까지 append
        
        if stack[-1] == num:
            stack.pop()
            ans.append("-")
        else: 
            print("NO")
            return
    
    for a in ans: print(a)

if __name__ == "__main__":
    main()
    
