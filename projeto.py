import os


# ********************************************************* Primeiro Menu ***************************************************************


# 2a - Primeira opção do primeiro menu

def marcarExame(nome):
    marcarExame = input(f'\n{nome}, que tipo de médico você gostaria de marcar? \n[1] - Tomografia \n[2] - Ultrasonografia \n[3] - Hemograma \n[*] - Sair \n')

    if marcarExame == "1":
        print("Para marcar uma Tomografia, você precisará ter em mãos um documento de identificação com foto e a carteirinha do plano em caso de marcação por convênio. \n \n O preparo varia de acordo com a região a ser examinada. Quando é necessário o uso de contraste, o paciente deve ficar de jejum por até 8 horas. Para a tomografia realizada, principalmente na área digestiva, pode ser indicado o uso de laxantes ou enema para limpar o intestino. \nPara marcar o exame, retorne ao menu e vá em 'contatos'" )

    if marcarExame == "2":
        print("Para marcar uma Tomografia, você precisará ter em mãos um documento de identificação com foto e a carteirinha do plano em caso de marcação por convênio. \n \nFazer jejum absoluto de no mínimo 8h no dia do exame, sendo a última refeição leve; \nNão fumar antes do exame.\nPode tomar água até duas horas antes do exame; \nSE VOCÊ TEM ATÉ 12 ANOS OU, PELO MENOS, 65 ANOS, três horas antes do seu exame não coma mais nada (jejum). Pode tomar água até duas horas antes do exame; \nSE VOCÊ TEM DIABETES, NÃO IMPORTA QUANTOS ANOS VOCÊ TEM, três horas antes do seu exame não coma mais nada (jejum).")

    if marcarExame == "3":
        print("Para agendar um Hemograma, você precisará ter em mãos um documento de identificação com foto e a carteirinha do plano em caso de marcação por convênio. \n \n Os pré-requisitos para fazer hemograma são: não ingerir bebidas alcoólicas 72 horas antes do exame, evitar exercícios físicos na véspera e caso siga uma leve dieta um dia antes do exame, não é necessário fazer jejum. \nPorém, caso contrário, recomenda-se um jejum de 3 horas. \nÉ preciso informar se faz o uso de medicamentos contínuos, pois alguns deles podem interferir no exame. O objetivo aqui é evitar a desidratação.")

    if marcarExame == "*":
        print("\nAgradecemos o seu contato! Qualquer dúvida, estarei disponível para ajudar!")

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
        return marcarExame(nome)
    # Verificar a resposta, se for 2, encaminhar para desmarcação de consulta
    elif respostaMenu == "2":
    #  respostaMenu = desmarcConsulta
        print(
            f'\n{nome}, insira o dia e horário da consulta que você gostaria de desmarcar: \n')

    # Verificar a resposta, se for 3, encaminhar para 
    elif respostaMenu == "3":
        #  respostaMenu = falarComAtendente
        print(f'\n{nome}, o consultorio se localiza na Rua A, 1 - Bairro, Cidade') 

    elif respostaMenu == "4":
        print(f'\n{nome}, estou te transferindo para um de nossos colaboradores \n')

    # Verificar a resposta, se não for compatível, retornar pedido de resposta certa 
    else:
        print('Digite apenas as opções 1, 2, 3 ou 4') 


# 1a - Estrutura aparência inicial

def start():
    #apresentar o chatbox
    print("\nOlá! \nBem vindo ao Connect Health \nMeu nome é Connie, sou a assistente digital do ConnectHealth que vai tirar suas dúvidas hoje\n")

    #pedir nome
    nome = input("Digite seu nome completo: ")


    #Pedir para repetir para que o menu entre em loop
    while True:
        #oferecer um menu de opções
        respostaMenu = input(f'\nO que você gostaria de fazer hoje? \n[1] - Marcar consulta \n[2] - Cancelar consulta \n[3] - Como chegar? \n[4] - Falar com atendente \n ')

        #processar a resposta enviada chamando a função
        processarResposta(respostaMenu, nome)


#************************************************* Bora rodar? ********************************************

if __name__ == '__main__':
    start()
