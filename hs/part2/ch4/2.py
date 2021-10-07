# 왕실의 나이트

data = input()
x = int(data[1]) # 행
y = ord(data[0]) - ord('a') + 1 # 열 ex) a: 1, b: 2...


dx = [2, 2, -2, -2, 1, -1, 1, -1]
dy = [1, -1, 1, -1, 2, 2, -2, -2]
cnt = 0

# 움직일 수 있는 경우의 수 모두 탐색
for i in range(8):
  nx = x + dx[i]
  ny = y + dy[i]
  if( 1 <= nx and nx <= 8 and 1 <= ny and ny <= 8):
    cnt += 1

print(cnt)
