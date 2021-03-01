# José Eduardo da Silva  


from jogador import Jogador
from game import Jogo


def main():
    print("-"*50)
    nome = input("Olá, digite o seu nome: ")

    #cria o objeto jogador e game
    jogador = Jogador(nome)
    game = Jogo(jogador)

    #laço de repetição onde verifica se o jogador deseja continuar
    while True:
        #cria o menu
        print('-'*50)
        print(' '*15, jogador.nome,' xXx  CPU')
        print('-' * 50)
        #recebe a escolha do jogador
        opcao = int(input("\nDigite um número para iniciar o jogo, sendo:\n0 = Pedra\n1 = Papel\n2 = Tesoura\n"))
        if not jogador.escolher(opcao):
            print("Opção inválida, digite novamente")
            continue

        #chama o metodo onde ira iniciar o jogo
        game.iniciar()
        continuar = input("\nDeseja continuar jogando? 1: Sair, 2: Continuar\n")

        if continuar != "2":
            print("Fim de jogo")
            break


if __name__ == "__main__":
    main()