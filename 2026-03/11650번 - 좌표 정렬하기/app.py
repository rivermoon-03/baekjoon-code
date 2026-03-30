#=====================================================================
#   11650번:    좌표 정렬하기                   
#   @date:   2026-03-24              
#   @link:   https://www.acmicpc.net/problem/11650  
#   @Note:   폴더 내부에 있는 파일을 삭제하거나 변경하지 말아주세요.
#   @Test:   코드를 작성 후 "BOJ: 테스트"통해서 테스트를 해보세요.
#=====================================================================

import sys;

input = sys.stdin.readline

dots = []

n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    dots.append([x, y])

dots.sort(key=lambda x : x[1]) # y좌표대로 정렬
dots.sort(key=lambda x : x[0]) # x좌표대로 정렬


for dot in dots:
    print(dot[0], dot[1])