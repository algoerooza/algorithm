#1이될때까지
n, k = map(int, input().split())

cnt = 0

# n이 1이상일 때까지 반복
while n > 1 :
  # 나누어떨어지면 k로 나누거 아니면 1 빼기
  if(n % k == 0) : 
    n //= k
  else:
    n -= 1
  cnt += 1

print(cnt)