# 1 - Defina as variáveis

estado1 = input("Insira um estado: ")
estado2 = input("Insira outro estado: ")
estado3 = input("Insira o último estado: ")
pais = input("Qual o país?")

estadosDoBrasil = ['Acre', 'Alagoas', 'Amapa', 'Amazonas', 
                   'Bahia', 'Ceara', 'Distrito Federal',
                   'Espirito Santo','Goias', 'Maranhao',
                   'Mato Grosso', 'Mato Grosso do Sul',
                   'Minas Gerais', 'Para', 'Paraiba',
                   'Parana', 'Pernambuco', 'Piaui',
                   'Rio de Janeiro', 'Rio Grande do Norte', 'Rio Grande do Sul',
                   'Rondonia', 'Roraima', 'Santa Catarina',
                   'Sao Paulo' 'Sergipe', 'Tocantins']

 

def local(estado1, estado2, estado3, pais = 'Brasil'):
     if estado1 in estadosDoBrasil:
           print (f'{estado1} pertence ao país {pais}')
     else:
           print (f'{estado1} não pertence ao país {pais}')
           
     if estado2 in estadosDoBrasil:
           print (f"{estado2} pertence ao país {pais}")
     else:
           print (f'{estado2} não pertence ao país {pais}')
           
     if estado3 in estadosDoBrasil:
           print (f"{estado3} pertence ao país {pais}")         
     else:
           print (f'{estado3} não pertence ao país {pais}')
      



local(estado1, estado2, estado3, pais='Brasil')
