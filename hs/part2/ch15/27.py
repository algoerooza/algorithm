# 정렬된 배열에서 특정 수의 개수 구하기

from bisect import bisect_left, bisect_right

def count_by_range(arr, left_value, right_value):
    return bisect_right(arr,x) - bisect_left(arr, x)


n, x = map(int, input().split())
arr = list(map(int, input().split()))

result = count_by_range(arr, x, x)

if result == 0:
    print(-1) 
else:
    print(result)

'''
7 2
1 1 2 2 2 2 3
'''
'''
7 4
1 1 2 2 2 2 3
'''