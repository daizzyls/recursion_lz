
def convert_to_base(number: int, base: int) -> str:
    
    if not (2 <= base <= 16):
        raise ValueError("Основание системы счисления должно быть от 2 до 16.")
    
    alphabet = "0123456789ABCDEF"
    
    
    if number < 0:
        return "-" + convert_to_base(-number, base)
    
    
    if number < base:
        return alphabet[number]
    
    
    return convert_to_base(number // base, base) + alphabet[number % base]



if __name__ == "__main__":
    print(convert_to_base(255, 16)) 
    print(convert_to_base(255, 8))   
    print(convert_to_base(255, 10))  