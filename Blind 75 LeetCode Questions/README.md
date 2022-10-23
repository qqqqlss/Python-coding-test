# Blind 75 LeetCode Questions
# grind75
https://leetcode.com/discuss/general-discussion/460599/blind-75-leetcode-questions
https://www.techinterviewhandbook.org/grind75?weeks=8&hours=8
---
01_TwoSum - pair 값이 정해져있다는 것 과 dict[key] 는 시간복잡도O(1) 이용해 시간 복잡도 O(2N) 내가푼건 O(N^2/2)
02_Valid Parentheses - dict이용하면 코드 간결하게, 리스트를 빈리스트가 아닌 값으로 초기화해 아무것도 없을 떄 pop하면 오류나는 것 방지  / 괄호 회전하기.py랑 비슷
03_Merge Two Sorted Lists -  연결 리스트 활용, 계속 넥스트에 바꿔가며 대입. / 파이썬에서는 필요없음.
04_Best Time to Buy and Sell Stock - 쉬움.
05_Valid Palindrome - isalnum 사용
06_Invert Binary Tree - 서로 값 바꿀 때 한줄에 입력하면 됨(튜플로 인식하기 때문) ex)x,y=y,x --> temp=(x,y) // y,x=temp
07_Valid Anagram - 확실히 파이썬은 다양한 방법이 가능. dict이용하는게 가장 깔끔한거 같음. collections.Counter사용해서도 가능
08_Binary Search - 이진탐색 이용 ( velog에 있음 ) O(logN)
09_Flood Fill - dfs, bfs사용 4방향 탐색.