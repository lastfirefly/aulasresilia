def previsaoRodagem():
    
    qntGasol = float(input("Quantos litros de gasolina possui no tanque?"))
    qualCarro = input("Qual o modelo do carro?")
    
      
    if qualCarro == "Opala":
        print("Troca de carro")
    
    
    kmL = float(input("Qual km/L média do modelo?"))
    estimativaKM = qntGasol*kmL
     
    return print(estimativaKM, "km")
    
    
if __name__ == '__main__':
    previsaoRodagem()   
    
