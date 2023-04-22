def main(tiles):
    play_game(tiles)

def print_grid_line(type, grid_size, row_size):
    if type == 0:
        print('┌' + '────┬' * (row_size-1) + '────┐')
    elif type != grid_size-1:
        print('├' + '────┼' * (row_size-1) + '────┤')
    else:
        print('└' + '────┴' * (row_size-1) + '────┘')

def print_cell(tile, tile_size, position='start'):

    if position != 'end':
        if tile_size == 0: print('│    ', end='')
        elif tile_size < 2: print(f'│  {tile} ', end='')
        else: print(f'│ {tile} ', end='')
    else:
        if tile_size == 0: print('│    │')
        elif tile_size < 2: print(f'│  {tile} │')
        else: print(f'│ {tile} │')

def display_board(input_tiles, row_size, grid_size):

    end = row_size
    print_grid_line(0, grid_size, row_size)
    for cell in range(grid_size):
        tile = input_tiles[cell]
        tile_size = len(tile)
        if cell < grid_size:
            if cell < end-1:                                # Internal tiles
                print_cell(tile, tile_size)
            else:                                           # Row-end tiles
                print_cell(tile, tile_size, 'end')
                print_grid_line(cell, grid_size, row_size)
                end += row_size                             # Start next row

def check_valid_move(tiles, row_size, grid_size, your_move):

    grid_array = [tiles[i:i+row_size] for i in range(0, grid_size, row_size)]
    for i in range(len(grid_array)):
        for j in range(len(grid_array[i])):
            if grid_array[i][j] == your_move:
                tile_row = i
                tile_col = j
    if (tile_row > 0 
    and grid_array[tile_row - 1][tile_col] == ''): return True # Check above
    if (tile_row < len(grid_array) - 1 
    and grid_array[tile_row + 1][tile_col] == ''): return True # Check below
    if (tile_col > 0 
    and grid_array[tile_row][tile_col - 1] == ''): return True # Check left
    if (tile_col < row_size - 1 
    and grid_array[tile_row][tile_col + 1] == ''): return True # Check right
    else: return False

def board_complete(input_tiles):

    if input_tiles[-1] == '':
        input_tiles_ints = [int(x) for x in input_tiles[0:len(input_tiles)-1]]
        are_sorted = sorted(input_tiles_ints)
        if input_tiles_ints == are_sorted: 
            return True
        else:
            return False
    else:
        return False
    
def swap_tile(input_tiles, your_move):

    i = input_tiles.index(your_move)
    j = input_tiles.index('')
    input_tiles[i], input_tiles[j] = input_tiles[j], input_tiles[i]
    
def you_win(turns):

    if turns == 1:
        print(f'You won in {turns} move. Congratulations!')
    else:
        print(f'You won in {turns} moves. Congratulations!')

def play_game(input_tiles):
    input_tiles = input_tiles.split(',')
    grid_size = len(input_tiles)
    row_size = int(grid_size**(1/2))
    turns = 0
    while board_complete(input_tiles) == False:
        display_board(input_tiles, row_size, grid_size)
        your_move = input('Your move: ')
        while (your_move not in input_tiles 
                or check_valid_move(input_tiles, row_size, grid_size, your_move) != True):
            if your_move == 'quit': exit()
            your_move = input(f'{your_move} is not valid. Try again.\nYour move: ')
        swap_tile(input_tiles, your_move); turns += 1
    display_board(input_tiles, row_size, grid_size)
    you_win(turns)

	
main("1,2,3,4,5,6,7,8,9,10,12,,13,14,11,15")