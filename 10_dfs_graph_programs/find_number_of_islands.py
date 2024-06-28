def check(i, j, n, m):
    return i >= 0 and j >= 0 and i < n and j < m


def mark_component(v, vis, i, j, n, m):
    if not check(i, j, n, m):
        return

    vis[i][j] = True
    if v[i][j] == 1:
        v[i][j] = 0

        mark_component(v, vis, i + 1, j, n, m)
        mark_component(v, vis, i - 1, j, n, m)
        mark_component(v, vis, i, j + 1, n, m)
        mark_component(v, vis, i, j - 1, n, m)
        mark_component(v, vis, i + 1, j + 1, n, m)
        mark_component(v, vis, i - 1, j - 1, n, m)
        mark_component(v, vis, i + 1, j - 1, n, m)
        mark_component(v, vis, i - 1, j + 1, n, m)


v = [[1, 1, 0, 0, 0],
     [0, 1, 0, 0, 1],
     [1, 0, 0, 1, 1],
     [0, 0, 0, 0, 0],
     [1, 0, 1, 0, 1]]
n = len(v)
m = len(v[0])
cnt = 0
vis = [[False for j in range(m)] for i in range(n)]

for i in range(n):
    for j in range(m):
        if not vis[i][j] and v[i][j] == 1:
            cnt += 1
            mark_component(v, vis, i, j, n, m)

print(cnt)
