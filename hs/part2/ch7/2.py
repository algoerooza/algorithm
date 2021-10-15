# 부품 찾기
import sys

def binary(arr, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary(arr, target, mid+1, end)
    else:
        return binary(arr, target, start, mid-1)


n = int(input())
narr = list(map(int, sys.stdin.readline().rstrip().split()))
narr.sort()

m = int(input())
marr = list(map(int, sys.stdin.readline().rstrip().split()))
marr.sort()

for i in marr:
    result = binary(narr, i, 0, n-1)
    if(result == None):
        print("no", end=' ')
    else:
        print("yes", end=' ')





'''
5
8 3 7 9 2
3
5 7 9
'''