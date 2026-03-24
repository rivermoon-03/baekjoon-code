#=====================================================================
#   14626번:    ISBN                   
#   @date:   2026-03-23              
#   @link:   https://www.acmicpc.net/problem/14626  
#   @Note:   폴더 내부에 있는 파일을 삭제하거나 변경하지 말아주세요.
#   @Test:   코드를 작성 후 "BOJ: 테스트"통해서 테스트를 해보세요.
#=====================================================================
import sys;
input = sys.stdin.readline

# 12개. 짝수는 가중치 1, 짝수는 3
# 인덱스로 생각하면 홀수 인덱스면 가중치 3, 짝수면 1.

isbn = list(input()); isbn.remove('\n')
pos = isbn.index('*')

isbn_sum = 0

# 10 - (a+3b+c+3d+e+3f+g+3h+i+3j+k+3l) mod 10 

for i in range(len(isbn)):
    if (i == pos): continue # * 부분은 계산 패스
    if (i % 2 == 0): isbn_sum += int(isbn[i])
    else: isbn_sum += 3 * int(isbn[i])

remainder = (10 - isbn_sum % 10) % 10
if pos % 2 == 1:  # 가중치 3인 경우, 3의 역원(mod 10) = 7
    print(remainder * 7 % 10)
else:
    print(remainder)

