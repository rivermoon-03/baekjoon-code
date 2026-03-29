#=====================================================================
#   1966번:    프린터 큐                   
#   @date:   2026-03-29              
#   @link:   https://www.acmicpc.net/problem/1966  
#   @Note:   폴더 내부에 있는 파일을 삭제하거나 변경하지 말아주세요.
#   @Test:   코드를 작성 후 "BOJ: 테스트"통해서 테스트를 해보세요.
#=====================================================================

import sys;

input = sys.stdin.readline

# 테스트케이스
testCase = int(input())
# 전체 과정
for _ in range(testCase):
    # 사이클 하나
    n, m = map(int, input().split())
    doc = list(map(int, input().split()))
    
    printed_times = 1
    
    while True:
        # 지금 인쇄할 문서의 중요도보다 더 중요한 게 큐에 있는가?
        if doc[0] < max(doc): doc.append(doc.pop(0)) # 있다면 가장 앞의 문서를 뗴어다가 다시 큐의 맨 뒤에 붙이기
        else: # 지금 인쇄할 문서가 가장 중요할 경우
            if m == 0: break # 그게 우리가 찾는 문서였다면 빠져나가기
            doc.pop(0) # 인쇄!
            if len(doc) == 0: break
            printed_times += 1 # 인쇄가 되었으므로 인쇄 횟수에 1회 추가
            
            
        # m은 우리가 뽑아야 할 문서의 인덱스.
        # 앞의 문서들이 뽑아지던 뒤에 붙어지던 우리가 뽑아야 할 문서의 인덱스는 1씩 줄어든다.
        # 우리의 문서가 뽑힐 차례인데 큐에 더 중요한 문서가 있다면, 맨 뒤 (doc[len(doc) - 1] 로 옮겨질 것.)
        if m > 0: m = m - 1
        else: m = len(doc) - 1
        
        
    print(printed_times)
    
    
    
    
    
    
    
    
    

