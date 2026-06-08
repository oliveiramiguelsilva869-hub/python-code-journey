def classificar_veiculo(velocidade):
    if velocidade < 125:
        return 'CLASSE B'
    elif velocidade >= 125 and velocidade <= 200:
        return 'CLASSE A'
    else:
        return 'CLASSE S'
continuar = True
while continuar:
    print('\n--- Rating your Car ---')
    marca = input('Qual a marca do seu veiculo?: ').upper()
    modelo = input('Qual o modelo?: ').upper()
    ano = int(input('Qual ano ele pertence?[0000]: '))
    top_speed = float(input('Qual o Top speed máximo alcançado?: '))

    print('\n--- DADOS INFORMADOS ---')
    print(f'MARCA: {marca}')
    print(f'MODELO: {modelo}')
    print(f'ANO: {ano}')
    print(f'TOP SPEED: {top_speed}')
    print(f'CLASSE: {classificar_veiculo(top_speed)}')

    resposta = input('Deseja classificar outro carro?(V/X): ').upper()
    print('. . .')
    if resposta == 'X':
        continuar = False
        print('\n--- PROGRAMA ENCERRADO ---')
