#=====================================================================
#   10814번:    나이순 정렬                   
#   @date:   2026-03-24              
#   @link:   https://www.acmicpc.net/problem/10814  
#   @Note:   폴더 내부에 있는 파일을 삭제하거나 변경하지 말아주세요.
#   @Test:   코드를 작성 후 "BOJ: 테스트"통해서 테스트를 해보세요.
#=====================================================================
import sys
input = sys.stdin.readline

n = int(input())
members = []
for _ in range(n):
    x, y = input().split()
    members.append((int(x), y))

members.sort(key=lambda m: m[0])  # 나이 기준 stable sort

for age, name in members:
    print(age, name)

