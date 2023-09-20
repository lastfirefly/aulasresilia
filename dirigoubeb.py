def dirigirOuBeber():
    
    idade = input("Qual sua idade?")
   
    if idade >= "18":
         print("Já pode dirigir ou beber")
    else:
         print("Não pode nem dirigir nem beber")


if __name__ == '__main__':
    dirigirOuBeber()
