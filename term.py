a = 36.5
b = 38
c = 39

temperatura = float(input("Insira a temperatura: "))


if temperatura < a:
    print("Hipotermia")
elif temperatura >= b:
    print("Você está com febre")
else:
    print("Nada de febre")
