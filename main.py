def dfs_n_queens(n):
    def backtrack(row):
        if row == n:
            solution = ["".join(row_chars) for row_chars in board]
            results.append(solution)
            return

        for col in range(n):
            if columns_used[col] == 0 and diagonals_used[row + col] == 0 and anti_diagonals_used[n - row + col] == 0:
                board[row][col] = "Q"
                columns_used[col] = 1
                diagonals_used[row + col] = 1
                anti_diagonals_used[n - row + col] = 1
                backtrack(row + 1)
                columns_used[col] = 0
                diagonals_used[row + col] = 0
                anti_diagonals_used[n - row + col] = 0
                board[row][col] = "."
    
    results = []
    board = [["."] * n for _ in range(n)]
    columns_used = [0] * n
    diagonals_used = [0] * (2*n)
    anti_diagonals_used = [0] * (2*n)
    backtrack(0)
    resultscopy = results.copy()
    if n < 1:
        return []
    resultsindex = []
    for result in resultscopy:
        resultindex = [i.index("Q") for i in result]
        resultsindex.append(resultindex)
    
    return resultsindex

print(dfs_n_queens(0))
print(dfs_n_queens(1))
print(dfs_n_queens(2))
print(dfs_n_queens(3))
print(dfs_n_queens(4))
print(dfs_n_queens(5))
print(len(dfs_n_queens(5)))
print(len(dfs_n_queens(8)))
