n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

# a는 오름차순, b는 내림차순
a.sort(reverse=False)
b.sort(reverse=True)

for i in range(k):
  if a[i] < b[i]:
    a[i], b[i] = b[i], a[i]
  else:
    break

print(sum(a))

'''
5 3
1 2 5 4 3
5 5 6 6 5
'''