def matrix_dot_vector(a: list[list[int | float]], b: list[int | float]) -> list[int | float]:
    # Return -1 if the matrix is empty or column count doesn't match vector length
    if not a or len(a[0]) != len(b):
        return -1

    result = []
    for row in a:
        # Ensure jagged matrices are caught if rows vary in length
        if len(row) != len(b):
            return -1
        row_dot = sum(x * y for x, y in zip(row, b))
        result.append(row_dot)

    return result