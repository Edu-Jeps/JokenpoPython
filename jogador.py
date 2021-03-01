# José Eduardo da Silva  

import random
escolha = [0, 1, 2]

#classe jogador
class Jogador():
    #recebe o nome e o numero de jogadas
    def __init__(self, nome):
        self.nome = nome
        self.contJogador = 0

    def get_opcao(self):
        return self.opcao_atual if self.opcao_atual else random.choice(escolha)

    #verifica se a escolha é valida
    def escolher(self, opcao):
        valido = opcao in escolha
        self.opcao_atual = opcao
        return valido