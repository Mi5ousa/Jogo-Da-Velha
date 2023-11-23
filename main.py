import random

def desenhar_table(table):
    print("-"*35, end="\n\n")
    print(end="       ")
    for i, sp in enumerate(table[0]):
       if i < 2:
           if sp == 0:
               print(" ", end="|")
           elif sp == 1:
               print("X", end="|")
           elif sp == 2:
               print("0", end="|")
       else:
            if sp == 0:
                print(" ")
            elif sp == 1:
                print("X")
            elif sp == 2:
                print("0")
    print(end="      ")
    print("-------")
    print(end="       ")
    for i, sp in enumerate(table[1]):
       if i < 2:
           if sp == 0:
               print(" ", end="|")
           elif sp == 1:
               print("X", end="|")
           elif sp == 2:
               print("0", end="|")
       else:
            if sp == 0:
                print(" ")
            elif sp == 1:
                print("X")
            elif sp == 2:
                print("0")
    print(end="      ")
    print("-------")
    print(end="       ")
    for i, sp in enumerate(table[2]):
       if i < 2:
           if sp == 0:
               print(" ", end="|")
           elif sp == 1:
               print("X", end="|")
           elif sp == 2:
               print("0", end="|")
       else:
            if sp == 0:
                print(" ")
            elif sp == 1:
                print("X")
            elif sp == 2:
                print("0")
    print("\n", "-"*35)


def player1(table):
    loop = True
    while loop:
        while True:
            try:
                esc = int(input("Player1\nDigite um número que corresponde a onde você quer jogar, \n\n    1, 2, 3\n    4, 5, 6\n    7, 8, 9\n\nNumero: "))
            except:
                print("Erro, digite um número inteiro")
            else:
                if 0 < esc < 10:
                    break
                else:
                    print("Digite um número correto")
        linhaesc = 0
        vesc = 0
        if esc <= 3:
            linhaesc = 1
            vesc = esc
        elif esc <= 6:
            linhaesc = 2
            vesc = esc - 3
        elif esc <= 9:
            linhaesc = 3
            vesc = esc - 6
        for I, linha in enumerate(table):
            for i, v in enumerate(linha):
                if I+1 == linhaesc:
                    if i+1 == vesc:
                        if v == 1 or v == 2:
                            print("Esse espaço já está sendo ocupado, Tente novamente")
                        else:
                            table[I][i] = 1
                            loop = False
            
    return table
    

def player2(table):
    loop = True
    while loop:
        while True:
            try:
                esc = int(input("Player2\nDigite um número que corresponde a onde você quer jogar, \n\n    1, 2, 3\n    4, 5, 6\n    7, 8, 9\n\nNumero: "))
            except:
                print("Erro, digite um número inteiro")
            else:
                if 0 < esc < 10:
                    break
                else:
                    print("Digite um número correto")
        linhaesc = 0
        vesc = 0
        if esc <= 3:
            linhaesc = 1
            vesc = esc
        elif esc <= 6:
            linhaesc = 2
            vesc = esc - 3
        elif esc <= 9:
            linhaesc = 3
            vesc = esc - 6
        for I, linha in enumerate(table):
            for i, v in enumerate(linha):
                if I+1 == linhaesc:
                    if i+1 == vesc:
                        if v == 1 or v == 2:
                            print("Esse espaço já está sendo ocupado, Tente novamente")
                        else:
                            table[I][i] = 2
                            loop = False
            
    return table


def player(table, lado):
    loop = True
    while loop:
        while True:
            try:
                esc = int(input("Player\nDigite um número que corresponde a onde você quer jogar, \n\n    1, 2, 3\n    4, 5, 6\n    7, 8, 9\n\nNumero: "))
            except:
                print("Erro, digite um número inteiro")
            else:
                if 0 < esc < 10:
                    break
                else:
                    print("Digite um número correto")
        linhaesc = 0
        vesc = 0
        if esc <= 3:
            linhaesc = 1
            vesc = esc
        elif esc <= 6:
            linhaesc = 2
            vesc = esc - 3
        elif esc <= 9:
            linhaesc = 3
            vesc = esc - 6
        for I, linha in enumerate(table):
            for i, v in enumerate(linha):
                if I+1 == linhaesc:
                    if i+1 == vesc:
                        if v == 1 or v == 2:
                            print("Esse espaço já está sendo ocupado, Tente novamente")
                        else:
                            table[I][i] = lado
                            loop = False
            
    return table


def bot(table, lado, modo):
    loop = True
    while loop:
        if modo == 1:
            esc = random.randint(1, 9)
            linhaesc = 0
            vesc = 0
            if esc <= 3:
                linhaesc = 1
                vesc = esc
            elif esc <= 6:
                linhaesc = 2
                vesc = esc - 3
            elif esc <= 9:
                linhaesc = 3
                vesc = esc - 6
            for I, linha in enumerate(table):
                for i, v in enumerate(linha):
                    if I+1 == linhaesc:
                        if i+1 == vesc:
                            if v == 1 or v == 2:
                                pass
                            else:
                                if lado == 1:
                                    table[I][i] = 2
                                elif lado == 2:
                                    table[I][i] = 1
                                loop = False
            
    return table


def verificacao(table):
    
    ganho1 = False
    ganho2 = False
    empate = False
    
    if table[0][0] == 1 and table[0][1] == 1 and table[0][2] == 1:
        ganho1 = True
    elif table[1][0] == 1 and table[1][1] == 1 and table[1][2] == 1:
        ganho1 = True
    elif table[2][0] == 1 and table[2][1] == 1 and table[2][2] == 1:
        ganho1 = True
    
    elif table[0][0] == 1 and table[1][0] == 1 and table[2][0] == 1:
        ganho1 = True
    elif table[0][1] == 1 and table[1][1] == 1 and table[2][1] == 1:
        ganho1 = True
    elif table[0][2] == 1 and table[1][2] == 1 and table[2][2] == 1:
        ganho1 = True
    
    elif table[0][0] == 1 and table[1][1] == 1 and table[2][2] == 1:
        ganho1 = True
    elif table[2][0] == 1 and table[1][1] == 1 and table[0][2] == 1:
        ganho1 = True
        
    elif table[0][0] == 2 and table[0][1] == 2 and table[0][2] == 2:
        ganho2 = True
    elif table[1][0] == 2 and table[1][1] == 2 and table[1][2] == 2:
        ganho2 = True
    elif table[2][0] == 2 and table[2][1] == 2 and table[2][2] == 2:
        ganho2 = True
    
    elif table[0][0] == 2 and table[1][0] == 2 and table[2][0] == 2:
        ganho2 = True
    elif table[0][1] == 2 and table[1][1] == 2 and table[2][1] == 2:
        ganho2 = True
    elif table[0][2] == 2 and table[1][2] == 2 and table[2][2] == 2:
        ganho2 = True
    
    elif table[0][0] == 2 and table[1][1] == 2 and table[2][2] == 2:
        ganho2 = True
    elif table[2][0] == 2 and table[1][1] == 2 and table[0][2] == 2:
        ganho2 = True
    
    else:
        iempate = 0
        for linha in table:
            for v in linha:
                if v == 0:
                    pass
                else:
                    iempate += 1
        if iempate == 9:
            empate = True
    
    return ganho1, ganho2, empate


table = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
PxPloop = True
PxBloop = True
mainloop = True
gameloop = True

while gameloop:
    while mainloop:
        print(" Menu")
        print("(1) Jogar PxP")
        print("(2) Jogar PxB")
        print("(3) Sair")
        while True:
            try:
                esc1 = int(input("Digite uma opção: "))
            except:
                print("Erro, tente novamente.")
            else:
                if 1 <= esc1 <= 3:
                    mainloop = False
                    break
                else:
                    print("Opção incorreta, tente novamente.")
    
    if esc1 == 3:
        break
    elif esc1 == 2:
        while True:
            
            try:
                lado = int(input("Você usará o X ou 0? (1=X, 2=0): "))
            except:
                print("Erro, tente novamente.")
            else:
                if 1 <= lado <= 2:
                    break
                else:
                    print("Opção inválida, tente novamente.")
        
        while True:
            
            try:
                modo = int(input("Modos 1Facil, 2Medio 3Dificil 4Imposivel: "))
            except:
                print("Erro, tente novamente.")
            else:
                if 1 <= modo <= 4:
                    break
                else:
                    print("Opção inválida, tente novamente.")
        
        while PxBloop:
            desenhar_table(table)
            if lado == 1:
                table = player(table, lado)
            else:
                table = bot(table, lado, modo)
            desenhar_table(table)
            veri = verificacao(table)
            
            if veri[0]:
                if lado == 1:
                    print("Você ganhou")
                    while True:
                        esc = input("Quer Recomeçar? (s/n): ")
                        if esc.lower() == "s":
                            table = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                            desenhar_table(table)
                            if lado == 1:
                                table = player(table, lado)
                            else:
                                table = bot(table, lado, modo)
                            break
                        elif esc.lower() == "n":
                            PxBloop = False
                            break
                        else:
                            print("Digite uma opção válida")
                else:
                    print("Você perdeu")
                    while True:
                        esc = input("Quer Recomeçar? (s/n): ")
                        if esc.lower() == "s":
                            table = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                            desenhar_table(table)
                            if lado == 1:
                                table = player(table, lado)
                            else:
                                table = bot(table, lado, modo)
                            break
                        elif esc.lower() == "n":
                            PxBloop = False
                            break
                        else:
                            print("Digite uma opção válida")
                            
            elif veri[1]:
                if lado == 2:
                    print("Você ganhou")
                    while True:
                        esc = input("Quer Recomeçar? (s/n): ")
                        if esc.lower() == "s":
                            table = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                            desenhar_table(table)
                            if lado == 1:
                                table = player(table, lado)
                            else:
                                table = bot(table, lado, modo)
                            break
                        elif esc.lower() == "n":
                            PxBloop = False
                            break
                        else:
                            print("Digite uma opção válida")
                else:
                    print("Você perdeu")
                    while True:
                        esc = input("Quer Recomeçar? (s/n): ")
                        if esc.lower() == "s":
                            table = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                            desenhar_table(table)
                            if lado == 1:
                                table = player(table, lado)
                            else:
                                table = bot(table, lado, modo)
                            break
                        elif esc.lower() == "n":
                            PxBloop = False
                            break
                        else:
                            print("Digite uma opção válida")
                            
                
            elif veri[2]:
                print("Empate")
                while True:
                    esc = input("Quer Recomeçar? (s/n): ")
                    if esc.lower() == "s":
                        table = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                        desenhar_table(table)
                        if lado == 1:
                            table = player(table, lado)
                        else:
                            table = bot(table, lado, modo)
                        break
                    elif esc.lower() == "n":
                        PxBloop = False
                        break
                    else:
                        print("Digite uma opção válida")
            if not PxBloop:
                break
                
            if lado == 1:
                table = bot(table, lado, modo)
            else:
                table = player(table, lado)
                
            veri = verificacao(table)
            if veri[0]:
                if lado == 1:
                    print("Você ganhou")
                    while True:
                        esc = input("Quer Recomeçar? (s/n): ")
                        if esc.lower() == "s":
                            table = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                            #desenhar_table(table)
                            #table = player1(table)
                            break
                        elif esc.lower() == "n":
                            PxBloop = False
                            break
                        else:
                            print("Digite uma opção válida")
                else:
                    print("Você perdeu")
                    while True:
                        esc = input("Quer Recomeçar? (s/n): ")
                        if esc.lower() == "s":
                            table = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                            #desenhar_table(table)
                            #table = player1(table)
                            break
                        elif esc.lower() == "n":
                            PxBloop = False
                            break
                        else:
                            print("Digite uma opção válida")
                            
            elif veri[1]:
                if lado == 2:
                    print("Você ganhou")
                    while True:
                        esc = input("Quer Recomeçar? (s/n): ")
                        if esc.lower() == "s":
                            table = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                            #desenhar_table(table)
                            #table = player1(table)
                            break
                        elif esc.lower() == "n":
                            PxBloop = False
                            break
                        else:
                            print("Digite uma opção válida")
                else:
                    print("Você perdeu")
                    while True:
                        esc = input("Quer Recomeçar? (s/n): ")
                        if esc.lower() == "s":
                            table = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                            #desenhar_table(table)
                            #table = player1(table)
                            break
                        elif esc.lower() == "n":
                            PxBloop = False
                            break
                        else:
                            print("Digite uma opção válida")
                            
                
            elif veri[2]:
                print("Empate")
                while True:
                    esc = input("Quer Recomeçar? (s/n): ")
                    if esc.lower() == "s":
                        table = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                        #desenhar_table(table)
                        #table = player1(table)
                        break
                    elif esc.lower() == "n":
                        PxBloop = False
                        break
                    else:
                        print("Digite uma opção válida")
            
    elif esc1 == 1:
        while PxPloop:
            desenhar_table(table)
            table = player1(table)
            veri = verificacao(table)
            if veri[0]:
                print("Player1 Ganhou")
                while True:
                    esc = input("Quer Recomeçar? (s/n): ")
                    if esc.lower() == "s":
                        table = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                        desenhar_table(table)
                        table = player1(table)
                        break
                    elif esc.lower() == "n":
                        PxPloop = False
                        break
                    else:
                        print("Digite uma opção válida")
        
            elif veri[1]:
                print("Player2 Ganhou")
                while True:
                    esc = input("Quer Recomeçar? (s/n): ")
                    if esc.lower() == "s":
                        table = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                        desenhar_table(table)
                        table = player1(table)
                        break
                    elif esc.lower() == "n":
                        PxPloop = False
                        break
                    else:
                        print("Digite uma opção válida")
                
            elif veri[2]:
                print("Empate")
                while True:
                    esc = input("Quer Recomeçar? (s/n): ")
                    if esc.lower() == "s":
                        table = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                        desenhar_table(table)
                        table = player1(table)
                        break
                    elif esc.lower() == "n":
                        PxPloop = False
                        break
                    else:
                        print("Digite uma opção válida")
            if not PxPloop:
                break
            desenhar_table(table)
            table = player2(table)
            veri = verificacao(table)
            if veri[0]:
                print("Player1 Ganhou")
                while True:
                    esc = input("Quer Recomeçar? (s/n): ")
                    if esc.lower() == "s":
                        table = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                        break
                    elif esc.lower() == "n":
                        PxPloop = False
                        break
                    else:
                        print("Digite uma opção válida")
        
            elif veri[1]:
                print("Player2 Ganhou")
                while True:
                    esc = input("Quer Recomeçar? (s/n): ")
                    if esc.lower() == "s":
                        table = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                        break
                    elif esc.lower() == "n":
                        PxPloop = False
                        break
                    else:
                        print("Digite uma opção válida")
                
            elif veri[2]:
                print("Empate")
                while True:
                    esc = input("Quer Recomeçar? (s/n): ")
                    if esc.lower() == "s":
                        table = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                        break
                    elif esc.lower() == "n":
                        PxPloop = False
                        break
                    else:
                        print("Digite uma opção válida")
    mainloop = True