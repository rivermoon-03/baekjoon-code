#=====================================================================
#   1018번:    체스판 다시 칠하기                   
#   @date:   2026-03-30              
#   @link:   https://www.acmicpc.net/problem/1018  
#   @Note:   폴더 내부에 있는 파일을 삭제하거나 변경하지 말아주세요.
#   @Test:   코드를 작성 후 "BOJ: 테스트"통해서 테스트를 해보세요.
#=====================================================================


import sys;
input = sys.stdin.readline

n, m = map(int, input().split())
# n = 줄, m = 한 줄의 요소 수

chess = []
answer = []

for _ in range(n):
    chess.append([list(input().strip())])

# 판떼기에서 8x8만큼 잘라야 한다.
def cnt_to_paint(x, y):
    count = 0
    first = chess[y][x]
    for i in range(y, y + 8):
        for j in range(x, x + 8):
            if (i+j) % 2 == 0: # 첫번째 칸과 색이 같아야 함
                if chess[i][j] != first:
                    count += 1
            else: # 첫번째 칸과 색이 달라야 함
                if chess[i][j] == first:
                    count += 1
    if count > 32: # 32개가 넘어가면 위에서 했던거 반대로 색 바꾸는 게 더 적게 소모됨
        count = 64 - count 
    return count

for i in range(n - 7):
    for j in range(m - 7):
        answer.append(cnt_to_paint(i, j))
    

print(min(answer))

