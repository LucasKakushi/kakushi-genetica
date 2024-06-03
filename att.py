#====================================declarações de funções====================================

lei = ''
sair = ''

def ordenar_genotipo_abab(genotipo):
    alelos = sorted(genotipo, key=lambda x: (x.lower(), x))
    return alelos[0] + alelos[2] + alelos[1] + alelos[3]

def ordenar_preR(escolhas):
    gen1 = sorted(escolhas, key=lambda x:(x.lower(), x))
    return gen1[0] + gen1 [1]

def porcentagem(resultados):
    frequencia = {}
    total = len(resultados)

    for resultado in resultados:
        if resultado in frequencia:
            frequencia[resultado] += 1
        else:
            frequencia[resultado] = 1


    porcentagem = {valor1: (valor2/total) *100 for valor1, valor2 in frequencia.items()}
    return frequencia, porcentagem

#========================================menu de escolha==========================================================      
for x in range(1000):
    print('bem vindo à calculadora de probabilidade genética ')
    print('estou trabalhando no código, então caso tenha algum bug, peço que me contate.')

    print('========================================')
    print('você gostaria de relacionar com a primeira [1], ou segunda [2] lei de mendel?')
    lei = input('Resposta: ')

#================ 1ª lei ===============================/////////////////////////////////

    if lei == '1': 
        print('===========================================')
        print('===========================================')
        print('por favor, digite em sequência do genótipo do 1º indivíduo:')
        escolhaA1 = input('Resposta: ')
        escolhaA2 = input('Resposta: ')



        print('por favor, digite em sequência do genótipo do 2º indivíduo:')
        escolhaB1 = input('Resposta: ')
        escolhaB2 = input('Resposta: ')
        
        cruz = [
        [escolhaA1 + escolhaA2],
        [escolhaB1 + escolhaB2]
        ]

        resultados = [
            ''.join(sorted([escolhaA1, escolhaB1], key=lambda x: (x.lower(), x))),
            ''.join(sorted([escolhaA1, escolhaB2], key=lambda x: (x.lower(), x))),
            ''.join(sorted([escolhaA2, escolhaB1], key=lambda x: (x.lower(), x))),
            ''.join(sorted([escolhaA2, escolhaB2], key=lambda x: (x.lower(), x)))
        ]



        print('cruzamentos finais: ', cruz[0], " x ", cruz[1])
        print('=======================')
        print('////', resultados [0], resultados [1], '////')
        print('////', resultados [2], resultados [3], '////')
        print('=======================')

        print('[sim]  [não]')
        sair = input('você deseja sair?: ')

    #=========================================================//////////////////////////////////
    #=============== 2ª lei ==================================//////////////////////////////////


    elif lei == '2':
        print('===========================================')
        print('===========================================')
        print('por favor, digite em sequência do genótipo do 1º indivíduo:')
        escolhaA1 = input('Resposta: ')
        escolhaA2 = input('Resposta: ')
        escolhaA3 = input('Resposta: ')
        escolhaA4 = input('Resposta: ')


        print('por favor, digite em sequência do genótipo do 2º indivíduo:')
        escolhaB1 = input('Resposta: ')
        escolhaB2 = input('Resposta: ')
        escolhaB3 = input('Resposta: ')
        escolhaB4 = input('Resposta: ')

        cruz2 = [
        [escolhaA1 + escolhaA2 + escolhaA3 + escolhaA4],
        [escolhaB1 + escolhaB2 + escolhaB3 + escolhaB4]
        ]

        preR = [          #pre resultados dos fenótipos ex: AB, ab
        [ordenar_preR(escolhaA1 + escolhaA3), ordenar_preR(escolhaA1 + escolhaA4), ordenar_preR(escolhaA2 + escolhaA3), ordenar_preR(escolhaA2 + escolhaA4)],
        [ordenar_preR(escolhaB1 + escolhaB3), ordenar_preR(escolhaB1 + escolhaB4), ordenar_preR(escolhaB2 + escolhaB3), ordenar_preR(escolhaB2 + escolhaB4)]
        ]

        w1, x1, y1, z1 = preR [0]                                            
        w2, x2, y2, z2 = preR [1]                                                

        resultados = [
        ordenar_genotipo_abab(w1 + w2), ordenar_genotipo_abab(w1 + x2), ordenar_genotipo_abab(w1 + y2), ordenar_genotipo_abab(w1 + z2),
        ordenar_genotipo_abab(x1 + w2), ordenar_genotipo_abab(x1 + x2), ordenar_genotipo_abab(x1 + y2), ordenar_genotipo_abab(x1 + z2),
        ordenar_genotipo_abab(y1 + w2), ordenar_genotipo_abab(y1 + x2), ordenar_genotipo_abab(y1 + y2), ordenar_genotipo_abab(y1 + z2),
        ordenar_genotipo_abab(z1 + w2), ordenar_genotipo_abab(z1 + x2), ordenar_genotipo_abab(z1 + y2), ordenar_genotipo_abab(z1 + z2),
        ]



        frequencias, porcentagens = porcentagem(resultados)

        print('Cruzamentos finais: ', cruz2[0], " x ", cruz2[1])
        print('=============================')
        for i in range(0, len(resultados), 4):
            print(resultados[i], resultados[i + 1], resultados[i + 2], resultados[i + 3])
        print('=============================')

        print('Frequências dos genótipos:')
        for genotipo, freq in frequencias.items():
            print(f'{genotipo}: {freq} vezes')

        print('Porcentagens dos genótipos:')
        for genotipo, porcentagem in porcentagens.items():
            print(f'{genotipo}: {porcentagem:.2f}%')

        print('Você deseja sair? [sim]  [não]')
        sair = input('Resposta: ')
        if sair.lower() == "sim":
            break

    #=========================================================//////////////////////////////////
        print('Você deseja sair? [sim]  [não]')
        sair = input('Resposta: ')
        if sair.lower() == "sim":
            break
    #=========================================================//////////////////////////////////