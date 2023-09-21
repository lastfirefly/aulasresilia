import os
from datetime import datetime



# ********************************************************* Primeiro Menu ***************************************************************


# 2a - Primeira opção do primeiro menu

def marcarConsulta(nome):
    print(
        f'\n{nome}, que tipo de médico você gostaria de marcar? \n[1] - Tomografia \n[2] - Ultrasonografia \n[3] - Hemograma \n[0] - Voltar para o menu inicial\n [*] - Sair \n')
    
# if 


# 2b - Segunda opção do primeiro bloco 

#def desmarcConsulta(nome):
#    print


# 2c - Terceira opção do primeiro menu

#def falarComAtendente(nome):


# ********************************************************* Menu iniciar *************************************************************

# 1b - Primeiro bloco de respostas e tratamentos para os dados

def processarResposta(respostaMenu, nome):
    
    # Verificar a resposta, se for 1, encaminhar para marcação de consulta
    if respostaMenu == "1":
        return marcarConsulta(nome)
    # Verificar a resposta, se for 2, encaminhar para desmarcação de consulta
    elif respostaMenu == "2":
        respostaMenu = desmarcConsulta
        print(
            f'\n{nome}, insira o dia e horário da consulta que você gostaria de desmarcar: \n')

    # Verificar a resposta, se for 3, encaminhar para 
    elif respostaMenu == "3":
        respostaMenu = falarComAtendente
        print(
            f'\n{nome}, estou te transferindo para um de nossos colaboradores \n')

    # Verificar a resposta, se não for compatível, retornar pedido de resposta certa 
    else:
        print('Digite apenas as opções 1, 2 ou 3') 


# 1a - Estrutura aparência inicial

def start():
    #apresentar o chatbox
    print("Olá! Bem vindo Connect Health \nMeu nome é Connie, sou a assistente digital que vai te auxiliar hoje")

    #pedir nome
    nome = input("Digite seu nome completo: ")


    #oferecer um menu de opções
    respostaMenu = input(
        f'O que você gostaria de fazer hoje? \n[1] - Marcar consulta \n[2] - Cancelar consulta \n[3] - Como chegar? \n[4] - Falar com atendente \n ')
#    respostaMenu = True
    
    #processar a resposta enviada chamando a função
    processarResposta(respostaMenu, nome)


#************************************************* Bora rodar? ********************************************

if __name__ == '__main__':
    start()
    
