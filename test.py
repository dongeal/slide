tiles_grid = [[1,2,3],[4,5,6],[7,8,0]]
tiles = []
for row, x in enumerate(tiles_grid):
    tiles.append([])
    
    for col, tile in enumerate(x):
        if tile !=0:
            tiles[row].append("A")
            
        else:
            tiles[row].append("Z")
        print (row, x, col, tile, tiles)
