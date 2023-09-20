#Escreva um programa em Python que some diversos números fornecidos pelo usuário. 
# A quantidade de números que serão somados, também deve ser fornecida pelo usuário.


#Crie as variáveis de número e soma;
#Realize o cálculo necessário;
#Imprima a informação para o usuário.


# 1- Crie uma variável para receber a quantidade de números que serão somados a ser fornecida pelo usuário

quantidadeValores = int(input("Quantos números vamos calcular? "))

  
contagem = 1

a = int(input("Insira primeiro valor: "))
b = int(input("Insira segundo valor: "))

resultado = a + b


#cont = 


#for i in range(0,quantidadeValores,1):
# print (contagem)
# contagem = contagem + 1 



while contagem < quantidadeValores:
        if quantidadeValores >= 2:
           print("Insira valor: ")
        else:
            print(a,b)

   
        
                   
print(resultado)


