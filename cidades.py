#➔ O QUE FAZER?
#Escreva uma função que aceite o nome de uma cidade e seu país.
#➔ COMO FAZER?
#1. A função deve exibir uma frase simples, como Brasília está localizada no país Brasil.
#2. Forneça um valor default ao parâmetro que representa o país.
#3. Chame sua função para três cidades diferentes em que pelo menos uma delas não esteja
#no país default.
#4. A intenção é que testem os diferentes tipos de argumentos e parâmetros que vimos ainda
#há pouco.
#➔ FECHAMENTO
#Compartilhar os resultados e as maiores dificuldades com a turma.



cidade1 = input("Onde você está? ")
cidade2 = input("Pra onde você quer ir?")
cidade3 = input("Primeira parada: ")
                
def localizacao(cidade1, cidade2, cidade3, pais = "Brasil"):
    print ("Você está saindo de", cidade1, "Você está indo para", cidade3, "e seu sonho é passar por", cidade2)

localizacao(cidade1, cidade2, cidade3)

a=4
