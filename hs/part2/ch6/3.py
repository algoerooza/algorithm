n = int(input())

arr = []
for i in range(n):
  temp = input().split()
  arr.append((temp[0], temp[1]))

arr.sort(key = lambda a : a[1])

for i in range(n):
  print(arr[i][0], end = " ")


'''
2
홍길동 95
이순신 77
'''