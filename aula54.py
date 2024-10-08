import os

lista_compras = []

while True:
    print('Selecione uma opcao')
    resposta = input('[i]nserir [a]pagar [l]istar [s]air: ').strip().lower()

    if resposta == 'i':
        os.system('cls')
        lista_compras.append(input('Valor: '))

    elif resposta == 'a':
        try:
            apagar = int(input('Indice que quer apagar: '))
            del lista_compras[apagar]
            print('Item apagado com sucesso!')
        
        except ValueError:
            print('Por favor digite um numero inteiro!')
        except TypeError:
            print('Este indice nao existe na lista atual!')

    elif resposta == 'l':
        if '' in lista_compras:
            print('Nada a mostrar')
        else:
            for indice, item in enumerate(lista_compras):
                print(indice, item)

    elif resposta == 's':
        print('Encerrando Programa...')
        break

    else:
        print('Essa opcao nao existe!')
