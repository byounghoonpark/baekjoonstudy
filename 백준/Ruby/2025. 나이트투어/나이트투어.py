import sys
input = sys.stdin.readline
write = sys.stdout.write

N = int(input())
sx, sy = map(int, input().split())
# 0-based
x, y = sx-1, sy-1

# 나이트 이동 8방향
moves = [(-2,-1),(-1,-2),(-2,1),(-1,2),(1,-2),(2,-1),(1,2),(2,1)]
# visited 체크: bytearray 로 0/1
visited = [bytearray(N) for _ in range(N)]

for step in range(1, N*N + 1):
    # 1) 현재 위치 출력
    write(f"{x+1} {y+1}\n")
    visited[x][y] = 1

    # 2) 마지막 칸이면 종료
    if step == N*N:
        break

    # 3) 다음 이동 후보 중 degree(후속 이동 수)가 가장 작은 곳 선택
    best = None  # (degree, nx, ny)
    for dx, dy in moves:
        nx, ny = x+dx, y+dy
        if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
            # 해당 칸의 degree 계산
            deg = 0
            for ddx, ddy in moves:
                tx, ty = nx+ddx, ny+ddy
                if 0 <= tx < N and 0 <= ty < N and visited[tx][ty] == 0:
                    deg += 1
            # 최소 degree 우선
            if best is None or deg < best[0]:
                best = (deg, nx, ny)

    # 4) 더 이상 갈 곳이 없으면 실패
    if best is None:
        write("-1 -1\n")
        sys.exit(0)

    # 5) 이동
    _, x, y = best