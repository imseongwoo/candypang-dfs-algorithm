num = 1


def dfs(x, y):
    global num
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= 7 or ny < 0 or ny >= 7:  # 좌표가 매트릭스 안에 속하지않는지
            continue
        if not visited[nx][ny] and graph[nx][ny] == graph[x][y]:    # false 값이고 그 전 노드와 값이 일치하면
            num += 1                                                #전역변수의 값을 1 증가시킨다, 그 이후 재귀함수
            dfs(nx, ny)


count = 0
graph = []
for i in range(7):
    graph.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

visited = [[False] * 7 for _ in range(7)]

for i in range(7):
    for j in range(7):
        num = 1                                                     # 반복문 실행 시 전역변수 값 1로 초기화
        dfs(i, j)
        if num >= 3:
            count += 1

print(count)
