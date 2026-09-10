def permut(lst: list) :
    
    if len(lst) <= 1:
        return [lst[:]]

    result = []

    
    for i in range(len(lst)):
        
        current = lst[i]
        
        
        remain = lst[:i] + lst[i+1:]
        
        
        for p in permut(remain):
            result.append([current] + p)

    return result


if __name__ == "__main__":
    example = [1, 2, 3]
    res = permut(example)
    print(f"permutations({example}) = {res}")