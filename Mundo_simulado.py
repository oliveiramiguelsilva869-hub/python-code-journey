class Estabelecimento:
    def __init__(self, nome_lugar, tipo_lugar, custo_ou_salario):
        self.nome = nome_lugar
        self.tipo = tipo_lugar
        self.valor = custo_ou_salario

class Personagem:
    def __init__(self, nome_inicial):
        self.nome = nome_inicial
        self.dinheiro = 100
        self.energia = 100
        self.fome = 0

    def exibir_status(self):
        print(f'\n--- STATUS DE {self.nome} ---')
        print(f'CARTEIRA: R${self.dinheiro}')
        print(f'ENERGIA: {self.energia}%')
        print(f'FOME: {self.fome}%')

    def ir_trabalhar(self, local_de_trabalho):
        if local_de_trabalho.tipo == 'Trabalho':
            if self.energia >= 30:
                print(f'{self.nome} foi tralhar no(a) {local_de_trabalho.nome}!')
                self.energia -= 30
                self.fome += 30
                self.dinheiro += local_de_trabalho.valor
            else:
                print(f'{self.nome} está sem energia para trabalhar.')
        else:
            print(f'{local_de_trabalho.nome} não é um local de trabalho!')

    def ir_comer(self, restaurante):
        if restaurante.tipo == 'Restaurante':
            if self.dinheiro >= restaurante.valor:
                print(f'{self.nome} comeu no(a) {restaurante.nome} e pagou R${restaurante.valor}.')
                self.dinheiro -= restaurante.valor
                self.fome = 0
                self.energia += 20
                if self.energia > 100: self.energia = 100
            else:
                    print(f'{self.nome} não tem dinheiro suficiente para comer no(a) {restaurante.nome}!')
        else:
                print(f'{restaurante.nome} não vende comida!')

hospital = Estabelecimento('Hospital Central', 'Trabalho', 1500)
lanchonete = Estabelecimento('Burguer Shot', 'Restaurante', 40)
restaurante_chique = Estabelecimento('Le Paris', 'Restaurante', 120)
oficina = Estabelecimento('Oficina do Tião', 'Trabalho', 300)

sim1 = Personagem('Andrey')

sim1.exibir_status()

sim1.ir_comer(restaurante_chique)

sim1.ir_trabalhar(oficina)
sim1.exibir_status()

sim1.ir_comer(lanchonete)
sim1.exibir_status()
