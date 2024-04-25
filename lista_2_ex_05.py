def bin_to_dec(num):
    return int(num, 2)

def bin_to_oct(num):
    dec_num = bin_to_dec(num)
    return oct(dec_num).lstrip("0o")

def bin_to_hex(num):
    dec_num = bin_to_dec(num)
    return hex(dec_num).lstrip("0x")

def dec_to_bin(num):
    return bin(num).lstrip("0b")

def dec_to_oct(num):
    return oct(num).lstrip("0o")

def dec_to_hex(num):
    return hex(num).lstrip("0x")

def oct_to_bin(num):
    dec_num = int(num, 8)
    return bin(dec_num).lstrip("0b")

def oct_to_dec(num):
    return int(num, 8)

def oct_to_hex(num):
    dec_num = oct_to_dec(num)
    return hex(dec_num).lstrip("0x")

def hex_to_bin(num):
    dec_num = int(num, 16)
    return bin(dec_num).lstrip("0b")

def hex_to_dec(num):
    return int(num, 16)

def hex_to_oct(num):
    dec_num = hex_to_dec(num)
    return oct(dec_num).lstrip("0o")

def convert_number():
    print("Escolha a base de origem:")
    print("1. Binário")
    print("2. Octal")
    print("3. Decimal")
    print("4. Hexadecimal")
    origem = int(input("Digite o número correspondente à base de origem: "))

    print("Escolha a base de destino:")
    print("1. Binário")
    print("2. Octal")
    print("3. Decimal")
    print("4. Hexadecimal")
    destino = int(input("Digite o número correspondente à base de destino: "))

    num = input("Digite o número a ser convertido: ")

    if origem == 1:
        if destino == 1:
            print(f"Resultado: {num}")
        elif destino == 2:
            print(f"Resultado: {bin_to_oct(num)}")
        elif destino == 3:
            print(f"Resultado: {bin_to_dec(num)}")
        elif destino == 4:
            print(f"Resultado: {bin_to_hex(num)}")
    elif origem == 2:
        if destino == 1:
            print(f"Resultado: {oct_to_bin(num)}")
        elif destino == 2:
            print(f"Resultado: {num}")
        elif destino == 3:
            print(f"Resultado: {oct_to_dec(num)}")
        elif destino == 4:
            print(f"Resultado: {oct_to_hex(num)}")
    elif origem == 3:
        if destino == 1:
            print(f"Resultado: {dec_to_bin(num)}")
        elif destino == 2:
            print(f"Resultado: {dec_to_oct(num)}")
        elif destino == 3:
            print(f"Resultado: {num}")
        elif destino == 4:
            print(f"Resultado: {dec_to_hex(num)}")
    elif origem == 4:
        if destino == 1:
            print(f"Resultado: {hex_to_bin(num)}")
        elif destino == 2:
            print(f"Resultado: {hex_to_oct(num)}")
        elif destino == 3:
            print(f"Resultado: {hex_to_dec(num)}")
        elif destino == 4:
            print(f"Resultado: {num}")
    else:
        print("Opção inválida!")

convert_number()