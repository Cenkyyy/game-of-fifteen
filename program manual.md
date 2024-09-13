# Program Manual

## Classes

### `Board`
Handles the board state and game mechanics.

#### Methods
- **`__init__`**: Initializes the board with the winning configuration, starting position and position of the empty space.
- **`print_board`**: Displays the current state of the board.
- **`shuffle_board(shuffle_count)`**: Shuffles the board by making a specified number of random moves.
- **`move_up(board, empty_space)`**: Moves a tile up, if the move is valid.
- **`move_down(board, empty_space)`**: Moves a tile down, if the move is valid.
- **`move_left(board, empty_space)`**: Moves a tile left, if the move is valid.
- **`move_right(board, empty_space)`**: Moves a tile right, if the move is valid.

### `Queue`
Implements a queue to assist the AI in solving the game.

#### Methods
- **`__init__`**: Initializes an empty queue.
- **`length()`**: Returns the length of the queue.
- **`is_empty()`**: Checks if the queue is empty.
- **`enqueue(stav)`**: Adds an item to the queue.
- **`dequeue()`**: Removes and returns the item at the front of the queue.

### `Game`
Handles the game logic and user interactions.

#### Methods
- **`__init__`**: Initializes the game with a new board.
- **`play_by_arrows()`**: Allows the player to control the game using arrow keys.
- **`play_by_keys()`**: Allows the player to control the game using WASD keys.
- **`solve_with_ai()`**: Uses a breadth-first search algorithm to solve the game automatically.

## Algorithm

- The algorithm uses a breadth-first search approach to find the shortest path to the solution.

### AI Algorithm steps:
1. Enqueues the starting board state and marks it as visited.
2. While queue isn't empty, dequeues a state and explores all possible moves (up, down, left, right).
3. If the winning board is reached, simulates the solution moves.
4. If the winnign board isn't reached yet, enqueues new game states and continues until the solution is found or all states are explored.
