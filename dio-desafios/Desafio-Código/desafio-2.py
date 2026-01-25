# DESAFIO
#
# Uma produtora e exportadora de papéis para embalagens precisa calcular
# o valor final de suas exportações. Cada remessa possui um peso em
# toneladas e um preço por tonelada em dólares. Além disso, dependendo
# do tipo de cliente, a empresa oferece descontos:
#
# Novo cliente: sem desconto
# Cliente fidelizado: 5% de desconto
# Cliente premium: 10% de desconto
#
# O programa deve calcular o valor total da remessa considerando o peso,
# o preço por tonelada e o desconto aplicável, retornando o valor final
# a ser pago pelo cliente.
#
# Entrada
#
# A entrada deve receber:
#
# Um número decimal representando o peso da carga em toneladas.
# Um número decimal representando o preço por tonelada em dólares.
# Uma string representando o tipo de cliente ("Novo cliente",
# "Cliente fidelizado", "Cliente premium").
#
# Saída
#
# O programa deverá retornar o valor final da exportação (em dólares),
# já com o desconto aplicado, formatado com duas casas decimais.


peso_toneladas = float(input("Digite o peso da carga em toneladas: "))
preco_por_tonelada = float(input("Digite o preço por tonelada em dólares: "))
tipo_cliente = input("Digite o tipo de cliente (Novo cliente, Cliente fidelizado, Cliente premium): ")  

valor_total = peso_toneladas * preco_por_tonelada

if tipo_cliente == "Novo cliente":
    desconto = 0.0
elif tipo_cliente == "Cliente fidelizado":
    desconto = 0.05 
elif tipo_cliente == "Cliente premium":
    desconto = 0.10 
else:
    desconto = 0.0

valor_final = valor_total * (1 - desconto)
print(f"{valor_final:.2f}")
