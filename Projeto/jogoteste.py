import random

print("===>   !SEJA BEM VINDO AO JOGO SECRETO!   <===")
print(" ------------------------------------------------")
print("              Desenvolvido Por:")
print("                Lucas Xavier,")
print("               Mateus Oliveira,")
print("              Wanderley Vieira,")
print("               Arthur Grizone;")
print(" ------------------------------------------------")
print(" ===>        EXPLICANDO O JOGO        <===")
print("Objetivo:\nAcertar um número secreto de 4 dígitos (entre 1000 e 9999) em 10 tentativas.")
print("Após a 5° tentativa, vamos te dar dicas extras.")
print(" ------------------------------------------------")

# Gerar um número secreto aleatório entre 1000 e 9999
code = random.randint(1000, 9999)
digito1 = code // 1000            
digito2 = (code // 100) % 10     
digito3 = (code // 10) % 10       
digito4 = code % 10  

tentativas = 0

# Variáveis para armazenar os acertos
acerto1 = "_"
acerto2 = "_"
acerto3 = "_"
acerto4 = "_"

while tentativas < 10:
    tentativa = int(input(f"Tentativa {tentativas + 1}/10 - Digite um número entre 1000 e 9999: "))

    if tentativa < 1000 or tentativa > 9999:
        print("Número fora do intervalo! Digite um número entre 1000 e 9999.")
        continue

    tent1 = tentativa // 1000            
    tent2 = (tentativa // 100) % 10     
    tent3 = (tentativa // 10) % 10       
    tent4 = tentativa % 10 

    # Verificação de acertos
    if tent1 == digito1:
        acerto1 = str(tent1)
    elif tent1 in [digito2, digito3, digito4]:
        print(f"O número {tent1} está correto, mas na posição errada.")

    if tent2 == digito2:
        acerto2 = str(tent2)
    elif tent2 in [digito1, digito3, digito4]:
        print(f"O número {tent2} está correto, mas na posição errada.")

    if tent3 == digito3:
        acerto3 = str(tent3)
    elif tent3 in [digito1, digito2, digito4]:
        print(f"O número {tent3} está correto, mas na posição errada.")

    if tent4 == digito4:
        acerto4 = str(tent4)
    elif tent4 in [digito1, digito2, digito3]:
        print(f"O número {tent4} está correto, mas na posição errada.")

    # Exibe os números corretos e os espaços vazios para os não descobertos
    print(f"Progresso: {acerto1} {acerto2} {acerto3} {acerto4}")

    tentativas += 1

    # Dicas extras após a 5ª tentativa
    if tentativas >= 5:
        print("\nDicas extras:")
        if digito1 > 5:
            print(f"O primeiro dígito é maior que 5.")
        else:
            print(f"O primeiro dígito é menor ou igual a 5.")
        
        if digito1 % 2 == 0:
            print(f"O primeiro dígito é par.")
        else:
            print(f"O primeiro dígito é ímpar.")

if tentativas == 10 and tentativa != code:
    print(f"\n❌ Fim de jogo! O número secreto era {code}. Melhor sorte na próxima vez!")
