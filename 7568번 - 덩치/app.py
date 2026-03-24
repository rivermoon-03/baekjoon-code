#=====================================================================
#   7568번:    덩치                   
#   @date:   2026-03-24              
#   @link:   https://www.acmicpc.net/problem/7568  
#   @Note:   폴더 내부에 있는 파일을 삭제하거나 변경하지 말아주세요.
#   @Test:   코드를 작성 후 "BOJ: 테스트"통해서 테스트를 해보세요.
#=====================================================================

import sys;

input = sys.stdin.readline

# x, y > p, q
# x, y 둘 다 p, q보다 커야 한다.

n = int(input())
people = []

for _ in range(n):
    x, y = map(int, input().split())
    people.append([x, y])

# 입력 끝
# 리스트에서 첫 번째 사람을 꺼내고, 그 사람이 몇 등인지.
# 이걸 n번 반복하면 될 듯.

for i in people:
    rank = 1
    for j in people:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
            
    print(rank, end=" ")

