n, m = map(int, input().split())

gragh = []
for i in range(n):
  gragh.append(list(map(int, input()))) 

# 방문 여부 확인용 (False : 미방문, True : 방문)
visited = [[False] * m for _ in range(n)]

# 위, 아래, 오른쪽, 아래 이동
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y):
  visited[y][x] = True

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    # 그래프 범위 벗어나는지 검사
    if(0<= nx and nx < m and 0<= ny and ny < n):
      # 1. 방문안하고 2. 칸막이 없는곳
      if(not visited[ny][nx] and not gragh[ny][nx]):
        dfs(nx, ny)

cnt = 0

for i in range(n):
  for j in range(m):
    # 1. 방문안하고 2. 칸막이 없는곳
    if(not visited[i][j] and not gragh[i][j]):
      dfs(j, i)
      cnt += 1

print(cnt) # 정답

'''
4 5
00110
00011
11111
00000
'''
'''
15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111
'''




