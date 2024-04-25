def bin_to_decimal(num):
    decimal = 0
    power = 0
    while num > 0:
        decimal += (num % 10) * (2 ** power)
        num //= 10
        power += 1
    return decimal

def oct_to_decimal(num):
    decimal = 0
    power = 0
    while num > 0:
        decimal += (num % 10) * (8 ** power)
        num //= 10
        power += 1
    return decimal

def hex_to_decimal(num):
    decimal = 0
    power = 0
    hex_map = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    for digit in num[::-1]:
        if digit.isdigit():
            decimal += int(digit) * (16 ** power)
        else:
            decimal += hex_map[digit.upper()] * (16 ** power)
        power += 1
    return decimal

def convert_to_decimal(base, num):
    if base == 'bin':
        return bin_to_decimal(num)
    elif base == 'oct':
        return oct_to_decimal(num)
    elif base == 'hex':
        return hex_to_decimal(num)
    else:
        return None

def main():
    base = input("Escolha a base de origem (bin, oct, hex): ")
    num = input("Digite o número: ")

    decimal = convert_to_decimal(base, num)
    while decimal is None:
        print("Número inválido!")
        num = input("Digite um novo número: ")
        decimal = convert_to_decimal(base, num)

    print(f"O número {num} na base {base} é igual a {decimal} na notação decimal.")

if __name__ == '__main__':
    main()