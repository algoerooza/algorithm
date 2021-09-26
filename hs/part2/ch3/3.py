# 게임 개발

n, m = map(int, input().split())
y, x, direct = map(int, input().split())

visited = [[0] * m for _ in range(n)] # 방문기록
visited[y][x] = 1

imap = []
for i in range(n):
  imap.append(list(map(int, input().split())))

# 북, 동, 남, 서
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
visitCnt = 1 # 방문수
turnCnt = 0 # 현재위치에서 회전수

while True:
  direct = (direct - 1 + 4) % 4 # 자신의 왼쪽 방향으로 전환
  nx = x + dx[direct]
  ny = y + dy[direct]
  turnCnt += 1
  # 1. 좌표를 벗어나지 않음 2. 방문안함 3. 육지
  if((0 <=nx and nx < m and 0 <= ny and ny < n) and visited[ny][nx] == 0 and imap[ny][nx] == 0):
    visitCnt += 1
    turnCnt = 0
    visited[ny][nx]=1
    x = nx
    y = ny
  # 네 방향 모두 갈 수 없으면
  if(turnCnt == 4):
    x -= dx[direct]
    y -= dy[direct]
    turnCnt=0
    # 만약 뒤가 바다면
    if(imap[y][x] == 1):
      break

print(visitCnt)
