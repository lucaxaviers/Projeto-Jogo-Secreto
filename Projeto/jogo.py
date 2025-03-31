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
print("Após a 5° tentativa vamos te dar dicas")
print(" ------------------------------------------------")
cont=0
code = 2710
digito1 = code // 1000            
digito2 = (code // 100) % 10     
digito3 = (code // 10) % 10       
digito4 = code % 10   

certo1=0
certo2=0
certo3=0
certo4=0

tentativa=0
tent1 = tentativa // 1000            
tent2 = (tentativa // 100) % 10     
tent3 = (tentativa // 10) % 10       
tent4 = tentativa % 10


for cont in range(10): 
    tentativa=int(input("Digite um numero entre 1000 e 9999: "))
    if tentativa < 1000 and tentativa > 9999:
            print("Número fora do intervalo! Digite um número entre 1000 e 9999.")

    if tentativa == code:
                print("Parabénsss Você Acertou o segredo de Primeira!!!!!")


    if tent1==digito1:
        certo1 = tent1
    else:
        certo2 = "_"
    
    if tent2==digito2:
        certo2 = tent2
    else:
        certo2 = "_"

    if tent3==digito3:
        certo3 = tent3
    else:
        certo3 = "_"

    if tent4==digito4:
        certo4 = tent4
    else:
        certo4 = "_"     
    
    
    print(f"{certo1} {certo2} {certo3} {certo4}")
tipodica = 0
if cont >= 5:
     if tent1!=digito1:
        if tipodica==0
            if digito1>5:
                print(f"O primeiro dígito é maior que 5")
            else:
                print(f"O primeiro dígito é menor ou igual a 5")
            tipodica=1
        else:
            if digito1%2==0:
                print(f"O primeiro dígito é par")
            else:
                print(f"O primeiro dígito é ímpar")
            tipodica=0

    