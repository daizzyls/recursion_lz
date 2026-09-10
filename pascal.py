
def pascal_triangle(n: int) -> list:

    if n <= 0:
        return []
    if n == 1:
        return [[1]]
    
    prev_triangle = pascal_triangle(n - 1)
    last_row = prev_triangle[-1]

   
    new_row = [1]
    
    for i in range(len(last_row) - 1):
        new_row.append(last_row[i] + last_row[i + 1])

    new_row.append(1)

    prev_triangle.append(new_row)
    return prev_triangle


if __name__ == "__main__":
    n = 5
    result = pascal_triangle(n)
    print(f"pascal_triangle({n}) = [")
    for row in result:
        print(f"    {row},")
    print("]")