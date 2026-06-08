print('\n--- Rating your Car ---')
continuar = True
while continuar:
    marca = input('Insira a marca do seu veiculo: ')
    modelo = input('Qual o modelo: ')
    ano = int(input('A qual ano ele pertence?: '))
    top_speed = float(input('Qual o top speed máximo alcançado?:'))

    print('\n--- Dados informados ---')
    print(f'Marca: {marca}')
    print(f'Modelo: {modelo}')
    print(f'Ano: {ano}')
    print(f'Top speed máximo: {top_speed}')

    if top_speed < 125:
        print('Classe B')
    elif top_speed >= 125 and top_speed <= 200:
        print('Classe A')
    else:
        print('Classe S')
    resposta = input('Deseja classificar outro carro? (V/X): ').upper()
    if resposta == 'X':
        continuar = False
        print('\n---Programa encerrado.---')
