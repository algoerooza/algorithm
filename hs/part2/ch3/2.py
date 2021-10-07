# 숫자카드게임

n, m = map(int, input().split())
arr = []
for _ in range(n):
  arr.append(list(map(int, input().split())))

# 각 행 리스트마다 오름차순 정렬
for i in range(n):
  arr[i].sort()

# 모든 행 첫번째 요소 기준으로 내림차순 정렬
arr.sort(key = lambda x: x[0], reverse = True)

print(arr[0][0])
