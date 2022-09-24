from time import sleep
print('=-'*10)
print("       FATORIAL")
print('=-'*10)
fatorial = int(input("Digite um número: "))
cont = fatorial
f = 1
opção = 0
while opção != 4:
    print("""    [1] Loop While
    [2] Loop For
    [3] Novos Números 
    [4] Sair""")
    opção = int(input("Selecione: "))
    if opção == 1:
        print("\033[34mFatorial de {}! =".format(fatorial),end=' ')
        while cont > 0:
            print(cont,end=' ')
            print('x' if cont > 1 else '=',end=' ')
            f *= cont
            cont -= 1
        print('{}\033[m'.format(f))
        solução = str(input("Deseja ver a Solução? [S/N] ")).strip().upper()
        while solução == '':
            print("Apenas S/N, Por favor.")
            solução = str(input("Deseja ver a Solução? [S/N] ")).strip().upper()
        if solução == 'S':
            print("""SOLUÇÃO:
print("Fatorial de {}! =".format(fatorial),end=' ')
while cont > 0:
    print(cont,end=' ')
    print('x' if cont > 1 else '=',end=' ')
    f *= cont
    cont -= 1
print('{}'.format(f))""")
            break
    elif opção == 2:
        print("\033[31mFatorial de !{} =".format(fatorial),end=' ')
        for cc in range(fatorial,0,-1):
            print(cc, end=' ')
            print('x' if cc > 1 else '=',end=' ')
            f *= cc
            cc -= 1
        print('{}\033[m'.format(f))
        solução = str(input("Deseja ver a Solução? [S/N] ")).strip().upper()
        while solução == '':
            print("Apenas S/N, Por Favor.")
            solução = str(input("Deseja ver a Solução? [S/N] ")).strip().upper()
        if solução == 'S':
            print("""SOLUÇÃO:
print("Fatorial de !{} =".format(fatorial),end=' ')
for cc in range(fatorial,0,-1):
    print(cc, end=' ')
    print('x' if cc > 1 else '=',end=' ')
    f *= cc
    cc -= 1
print('{}'.format(f))""")
            break
    elif opção == 3:
        print("Tudo Bem")
        fatorial = int(input("Novo Valor: "))
    elif opção == 4:
        print("Até Logo.")
        break
    else:
        print("Opção inválida, Tente novamente.")
        sleep(2)
