def solution(numbers): 
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True) #1000까지 수가 있어서 str3번 반복해서 붙이고 사전순으로 내림차 정렬
    return str(int(''.join(numbers)))

# def solution(numbers):
#     s=[]
#     answer=""
#     for i in numbers:
#         if len((str(i))) == 1:
#             c = str(i) * 6
#         elif len((str(i))) == 2:
#             c = str(i) * 3
#         elif len((str(i))) == 3:
#             c = str(i) * 2
#         else:
#             c = "100000"
#         s.append([int(c) ,  i])
#     s.sort(reverse=True)
#     for i in s:
#         answer+=str(i[1])
#     return str(int(answer))


