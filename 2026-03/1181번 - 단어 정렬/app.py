#=====================================================================
#   1181번:    단어 정렬                   
#   @date:   2026-03-24              
#   @link:   https://www.acmicpc.net/problem/1181  
#   @Note:   폴더 내부에 있는 파일을 삭제하거나 변경하지 말아주세요.
#   @Test:   코드를 작성 후 "BOJ: 테스트"통해서 테스트를 해보세요.
#=====================================================================

import sys;

input = sys.stdin.readline

n = int(input())
words = [input().strip() for i in range(n)]

words = list(set(words)) # 중복제거
words.sort() # 단어 정렬

words.sort(key = len) # 글자 수 정렬


for i in words:
    print(i)