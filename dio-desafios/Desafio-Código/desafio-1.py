#DESAFIO!!!
#
#Faça um programa que calcule e imprima o salário
#a ser transferido para um funcionário.
#
#Para ealizar o calculo, receba o valor bruto do salário adicional
#dos benefícios e o valor dos descontos
#
#O salário a ser transferido é calculado da seguinte forma:
#
#(valor bruto do salário - percentual de impostos mediante ao salário) + adional dos benefícios
#
# Para calcular o percentual de imposto segue as alíquotas:
#
# De R$ 0.00 a R$ 1100.00 - 5.00%
# De R$ 1100.01 a R$ 2500.00 - 10.00%
# Maior que R$ 2500.00 - 15.00%
#
# Entrada
#
# A entrada consiste em vários arquivos de teste, que conterá o valor
# bruto do salário e adicional dos benefícios. Conforme mostrado
# no exemplo de entrada a seguir.
#
# Saída
#
# Para cada arquivo de entrada, terá um arquivo de saída. É como
# mencionado no Desafio, será gerado uma linha com um
# número que será a diferença entre o valor bruto do salário e o
# percentual do imposto mediante a faixa salarial somado com o
# adicional dos benefícios. 

salario_bruto = float(input("Qual o seu salário bruto? "))
adicional_beneficios = float(input("Qual o adicional dos benefícios? "))   

if salario_bruto <= 1100.00:
    percentual_imposto = 0.05
elif salario_bruto <= 2500.00:
    percentual_imposto = 0.10   
else:
    percentual_imposto = 0.15

salario_liquido = (salario_bruto - (salario_bruto * percentual_imposto)) + adicional_beneficios 
print(f"{salario_liquido:.2f}")

