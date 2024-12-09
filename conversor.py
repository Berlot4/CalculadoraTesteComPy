
while True:
    print('O que você gostaria de fazer?')
    objetivo = input('[C]onverter ou [S]air: ')
    objetivo = objetivo.upper()

    if objetivo == 'C':
        tipo_finalizador = input('Você quer converter para? [D]ecimal, [H]exadecimal, [B]inario ou [O]ctadecimal? ')
        tipo_finalizador = tipo_finalizador.upper()
        if tipo_finalizador == 'D':
            tipo_inicial = input('Seu numero inicial é [H]exadecimal [O]ctal ou [B]inario? ')
            tipo_inicial = tipo_inicial.upper()
            if tipo_inicial == 'B':
                binario = input('Digite um número bínario: ')
                try:
                        decimal = int(binario, 2)
                        print('Resultado = ', decimal)
                except:
                      print('Por favor digite apenas números.')
                      continue
            elif tipo_inicial == 'H':
                    hexadecimal = input('Digite um número Hexadecimal: ')
                    decimal = int(hexadecimal, 16)
                    print('Resultado = ', decimal)
            elif tipo_inicial == 'O':
                    octal = input('Digite um número Octal: ')
                    decimal = int(octal, 8)
                    print('Resultado = ', decimal)
            else:
                print('Por favor digite um tipo válido.')
                continue
        elif tipo_finalizador == 'H':
            tipo_inicial = input('Seu numero inicial é [D]ecimal [O]ctal ou [B]inario? ')
            tipo_inicial = tipo_inicial.upper()
            if tipo_inicial == 'B':
                    binario = input('Digite um número bínario: ')
                    decimal = int(binario, 2)
                    hexadecimal = hex(decimal)
                    print('Resultado = ', hexadecimal[2:])
            elif tipo_inicial == 'D':
                    decimal = input('Digite um número Decimal: ')
                    hexadecimal = hex(int(decimal))
                    print('Resultado = ', hexadecimal[2:])
            elif tipo_inicial == 'O':
                    octal = input('Digite um número Octal: ')
                    decimal = int(octal, 8)
                    hexadecimal = hex(decimal)
                    print('Resultado = ', hexadecimal[2:])
            else:
                print('Por favor digite um tipo válido.')
                continue
        elif tipo_finalizador == 'B':
            tipo_inicial = input('Seu numero inicial é [H]exadecimal [O]ctal ou [D]ecimal? ')
            tipo_inicial = tipo_inicial.upper()
            if tipo_inicial == 'D':
                    decimal = input('Digite um número decimal: ')
                    binario = bin(int(decimal))
                    print('Resultado = ', binario[2:])
            elif tipo_inicial == 'H':
                    hexadecimal = input('Digite um número Hexadecimal: ')
                    decimal = int(hexadecimal, 16)
                    binario = bin(decimal)
                    print('Resultado = ', binario[2:])
            elif tipo_inicial == 'O':
                    octal = input('Digite um número Octal: ')
                    binario = bin(int(octal, 8))
                    print('Resultado = ', binario[2:])
            else:
                print('Por favor digite um tipo válido.')
                continue
        elif tipo_finalizador == 'O':
            tipo_inicial = input('Seu numero inicial é [H]exadecimal [B]inario ou [D]ecimal? ')
            tipo_inicial = tipo_inicial.upper()
            if tipo_inicial == 'D':
                    decimal = input('Digite um número decimal: ')
                    octadecimal = oct(int(decimal))
                    print('Resultado = ', octadecimal[2:])
            elif tipo_inicial == 'H':
                    hexadecimal = input('Digite um número Hexadecimal: ')
                    decimal = int(hexadecimal, 16)
                    octadecimal = oct(decimal)
                    print('Resultado = ', octadecimal[2:])
            elif tipo_inicial == 'B':
                    binario = input('Digite um número Binario: ')
                    binario = oct(int(binario, 2))
                    print('Resultado = ', binario[2:])
            else:
                print('Por favor digite um tipo válido.')
                continue
        else:
            print('Por favor digite um tipo valido')
            continue

    elif objetivo == 'S':
        break
    else:
        print('Digite uma alternativa válida.')