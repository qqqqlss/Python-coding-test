# Python-coding-test
---
=======
**프로그래머스 고득점kit 유형별 폴더**
**Leetcode 75 폴더**

**level2**
두 큐 합 같게 만들기 - 이중 큐 문제 / 사고력 필요 / while문 i<2*t 이해안가서 애먹음  
양궁대회 - 완전 탐색 문제 / 비트연산 이용한 승패 경우의수 / reversed() / 1<<5 = 100000(2진수) / 비트와 비트의 and 연산 / 경이롭다.  
주차 요금 계산 - dict 이용(sorted: key기준 정렬) / 문자열 split  
k진수에서 소수 개수 구하기 - math 안쓰고 소수 구하기 / 몫연산자://  
n^2 배열 자르기 - 좀더 쉽게 생각하자.  
최댓값과 최솟값 --  
교점에 별 만들기 - combinations(조합) 사용 / list 이차원 리스트  최소 최대 구하기 / lambda정렬, reversed  
빛의 경로 사이클 - 어떻게 보면 4중 for문. / 어려워보여도 차근차근 문제보고 하면 된다.!!!! 끈기있게!!  
거리두기 확인하기 - 노가다성 문제 하면 된다!!  
두개 이하로 다른 비트 - 이진수 -> 십진수, 십진수 -> 이진수, 비트 연산  
행렬 테두리 회전하기 - 행렬 다루기.. xy약간 헷갈렷음  
괄호 회전하기 - ([)]는 안돼서 stack을 이용해 푸니 깔끔.  
순위 검색 - 이분탐색, setdefault 사용 / 데이터 사용시 방대할 시 극한까지 효율성을 높여야 한다.  
메뉴 리뉴얼 - combinations, sorted, defaultdict 활용 // 풀이 자체가 매끄러운지는 모르게다. 정렬의 반복  
혼자 놀기의 달인 - set활용 // 차례로 그룹 찾기.. 은근 어렵  
택배 상자 - 효율성 중요(order에 box넘어갔을때 sup에 없으면 break) // 잘생각하기  
야간 전술 보행 - 앞에 정렬에 시간씀 ..// 경비 구간만 정렬해서 테스트하면 훨씬 빠름!   
롤케이크 자르기 - set으로 변환은 효율성down / index저장해 효율성 높임 // defaultdict, counter사용버전도 잇으나 내게 제일 빠름  
연속 부분 수열 합의 개수 - 효율성 어떻게 높일지 모르겠음../ set,sum 활용  
할인 행사 - dict,zip 이용  
후보키 - for else, combinations, set.subset 사용 / 어렵다 .. 나중에 다시봐줘  
이진 변환 반복하기 - format사용(이진수->십진수)  
쿼드압축 후 개수 세기 - 재귀함수 이용 똑똑하게 풀음.  
삼각 달팽이 - while 2번, 그래프 방문, extend이용 이차원 ->일차원 리스트  
수식 최대화 - permutations 사용 // pop, insert이용 리스트 수정  
튜플 - lstrip,rstrip 사용 // .sort(key = len) 길이 기준 정렬 // 문자열 나누기 참고하기!!  
멀쩡한 사각형 - math(floor, ceil, gcd) 사용 / 수학적 계산 필요..어렵  
괄호 변환 - 문제가 표현한 알고리즘 그대로 표현  
우박수열 정적분 - 쉽지만 문제를 잘읽자..  
문자열 압축 - 문제 잘읽자....  
푸드 파이트 - list[::-1] 문자열 reverse  
햄버거 만들기 - list.pop() 시간 복잡도 O(1)  
등대 - 재귀 깊이 설정, Treenode, 중복 생각, 문제 잘못이해함..제대로봐라!!!  
옹알이(2) - 단순  
콜라 문제 - 처음에 b개수를 생각못함.. 바보..  
부대 복귀 - 반대로 생각하면 한번에 가능한 거였음.. bfs  
삼총사 - combinations쓰니깐 쉬움  
2022_2kb_2 - heapq이용  
숫자 짝꿍 - counter (import Counter 보다 빠름) STR 리스트로 추가해서 나중에 join으로 합치는거보다 +=로 합치는게 훨씬 빠름.  
2차원 동전 뒤집기 - 천재가 만들었나.. 진짜 생각 잘했다. 덕분에 deepcopy배움, ^연산  
고고학 최고의 발견 - 어렵다. product 사용 N*N보다는 N에다가 한줄 씩 채워가며 조금이라도 시간을 줄임.  
카운트 다운 - 순서대로 차근차근 bfs, 생각이 중요하다. 너무 거져먹으려 하지 말자  
숫자 카드 나누기 - gcd,lcm  
과일 장수 --  
행렬 연산 - deque appendleft,popleft이용 효율성up, rotate도 너무 O(k)라 너무 유용 duque 이용 잘하자!!!  
성격 유형 검사히기 - dict사용 쉬움  
기사단원의 무기 - 약수는 짝지으므로 제곱근까지만 탐색해도 충분.  
등산코스 정하기 - 노드를 여러번 방문할 수 있는데 visit을 체크할 떄 intensity가 더 작을 때만 방문. (코드는 거짓말 안함)  
코딩 테스트 공부 - 알고력, 코딩력에 최소값 저장하면서 나아감. (비교적 간단 bfs)  
명예의 전당 - heap 사용 (빠름) 