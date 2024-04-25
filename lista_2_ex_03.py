def hex_to_decimal(hex_number):
    try:
        decimal_number = int(hex_number, 16)
        return decimal_number
    except ValueError:
        return None

hex_number = input("Digite um número em hexadecimal: ")
decimal_number = hex_to_decimal(hex_number)

if decimal_number is not None:
    print(f"O número decimal equivalente é: {decimal_number}")
else:
    print("Número hexadecimal inválido.")