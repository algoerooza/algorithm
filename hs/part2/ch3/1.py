# 상하좌우

n = int(input()) 
# 이동방향
plan = input().split()

# 현재 위치 좌표
x,y = 1, 1

for i in plan:
  if(i == 'R' and (y+1) <= n):
    y+=1
  elif(i == 'L' and (y-1) >= 1):
    y-=1
  elif(i == 'D' and (x+1) <= n):
    x+=1
  elif(i == 'U' and (x-1) >= 1):
    x-=1

print(x, y)
