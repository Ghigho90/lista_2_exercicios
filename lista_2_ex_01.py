def binario_para_decimal(binario):
    # Verifica se o número binário é válido
    for digito in binario:
        if digito != '0' and digito != '1':
            return None
    
    # Converte o número binário para decimal
    decimal = 0
    potencia = len(binario) - 1
    for digito in binario:
        decimal += int(digito) * (2 ** potencia)
        potencia -= 1
    
    return decimal

# Captura o número binário do usuário
binario = input("Digite um número binário: ")

# Converte e imprime o número na notação decimal
decimal = binario_para_decimal(binario)
if decimal is not None:
    print("O número em decimal é:", decimal)
else:
    print("Número inválido!")