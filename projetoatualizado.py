import os


# ********************************************************* Primeiro Menu ***************************************************************


# 2a - Primeira opção do primeiro menu

def marcarExame(nome):
    marcarExame = input(f'\n{nome}, que tipo de médico você gostaria de marcar? \n[1] - Tomografia \n[2] - Ultrasonografia \n[3] - Hemograma \n[*] - Sair \n')

    if marcarExame == "1":
        print(f"{nome}, para marcar uma Tomografia, você precisará ter em mãos um documento de identificação com foto e a carteirinha do plano em caso de marcação por convênio. \n \n O preparo varia de acordo com a região a ser examinada. Quando é necessário o uso de contraste, o paciente deve ficar de jejum por até 8 horas. Para a tomografia realizada, principalmente na área digestiva, pode ser indicado o uso de laxantes ou enema para limpar o intestino. \nPara marcar o exame, retorne ao menu e vá em 'contatos'" )

    elif marcarExame == "2":
        print(f"{nome}, para marcar uma Tomografia, você precisará ter em mãos um documento de identificação com foto e a carteirinha do plano em caso de marcação por convênio. \n \nFazer jejum absoluto de no mínimo 8h no dia do exame, sendo a última refeição leve; \nNão fumar antes do exame.\nPode tomar água até duas horas antes do exame; \nSE VOCÊ TEM ATÉ 12 ANOS OU, PELO MENOS, 65 ANOS, três horas antes do seu exame não coma mais nada (jejum). Pode tomar água até duas horas antes do exame; \nSE VOCÊ TEM DIABETES, NÃO IMPORTA QUANTOS ANOS VOCÊ TEM, três horas antes do seu exame não coma mais nada (jejum).")

    elif marcarExame == "3":
        print(f"{nome}, para agendar um Hemograma, você precisará ter em mãos um documento de identificação com foto e a carteirinha do plano em caso de marcação por convênio. \n \n Os pré-requisitos para fazer hemograma são: não ingerir bebidas alcoólicas 72 horas antes do exame, evitar exercícios físicos na véspera e caso siga uma leve dieta um dia antes do exame, não é necessário fazer jejum. \nPorém, caso contrário, recomenda-se um jejum de 3 horas. \nÉ preciso informar se faz o uso de medicamentos contínuos, pois alguns deles podem interferir no exame. O objetivo aqui é evitar a desidratação.")




# 2b - Segunda opção do primeiro bloco 

def desmarcExame(nome):
    print("\nA desmarcação tem que ser feita presencialmente ou através de um dos meios de contato oficial.")
    desmarcExame = input(f'\nO que gostaria de fazer?\n[1] - Como chegar?\n[2] - Contatos \n[3] - Voltar para o menu inicial \n[*] - Sair')
    #Se opção 1, encaminhar para função comoChegar 
    if desmarcExame == "1":
        return comoChegar(nome)
    elif desmarcExame == "2":
        return contatos(nome)
    elif desmarcExame == "3":
        print("")



# 2c - Terceira opção do primeiro menu

def comoChegar(nome):
    comoChegar = input(f'\n{nome}, o consultorio principal localiza-se na Rua A, 1 - Bairro, Cidade')

def contatos(nome):
    contatos = input(f'\n{nome}, toma o endereço aí')



# ********************************************************* Menu iniciar *************************************************************

# 1b - Primeiro bloco de respostas e tratamentos para os dados

def processarResposta(respostaMenu, nome):
    
    # Verificar a resposta, se for 1, encaminhar para marcação de exame
    if respostaMenu == "1":
        return marcarExame(nome)
    # Verificar a resposta, se for 2, encaminhar para desmarcação de exame
    elif respostaMenu == "2":
    #  respostaMenu = desmarcExame
        return desmarcExame(nome)
    # Verificar a resposta, se for 3, encaminhar para 
    elif respostaMenu == "3":
        return comoChegar(nome)

    elif respostaMenu == "4":
        return contatos(nome)

    # Verificar a resposta, se não for compatível, retornar pedido de resposta certa 
    else:
        print('Digite apenas as opções 1, 2, 3 ou 4') 


# 1a - Estrutura aparência inicial

def start():
    #apresentar o chatbox
    print("\nOlá! \nBem vindo ao Connect Health \nMeu nome é Connie, sou a assistente digital do ConnectHealth que vai tirar suas dúvidas hoje\n")

    #pedir nome
    nome = input("Digite seu nome: ")


    #Pedir para repetir para que o menu entre em loop
    while True:
        #oferecer um menu de opções
        respostaMenu = input(f'\nO que você gostaria de saber hoje, {nome}? \n[1] - Como faço para marcar exame? \n[2] - Como cancelar exame? \n[3] - Como chegar? \n[4] - Contatos \n ')
        #processar a resposta enviada chamando a função
        processarResposta(respostaMenu, nome)
        
        if marcarExame == "*" or desmarcExame == "*" or comoChegar == "*" or contatos == "*":
            print(f"\nAgradecemos o seu contato, {nome}! Qualquer dúvida, estarei disponível para te ajudar!")
            break
        else:
            continue




#************************************************* Bora rodar? *******************************************************

if __name__ == '__main__':
    start()
    
    
# # ********************************* Chat GPT sugestão ****************************************
# def processarResposta(respostaMenu, nome):
#     if respostaMenu == "1":
#         return marcarExame(nome)
#     elif respostaMenu == "2":
#         return desmarcExame(nome)
#     elif respostaMenu == "3":
#         return comoChegar(nome)
#     elif respostaMenu == "4":
#         return contatos(nome)
#     elif respostaMenu == "*":
#         print(f"Agradecemos o seu contato, {nome}! Qualquer dúvida, estarei disponível para te ajudar!")
#         return True  # Sair do loop
#     else:
#         print('Digite apenas as opções 1, 2, 3, 4 ou *')
#     return False
