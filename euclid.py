
def BiggestGeneralDevider(a: int, b: int) -> int:

    if b == 0:
        return abs(a)
        
    return BiggestGeneralDevider(b, a % b)

def main():
    x = 75
    y = 25
    result = BiggestGeneralDevider(x, y)
    print(f"gcd({x}, {y}) = {result}")
    
if __name__ == "__main__":
    main()
    