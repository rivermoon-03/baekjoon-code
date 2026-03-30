#=====================================================================
#   11047번:    동전 0                   
#   @date:   2026-03-30              
#   @link:   https://www.acmicpc.net/problem/11047  
#   @Note:   폴더 내부에 있는 파일을 삭제하거나 변경하지 말아주세요.
#   @Test:   코드를 작성 후 "BOJ: 테스트"통해서 테스트를 해보세요.
#=====================================================================
import sys;
input = sys.stdin.readline

coins = 0

n, k = map(int, input().split())
# n : 동전 종류의 개수, k : 만들어야 하는 돈

coin_type = []
# 아래에는 동전의 종류가 한 줄에 하나씩.
for _ in range(n):
    coin_type.append(int(input()))
    
    
# 1원을 1원, 3원 코인으로 만드려면? 1원 1개.
# 4200원을 동전들로 만드려면? 1000원으로 4개,

i = len(coin_type) - 1
while (k > 0):
    if (coin_type[i] > k): i -= 1
    else:
        div = k // coin_type[i]
        coins += div
        k -= div * coin_type[i]
        
print(coins)   
