import random
from time import sleep
from os import system

def exibir_escolha():
    print(f'Escolha do Player: {escolha_player.capitalize()}.')
    print(f'Escolha do Máquina: {escolha_maquina.capitalize()}.')


def exibir_pontuacao():
    print(f'Pontuação Player = {pontuacao_player}\nPontuação Máquina = {pontuacao_maquina}')
    print('-' * 50)

OPCOES = ('pedra', 'papel', 'tesoura')
escolha_valida = False
pontuacao_player = 0
pontuacao_maquina = 0
finalizar_partida = False
PONTUACAO_MAXIMA = 5

while finalizar_partida == False:
    escolha_maquina = random.choices(OPCOES)[0]
    escolha_player = input('Escolha entre, "Pedra", "Papel" e "Tesoura": ').lower()
    
    while escolha_valida == False:
        if escolha_player not in OPCOES:
            print('Escolha inválida.')
            sleep(1)
            break
        else:
            escolha_valida = True
            system('cls')
            exibir_escolha()
            
            
            # Possiblidades de vitória
            if escolha_player == 'pedra' and escolha_maquina == 'tesoura':
                print('O Player venceu a partida!')
                pontuacao_player +=1
            elif escolha_player == 'papel' and escolha_maquina == 'pedra':
                print('O Player venceu a partida!')
                pontuacao_player +=1
            elif escolha_player == 'tesoura' and escolha_maquina == 'papel':
                print('O Player venceu a partida!')
                pontuacao_player +=1
                
                
            # Possibilidades de derrota
            if escolha_maquina == 'pedra' and escolha_player == 'tesoura':
                print('A máquina venceu a partida!')
                pontuacao_maquina += 1
            elif escolha_maquina == 'papel' and escolha_player == 'pedra':
                print('A máquina venceu a partida!')
                pontuacao_maquina += 1
            elif escolha_maquina == 'tesoura' and escolha_player == 'papel':
                print('A máquina venceu a partida!')
                pontuacao_maquina += 1
                
                
            # Empate
            if escolha_player == escolha_maquina:
                print('Empatou!')
                
            
            if pontuacao_player == PONTUACAO_MAXIMA:
                exibir_pontuacao()
                print('Pontuação máxima atingida, o Player venceu!')
                break
            elif pontuacao_maquina == PONTUACAO_MAXIMA:
                exibir_pontuacao()
                print('Pontuação máxima atingida, a Máquina venceu!')
                break

            exibir_pontuacao()
    escolha_valida = False

