#=====================================================================
#   1920번:    수 찾기                   
#   @date:   2026-03-24              
#   @link:   https://www.acmicpc.net/problem/1920  
#   @Note:   폴더 내부에 있는 파일을 삭제하거나 변경하지 말아주세요.
#   @Test:   코드를 작성 후 "BOJ: 테스트"통해서 테스트를 해보세요.
#=====================================================================
# bisect로 이진 탐색
from bisect import bisect_left
import sys;

input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
A = sorted(A)


m = int(input())
X = list(map(int, input().split()))



for x in X:
    idx = bisect_left(A, x)
    if idx < len(A) and A[idx] == x: # bisect_left로 찾은 인덱스가 A의 범위 내에 있고, 그 위치의 값이 x와 같다면
        print(1) # 존재한다는 뜻이므로 1 출력
    else:
        print(0)