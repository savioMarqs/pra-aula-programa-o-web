#Desenvolva um programa Python que devolva leia um nome e uma data e retorne uma String. Neste caso o programa vai 
# falar a data de nascimento de alguém.
nome = input("Digite o Nome: ").title()
dia = input("Digite o dia: ").title()
mes = input("Digite o mês: ").title()
ano = input("Digite o ano: ").title()




txt = "{} nasceu no dia: {}/{}/{}"
print(txt.format(nome,dia,mes,ano))