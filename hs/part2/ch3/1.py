# 큰수의법칙

n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort(reverse = True)

result = 0
result += (m // (k + 1)) * k * arr[0]
result += (m // (k + 1)) * arr[1]
result += (m % (k + 1)) * arr[0]

print(result)
