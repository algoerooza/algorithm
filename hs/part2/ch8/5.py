# 효율적인 화폐 구성

n, m = map(int, input().split())
d = [10001] * 10001

arr = []
for i in range(n):
    arr.append(int(input()))

d[0] = 0

for i in range(1, m+1):
    for j in range(n):
        if (i-arr[j]) < 0:
            continue
        d[i] = min(d[i], d[i-arr[j]] + 1)

if(d[m] == 10001):
    print(-1)
else:
    print(d[m])

'''
2 15
2 
3
'''

'''
3 4
3
5
7
'''
