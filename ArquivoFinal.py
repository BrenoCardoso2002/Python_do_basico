# função que verifica se o número é par ou impar:
def verifica_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

indice = 1 # variavel do indice do laço de repetição:

# laço de repetição:
while indice <= 5:
    num = input("Insira o " + str(indice) + "º número: ")
    numero = int(num)
    if verifica_par(numero):
        print(str(num) + " é um número par!")
    else:
        print(str(num) + " é um número impar!")
    indice += 1
    print() # print para ter uma linha em branco entre cada repetição.
