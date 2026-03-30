#=====================================================================
#   18110번:    solved.ac                   
#   @date:   2026-03-30              
#   @link:   https://www.acmicpc.net/problem/18110  
#   @Note:   폴더 내부에 있는 파일을 삭제하거나 변경하지 말아주세요.
#   @Test:   코드를 작성 후 "BOJ: 테스트"통해서 테스트를 해보세요.
#=====================================================================
import sys
input = sys.stdin.readline

def roundUp(n):
    return int(n + 0.5)

def main(): # return 쓰려고 함수로 선언
    n = int(input())
    if n == 0: # 입력에 0 들어오는 경우가 존재할 수 있음.
        print(0)
        return

    # 난이도 받고 정렬
    diff = []
    for _ in range(n): diff.append(int(input()))
    diff.sort()

    # 15% 반올림으로 절사 범위 정하기
    trim_rate = roundUp(n * 0.15)
    target_diff = diff[trim_rate : n - trim_rate] # 앞뒤 15% 자르기

    # 평균 계산
    print(roundUp(sum(target_diff) / len(target_diff)))

if __name__ == "__main__":
    main()