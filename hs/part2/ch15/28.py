def find(arr, start, end):
    if(start > end):
        return -1

    mid = (start + end) // 2

    # 고정점이면
    if arr[mid] == mid:
        return mid
    # 중앙값이 index값보다 크면 왼쪽 확인
    elif arr[mid] > mid:
        return find(arr, start, mid-1)
    # 중앙값이 index값보다 작으면 오른쪽 확인
    else:
        return find(arr, mid+1, end)

n = int(input())
arr = list(map(int, input().split()))

print(find(arr, 0, n-1))

'''
5
-15 -6 1 3 7
'''
'''
7
-15 -4 2 8 9 13 15
'''
'''
7
-15 -4 3 8 9 13 15
'''