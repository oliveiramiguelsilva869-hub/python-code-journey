print("\n--- Info. Cars ---")
marca = input('Qual a marca do seu veiculo?: ')
modelo = input('Qual o modelo?: ')
ano = int(input('Qual o ano?: '))
top_speed = float(input('Qual a velocidade máxima?: '))

print('\n--- DADOS DO VEICULO ---')
print(f'Marca: {marca}')
print(f'Modelo: {modelo}')
print(f'Ano: {ano}')
print(f'Top speed alcançado: {top_speed}')

if top_speed >= 150:
    print('Bem vindo ao First2')
else :
    print('Não foi possível fazer o seu registro.')
