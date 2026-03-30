#=====================================================================
#   11866번:    요세푸스 문제 0                   
#   @date:   2026-03-30              
#   @link:   https://www.acmicpc.net/problem/11866  
#   @Note:   폴더 내부에 있는 파일을 삭제하거나 변경하지 말아주세요.
#   @Test:   코드를 작성 후 "BOJ: 테스트"통해서 테스트를 해보세요.
#=====================================================================

import sys;

input = sys.stdin.readline


eliminated = []
n, k = map(int, input().split())
seq = [i for i in range(1, n+1)]
cursor = 0
 
while (len(seq) > 0):
    cursor += (k - 1) # k번째 사람을 제거하라는 것이지, k번 뒤에 있는 사람을 제거하라는 것이 아니기 떄문.
    if (cursor >= len(seq)): # 인덱스를 넘어가버리면
        cursor %= len(seq) # 나머지 연산으로 맨 앞으로 돌아오게 하기
        # cursor = 3인데 len(seq)가 4인 경우, cursor = 3 % 4로 cursor = 1이 나오게 해야 하는 것.
    eliminated.append(str(seq.pop(cursor)))
    # str로 안하면 28번째 줄 join에서 에러난다.

print("<", end="")
print(", ".join(eliminated), end="")
print(">")


