def print_board(board):
    for row in board:
        print("".join(row))
    print("\n" + "-" * (2 * len(board) - 1) + "\n")

def is_safe(board, row, col):
    for i in range(row):
        if board[i][col] == 'Q':
            return False
    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i][j] == 'Q':
            return False
    for i, j in zip(range(row - 1, -1, -1), range(col + 1, len(board))):
        if board[i][j] == 'Q':
            return False
    return True

def solve_n_queens(n):
    def backtrack(board, row):
        if row == n:
            solution = ["".join(row) for row in board]
            solutions.append(solution)
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row][col] = 'Q'
                backtrack(board, row + 1)
                board[row][col] = '.'

    board = [['.' for _ in range(n)] for _ in range(n)]
    solutions = []
    backtrack(board, 0)
    return solutions

def main(n):
    solutions = solve_n_queens(n)
    print(f"共有{len(solutions)}种方案！")
    for idx, solution in enumerate(solutions, start=1):
        print(f"第{idx}个方案")
        for line in solution:
            print(line)
        print("-" * (2 * n))

# 输入棋盘尺寸
n = 4 
main(n)
print('许会杰','2125120073')
