#Um lojista comprou diversos produtos para sua loja e deseja revendê-lo 
#com margem de lucro diferente dependendo do valor; por exemplo, 
#ele deseja obter lucro de 45% caso o produto custe menos que R$ 20,00. 
#Porém, caso o produto custe mais que isso, o lucro deve ser de 30%.
# Escreva um programa em Python que ajude esse lojista.

#1- insira valores para produtos

x = int(input("Insira o valor do produto: "))

#2- Mostrar valores a serem cobrados respeitando as regras de lucro

a = (x * 0.45) + x
b = (x * 0.30) + x

if x <= 20 :
    print("Lucro de 45%.", "\nValor a ser cobrado: ",a)
else :
    print("Lucro de 30%.", "\nValor a ser cobrado: ",b)
    
