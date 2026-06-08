nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

if idade >= 18:
    autorizado = True
else:
    autorizado = False

print("\n--- Resultado da análise ---")
if autorizado:
    print(f"Acesso PERMITIDO para {nome}. Aproveite o sistema!")
else:
    print("Acesso NEGADO, {}. Menores de 18 anos não podem entrar.".format(nome))
