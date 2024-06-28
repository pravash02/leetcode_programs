def nearestExit(maze, entrance):
    row = len(maze)
    col = len(maze[0])
    if row == 0 and col == 0:
        return -1
    itlist = [[entrance, 0]]
    maze[entrance[0]][entrance[1]] = '+'
    moves = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    while itlist:
        it_entrance = itlist[0][0]
        x = it_entrance[0]
        y = it_entrance[1]
        dist = itlist[0][1]
        itlist.pop(0)
        dist = dist + 1
        for i in range(4):
            xin = x + moves[i][0]
            yin = y + moves[i][1]
            if xin < 0 or yin < 0 or xin >= row or yin >= col or maze[xin][yin] == '+':
                continue
            elif xin == 0 or yin == 0 or xin == row - 1 or yin == col - 1:
                return dist
            itlist.append([[xin, yin], dist])
            maze[xin][yin] = '+'

    return -1


maze = [["+", "+", ".", "+"], [".", ".", ".", "+"], ["+", "+", "+", "."]]
entrance = [1, 2]
print(nearestExit(maze, entrance))
