import random
import time
from copy import deepcopy
from pynput import keyboard
from pynput.keyboard import Key

# Board size
ROWS = 4
COLUMNS = 4

class Board:
    def __init__(self):
        print('Game of Fifteen\n')
        
        # winning board state
        self.winning_board = [[' 1', ' 2', ' 3', ' 4'], 
                              [' 5', ' 6', ' 7', ' 8'],
                              [' 9', '10', '11', '12'],
                              ['13', '14', '15', '__']]

        # starting board state
        self.current_board = [[' 1', ' 2', ' 3', ' 4'],
                              [' 5', ' 6', ' 7', ' 8'],
                              [' 9', '10', '11', '12'],
                              ['13', '14', '15', '__']]

        # position of the empty space
        self.empty_space = [ROWS - 1, COLUMNS - 1]    

    # displays current board state
    def print_board(self):
        for i in range(ROWS):
            for j in range(COLUMNS):
                print(self.current_board[i][j], end = ' ')
            print()

    # shuffle the board, make shuffle_count amount of random moves
    def shuffle_board(self, shuffle_count):
        random_moves_made_count = 0

        while random_moves_made_count < shuffle_count:
            # choose a random move index and make a move
            random_move_index = random.randint(0,3)

            if random_move_index == 0 and self.empty_space[0] > 0:
                self.move_up(self.current_board, self.empty_space)
            elif random_move_index == 1 and self.empty_space[0] < 3:
                self.move_down(self.current_board, self.empty_space)
            elif random_move_index == 2 and self.empty_space[1] > 0:
                self.move_left(self.current_board, self.empty_space)
            elif random_move_index == 3 and self.empty_space[1] < 3:
                self.move_right(self.current_board, self.empty_space)

            if random_move_index >= 0 and random_move_index <= 3:
                random_moves_made_count += 1
        
        print('\nThis is how the board looks like after', shuffle_count, 'number of random moves, good luck!')     
        
        self.print_board()
        print()

        return self.current_board, self.empty_space

    def move_up(self, board, empty_space):
        # check for validity of the move
        if empty_space[0] <= ROWS - 1 and empty_space[0] - 1 >= 0 and empty_space[1] <= COLUMNS - 1 and empty_space[1] >= 0:
            # update empty space's position
            board[empty_space[0]][empty_space[1]], board[empty_space[0] - 1][empty_space[1]] = board[empty_space[0] - 1][empty_space[1]], board[empty_space[0]][empty_space[1]]
            empty_space[0] -= 1
        
        return board, empty_space
    
    def move_down(self, board, empty_space):
        # check for validity of the move
        if empty_space[0] + 1 <= ROWS - 1 and empty_space[0] >= 0 and empty_space[1] <= COLUMNS - 1 and empty_space[1] >= 0:
            # swap and update empty space's position
            board[empty_space[0]][empty_space[1]], board[empty_space[0] + 1][empty_space[1]] = board[empty_space[0] + 1][empty_space[1]], board[empty_space[0]][empty_space[1]]
            empty_space[0] += 1
        
        return board, empty_space
    
    def move_left(self, board, empty_space):
        # check for validity of the move
        if empty_space[0] <= ROWS - 1 and empty_space[0] >= 0 and empty_space[1] <= COLUMNS - 1 and empty_space[1] - 1 >= 0:
            # swap and update empty space's position
            board[empty_space[0]][empty_space[1]], board[empty_space[0]][empty_space[1] - 1] = board[empty_space[0]][empty_space[1] - 1], board[empty_space[0]][empty_space[1]]
            empty_space[1] -= 1

        return board, empty_space
    
    def move_right(self, board, empty_space):
        # check for validity of the move
        if empty_space[0] <= ROWS-1 and empty_space[0] >= 0 and empty_space[1]+1 <= COLUMNS-1 and empty_space[1] >= 0:
            # swap and update empty space's position
            board[empty_space[0]][empty_space[1]], board[empty_space[0]][empty_space[1]+1] = board[empty_space[0]][empty_space[1]+1], board[empty_space[0]][empty_space[1]]
            empty_space[1] += 1
        
        return board, empty_space

class Queue:
    def __init__(self):
        self.board = []    

    def length(self):
        return len(self.board)
    
    def is_empty(self):
        return self.length() == 0    
    
    def enqueue(self, stav):
        self.board.append(stav) 
        
    def dequeue(self):
        if self.is_empty():
            print('Queue is empty')
            return False
        else:    
            return self.board.pop(0)

class Game:
    def __init__(self):
        self.board = Board()
        self.moves_count = 0    
    
    def play_by_arrows(self):
        '''
        You play by using:
        - arrow up = move up
        - arrow down = move down
        - arrow left = move left
        - arrow right = move right
        - esc = exit the game and surrender
        - left shift = let AI solve the game for you
        '''
        
        # in case board is shuffled into a winning state
        if self.board.current_board == self.board.winning_board:
            print('Congrats, you won without moving!')
            return False        

        # make a move based on clicked key
        def on_key_release(key): 
            nonlocal self
            was_move_made = False

            if key == Key.up:
                self.board.current_board, self.board.empty_space = self.board.move_up(self.board.current_board, self.board.empty_space)
                was_move_made = True
            elif key == Key.down:
                self.board.current_board, self.board.empty_space = self.board.move_down(self.board.current_board, self.board.empty_space)
                was_move_made = True
            elif key == Key.left:
                self.board.current_board, self.board.empty_space = self.board.move_left(self.board.current_board, self.board.empty_space)
                was_move_made = True
            elif key == Key.right:
                self.board.current_board, self.board.empty_space = self.board.move_right(self.board.current_board, self.board.empty_space)
                was_move_made = True
            elif key == Key.esc:
                print('Looks like you chose to surrender...')
                time.sleep(3)
                listener.stop()
            elif key == Key.shift_l:
                game.solve_with_ai()
                time.sleep(1)
                listener.stop()
             
            if was_move_made:
                self.board.print_board()
                print()
                self.moves_count += 1

            if self.board.current_board == self.board.winning_board:
                if key != Key.shift_l:    
                    print('Congrats, you won')
                    print('You managed to win in', self.moves_count, 'moves.')
                    time.sleep(3)
                    listener.stop()
        
        # create a listener and start catching released keys
        with keyboard.Listener(on_release = on_key_release) as listener:    
            listener.join()
    
    # game is played by using WASD
    def play_by_keys(self):        
        global moves_count
        was_move_made = False
        
        while True:
            if self.board.current_board == self.board.winning_board:
                print('Congrats, you won!')
                print('You managed to win in', self.moves_count, 'moves.')
                return False
            
            move = input('Choose direction you would like to go to (WASD / wasd): ')
            if move == 'w' or move == 'W':
                self.board.current_board, self.board.empty_space = self.board.move_up(self.board.current_board, self.board.empty_space)
                was_move_made = True
            elif move == 's' or move == 'S':
                self.board.current_board, self.board.empty_space = self.board.move_down(self.board.current_board, self.board.empty_space)
                was_move_made = True
            elif move == 'a' or move == 'A':
                self.board.current_board, self.board.empty_space = self.board.move_left(self.board.current_board, self.board.empty_space)
                was_move_made = True
            elif move == 'd' or move == 'D':
                self.board.current_board, self.board.empty_space = self.board.move_right(self.board.current_board, self.board.empty_space)
                was_move_made = True
            elif move == 'e' or move == 'E':
                print('Looks like you decided to give up huh...')    
                return False
            elif move == 'q' or move == 'Q':
                game.solve_with_ai()
                return False 

            if was_move_made:
                self.board.print_board()
                print()
                self.moves_count += 1
    
    def solve_with_ai(self):
        queue = Queue()

        # keep track of visited game states
        visited = [] 

        # enqueue starting position, keep track of board, empty space, and moves it took to finish the game
        queue.enqueue((self.board.current_board, self.board.empty_space, []))

        def possible_moves(board, empty_space):
            # use deepcopy to prevent any possible mistake / error
            possible_moves = [self.board.move_up(deepcopy(board), deepcopy(empty_space)),
                              self.board.move_down(deepcopy(board), deepcopy(empty_space)),
                              self.board.move_left(deepcopy(board), deepcopy(empty_space)),
                              self.board.move_right(deepcopy(board), deepcopy(empty_space))]
            return possible_moves            

        print('Beep, calculating...\n')
        
        while not queue.is_empty():
            board, empty_space, moves = queue.dequeue()                
            
            for i in range(len(possible_moves(board, empty_space))):
                possible_move = possible_moves(board, empty_space)[i]

                # possible_moves_position[0] = current board, possible_moves_position[1] = empty space position
                possible_moves_position = (deepcopy(possible_move[0]), deepcopy(possible_move[1]))
                
                if possible_moves_position[0] == self.board.winning_board:
                    # remember the move's index
                    moves += [i]
                    
                    # simulate the moves to win the game, make each move after 1 second
                    for move_index in moves:
                        if move_index == 0:
                            self.board.current_board, self.board.empty_space = self.board.move_up(self.board.current_board, self.board.empty_space)
                            self.board.print_board()
                            print()
                            time.sleep(1)
                        elif move_index == 1:
                            self.board.current_board, self.board.empty_space = self.board.move_down(self.board.current_board, self.board.empty_space)
                            self.board.print_board()
                            print()
                            time.sleep(1)
                        elif move_index == 2:
                            self.board.current_board, self.board.empty_space = self.board.move_left(self.board.current_board, self.board.empty_space)
                            self.board.print_board()
                            print()
                            time.sleep(1)
                        elif move_index == 3:
                            self.board.current_board, self.board.empty_space = self.board.move_right(self.board.current_board, self.board.empty_space)
                            self.board.print_board()
                            print()
                            time.sleep(1)
                        self.moves_count += 1
                        
                    print('AI has found a solution!')
                    print('Game could have been won in', self.moves_count, 'moves.')
                    return False
                
                # if new game state has been found
                if possible_moves_position[0] not in visited:

                    # enqueue the new game state and add it to visited 
                    queue.enqueue((possible_moves_position[0],possible_moves_position[1], moves + [i])) # moves = [1,2,3] -> moves + [2] -> print(moves) -> [1,2,3,2]    
                    visited.append(possible_move[0])
        
        print('Solution wasn\'t found')       

if __name__ == "__main__":
    game = Game()
    
    # display starting board
    print('Here\'s how the winning board looks like, try and recreate it!')
    game.board.print_board()
    print()    
    
    # shuffle the board
    while True:
        try:
            shuffle_count = int(input('Choose how many times you want to shuffle the board: '))
            if shuffle_count > 0: 
                # shuffle and display board
                game.board.shuffle_board(shuffle_count)
                break
            else:
                print('Please choose a positive number')
        except ValueError:
            print('Please choose a positive number')
        except EOFError:
            print('Please choose a positive number')
    
    # choose the way how to play
    play_option = input('Choose the way you want to play: arrows -> 1, writing keys -> 2: ')
    while True:
        try:
            if play_option == '1':
                print('\nInstructions:\narrow up -> move up\narrow down -> move down\narrow left -> move left\narrow right -> move right\nleft shift -> game will be solved by AI\nesc -> surrender the game and exit\n\nSTART!')
                game.play_by_arrows()
                break
            elif play_option == '2':
                print('\nInstructions:\nw/W -> move up\ns/S -> move down\na/A -> move left\nd/D -> move right\nq/Q -> game will be solved by AI\ne/E -> surrender the game and exit\n\nSTART!')
                game.play_by_keys()
                break
            play_option = input('Choose the way you want to play: arrows -> 1, writing keys -> 2: ')
        except EOFError:
            play_option = input('Choose the way you want to play: arrows -> 1, writing keys -> 2: ')


