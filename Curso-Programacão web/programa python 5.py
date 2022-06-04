#Crie um sistema que imprima um recibo de compras para o usuário. O sistema vai perguntar a quantidade de itens 
# diferentes e depois vai perguntar qual o nome do item e a quantidade deste item. No final o programa exibe o recibo
#  juntamente com o valor final da compra. Veja um exemplo de como o sistema deve funcionar: 



QuantidadeDeItens = float(input("Digite quantos itens: "))

valorTotal = 0

itens = []

i = 0
while i < QuantidadeDeItens:
    nome = input("nome do item " + str(i+1) + ": ")
    quantia = float(input("Quantidade desse produto " + str(i+1) + ": "))
    valorTotal += quantia
    preçoProduto = {
        "nome": nome,
        "quantia": quantia
    }
    itens.append(preçoProduto)
    i += 1

print("Nome | Quantia")
for itens in quantia:
    print("{} | {} ".format(quantia["nome"], itens["quantia"]))

print("total: " + str(valorTotal * QuantidadeDeItens))

#erro na linha 26, não consegui consertar
        
    




