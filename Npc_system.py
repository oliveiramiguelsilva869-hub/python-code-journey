class Personagem:
    def __init__(self, nome_inicial, profissao_inicial):
        self.nome = nome_inicial
        self.profissao = profissao_inicial
        self.energia = 100
        self.fome = 0

    def exibir_status(self):
        print(f'\n--- Status de {self.nome} ---')
        print(f'Profissão: {self.profissao}')
        print(f'Energia: {self.energia}%')
        print(f'Fome: {self.fome}%')

    def trabalhar(self):
        if self.energia >= 30:
            print(f'💼 {self.nome} está trabalhando como {self.profissao}...')
            self.energia -= 30
            self.fome += 20
        else:
            print(f'❌ {self.nome} está cansado demais para trabalhar! Precisa dormir.')
    def comer(self):
        if self.fome >= 15:
            print(f'{self.nome} está comendo!')
            self.energia += 15
            self.fome -= 20
            if self.fome < 0:
                self.fome = 0
        else:
            print(f'{self.nome} não está com fome.')

    def dormir(self):
        print(f'💤 {self.nome} foi dormir e recuperou a energia!')
        self.energia = 100
        self.fome -= 10
        if self.fome < 0:
            self.fome = 0

sim1 = Personagem('Carlos','Médico')
sim2 = Personagem('Amanda', 'Piloto de Fuga')

sim1.exibir_status()
sim1.trabalhar()
sim1.trabalhar()
sim1.comer()
sim1.exibir_status()

sim1.trabalhar()
sim1.comer()
sim1.dormir()
sim1.exibir_status()

#sim2.exibir_status()
