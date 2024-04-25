def is_valid_octal(number):
    for digit in number:
        if digit not in '01234567':
            return False
    return True

def octal_to_decimal(number):
    decimal = 0
    power = 0
    for digit in reversed(number):
        decimal += int(digit) * (8 ** power)
        power += 1
    return decimal

octal_number = input("Digite um número em octal: ")

if is_valid_octal(octal_number):
    decimal_number = octal_to_decimal(octal_number)
    print("O número em decimal é:", decimal_number)
else:
    print("Número inválido. Certifique-se de digitar um número em octal válido.")