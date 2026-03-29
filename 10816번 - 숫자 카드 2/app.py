#=====================================================================
#   10816번:    숫자 카드 2                   
#   @date:   2026-03-29              
#   @link:   https://www.acmicpc.net/problem/10816  
#   @Note:   폴더 내부에 있는 파일을 삭제하거나 변경하지 말아주세요.
#   @Test:   코드를 작성 후 "BOJ: 테스트"통해서 테스트를 해보세요.
#=====================================================================

import sys;

input = sys.stdin.readline

# 입력부 (첫 줄에는 카드 수, 아랫줄에는 카드 번호)
cards = {}
n = int(input())

input_stack = list(map(int, input().split()))
for stack in input_stack:
    cards[stack] = cards.get(stack, 0) + 1
    
# 카드 기록 완료. 이제 카드 확인의 시간.

m = int(input())
output_stack = list(map(int, input().split()))

for o_stack in output_stack:
    if o_stack in cards: print(cards[o_stack], end=" ")
    else: print("0", end =" ")
