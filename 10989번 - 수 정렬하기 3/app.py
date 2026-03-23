#=====================================================================
#   10989번:    수 정렬하기 3                   
#   @date:   2026-03-23              
#   @link:   https://www.acmicpc.net/problem/10989  
#   @Note:   폴더 내부에 있는 파일을 삭제하거나 변경하지 말아주세요.
#   @Test:   코드를 작성 후 "BOJ: 테스트"통해서 테스트를 해보세요.
#=====================================================================

import sys;

input = sys.stdin.readline

# 어떤 정렬을 쓸 것인가? - 당연히 sort()는 안 씀.
# 일단 속도가 안정적인 merge sort를 써 보려 한다.

# merge sort
# [1,2,3,4,5,6] -> [1, 2, 3] / [4, 5, 6] -> 
# [1] / [2, 3] / [4] / [5, 6] ->
# [1] [2] [3] [4] [5] [6]


def merge_sort():
    return

def merge():
    return

numbers = []

cnt = int(input())
for _ in range(cnt):
    numbers.append(int(input().strip()))

print(numbers)


