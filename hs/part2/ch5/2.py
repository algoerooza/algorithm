from collections import deque

n, m = map(int, input().split())

gragh = []
for i in range(n):
  gragh.append(list(map(int, input()))) 

# 방문 여부 확인용 (False : 미방문, True : 방문)
visited = [[False] * m for _ in range(n)]

# 위, 아래, 오른쪽, 아래 이동
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
  q = deque()
  # q에 들어가는 값은 (x, y)좌표, 시작점으로부터 거리(= 최단거리)
  q.append((x, y, 1))
  visited[y][x] = True

  while q:
    v = q.popleft()
    # 출구 발견
    if(v[0] == m-1 and v[1] == n-1):
      return v[2]
    for i in range(4):
      nx = v[0] + dx[i]
      ny = v[1] + dy[i]
      # 그래프 범위 벗어나는지 검사
      if(0<= nx and nx < m and 0<= ny and ny < n):
        # 1. 방문안하고 2. 괴물 없는 부분
        if(not visited[ny][nx] and gragh[ny][nx]):
          q.append((nx, ny, v[2]+1))

print(bfs(0, 0))
      
'''
5 6
101010
111111
000001
111111
111111
'''