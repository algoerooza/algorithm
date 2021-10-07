# 위에서 아래로

n = int(input())
arr = []

for _ in range(n):
  arr.append(int(input()))

arr.sort(reverse = True)

for i in range(n):
  print(arr[i], end = " ")


'''
3
15
27
12
'''