special_coins_pos = [(1, 1), (14, 1), (1, 13), (14, 13)]
center_pos = [(12, 7), (11, 7), (13, 7), (14, 7)]

def create_board():

    # TODO Create a board with the following structure
    # 1 -> Wall
    # 0 -> Path
    
    maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], # Top boundary
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], # Path
    [1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1], # Internal walls
    [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1], # Paths
    [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1], # Complex paths
    [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1], # Open path area
    [1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1], # Narrow passage
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1], # Large open path
    [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1], # Solid wall section
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], # Path
    [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1], # Complex wall structure
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1], # More paths
    [1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1], # Internal walls
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], # Open path
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], # Extra boundary row
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], # Extra boundary row
    ]

    return maze

def create_coins(board):
    coins = []

    for x in range(len(board)-1):
        for y in range(len(board[x])-1):
            if board[y][x] == 0:
                coins.append((x,y))
    print(coins)
    for i in special_coins_pos:
        coins.remove(i)
    # for j in center_pos:
    #     j = (j[1], j[0])
    #     print(j)
    #     coins.remove(j)

    return coins

def create_special_coins(board):
    return special_coins_pos


