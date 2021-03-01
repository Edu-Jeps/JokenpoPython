# José Eduardo da Silva 

from jogador import Jogador
import random

# 0 = pedra / 1 = papel / tesoura = 2
escolha = [0, 1, 2]


class Jogo:
    #recebe o jogador como objeto
    def __init__(self, jogador):
        self.jogador = jogador
        self.contJogos = 0
        self.contCpu = 0

    def iniciar(self):
        #recebe a opcao no rendom para o cpu
        cpu = random.choice(escolha)
        print('o cpu escolheu', cpu)

        #verifica quem ganhou, com uma estrutura de condição
        #caso o jogador escolheu 0 (Pedra)
        if self.jogador.get_opcao() == 0:
            if cpu == 0:
                print("\nCPU -> Pedra\nEmpate!\n")
            elif cpu == 1:
                print("\nCPU -> Pedra\nVocê venceu!\n")
                self.jogador.contJogador += 1
            elif cpu == 2:
                print("\nCPU -> Pedra\nVocê perdeu!\n")
                self.contCpu += 1

        # caso o jogador escolheu 1 (Papel)
        elif self.jogador.get_opcao() == 1:
            if cpu == 0:
                print(f"\nCPU -> Papel\nVocê perdeu!\n")
                self.contCpu += 1
            elif cpu == 1:
                print(f"\nCPU -> Papel\nEmpate!\n")
            elif cpu == 2:
                print(f"\nCPU -> Papel\nVocê venceu!\n")
                self.jogador.contJogador += 1

        # caso o jogador escolheu 2 (Tesoura)
        elif self.jogador.get_opcao() == 2:
            if cpu == 0:
                print(f"\nCPU -> Tesoura\nVocê ganhou!\n")
                self.jogador.contJogador += 1
            elif cpu == 1:
                print(f"\nCPU -> Tesoura\nVocê perdeu!\n")
                self.contCpu += 1
            elif cpu == 2:
                print(f"\nCPU -> Tesoura\nEmpate!\n")

        #conta as jogadas
        self.contJogos += 1
        #imprime o resultado
        print(
            f"\nResultado:\nNúmero de jogos: {self.contJogos}\n{self.jogador.nome}: {self.jogador.contJogador}\nCPU: {self.contCpu}")