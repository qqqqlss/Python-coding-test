def solution(distance, rocks, n):
    answer = 0
    sorted_rocks = sorted(rocks)
    sorted_rocks.append(distance)
    left = 0
    right = distance
    while (left <= right):
        mid = int((left + right) / 2)
        cnt = 0
        p = 0
        for i in range(len(sorted_rocks)):
            if (sorted_rocks[i] - p < mid):
                cnt += 1
            else:
                p = sorted_rocks[i]
            print(p)
        if cnt > n:
            right = mid - 1
        else:
            left = mid + 1
            answer = mid
        print([left,right])
    return answer

distance=25
rocks=[2, 14, 11, 21, 17]
n=2

print(solution(distance, rocks, n))