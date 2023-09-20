#1- Solicitar informações

a = int(input("Quantas polegadas tem a tv? ")) # mínimo 32 polegadas
b = int(input("Qual o valor da tv? "))  #máximo R$1900,00



#2- Testar condições

if a >= 32:
       print("Tamanho aceito.")
       if b <= 1900:
             print("Valor aceito. >Pode Comprar<")      
else:
         print("Testa outra")
