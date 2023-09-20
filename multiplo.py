#teste de multiplo de 5

#1 - Insira um número
x = int(input ("Digite um número inteiro:") )

#2- Verificar se o resto da divisão é 0 utilizando "%" para analizar
resultado = x % 5

#3- Se teste for verdadeiro:
if resultado == 0:
    print("Múltiplo de 5")

#4- Se não:
else:
    print("Não é multiplo")
