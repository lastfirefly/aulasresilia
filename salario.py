# 1- Definir Valores Iniciais
salarioFuncionario = 1250
percentualReajuste = 0.05

percReaj = percentualReajuste*100

# 2- Calcular valor de reajuste e aplicar ao valor inicial para atualização salarial
# do funcionário

valorReajuste = salarioFuncionario*percentualReajuste
salarioAtualizado = valorReajuste + salarioFuncionario

# 3- Resultado do calculo total de reajuste

print("O funcionário que recebe R$", salarioFuncionario, " tendo o reajuste de", percReaj, 
   "porcento, terá o novo valor mensal total de R$", salarioAtualizado)
