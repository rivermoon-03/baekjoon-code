#=====================================================================
#   10989번:    수 정렬하기 3                   
#   @date:   2026-03-23              
#   @link:   https://www.acmicpc.net/problem/10989  
#   @Note:   폴더 내부에 있는 파일을 삭제하거나 변경하지 말아주세요.
#   @Test:   코드를 작성 후 "BOJ: 테스트"통해서 테스트를 해보세요.
#=====================================================================

import sys;

input = sys.stdin.readline
import sys

# 일단 sort로는 안됨. - 메모리 초과
# 그럼 버블 정렬? -> 근데 얘도 메모리를 많이 먹는다.

# 수는 1~10000까지 나옴. 개수는 10,000,000개. 즉 중복이 있다는 말.
# 그럼 10000칸의 공간을 가진 배열을 만들고, 각 칸을 숫자가 나온 빈도 수로 생각하기.
# -> Counting Sort.

number = [0 for x in range(10001)] # number[1:10000]까지 사용할 것이다. 편하게 1부터 세기.
n = int(input())
for _ in range(n):
    incoming = int(input())
    number[incoming] += 1

for i in range(1, len(number)):
    for _ in range(number[i]):
        print(i)

    
    
    

