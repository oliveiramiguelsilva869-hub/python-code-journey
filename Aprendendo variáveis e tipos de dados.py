##nome_jogo = str('SiTA')
##nivel = int(5)
##vida_personagem = int(100)
##velocidade = float(14.5)
##esta_vivo = True

nome_jogador = input(str('Insira o seu nome: '))
xp_atual = 1555
multiplicador_danos = 1.78
boss_derrotado = False
print("--- DADOS DO JOGADOR ---")
print("Nome:", nome_jogador)
print("XP:", xp_atual)
print("Multiplicador de danos", multiplicador_danos)
print("Já derrotou o  Boss?:", boss_derrotado)

print("\n--- TIPOS DETECTADOS PELO PYTHON ---")
print(type(nome_jogador))
print(type(xp_atual))
print(type(multiplicador_danos))
print(type(boss_derrotado))
