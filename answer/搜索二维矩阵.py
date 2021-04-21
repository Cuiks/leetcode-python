from typing import List


def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    if not matrix:
        return False
    column = len(matrix)
    row = len(matrix[0])
    if target < matrix[0][0] or target > matrix[column - 1][row - 1]:
        return False
    left = 0
    right = column * row - 1
    cur_col = int(int((left + (right - left) / 2)) / row)
    cur_row = int((left + (right - left) / 2)) % row
    current = matrix[cur_col][cur_row]
    while current != target:
        if right - left <= 1:
            if target == matrix[int(right / row)][right % row] or target == matrix[int(left / row)][left % row]:
                return True
            return False
        if current > target:
            right = int((left + (right - left) / 2))
            cur_col = int(int((left + (right - left) / 2)) / row)
            cur_row = int((left + (right - left) / 2)) % row
            current = matrix[cur_col][cur_row]
        else:
            left = int((left + (right - left) / 2))
            cur_col = int(int((left + (right - left) / 2)) / row)
            cur_row = int((left + (right - left) / 2)) % row
            current = matrix[cur_col][cur_row]
    if current == target:
        return True
    else:
        return False


a = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
b = 13

print(searchMatrix(a, b))
