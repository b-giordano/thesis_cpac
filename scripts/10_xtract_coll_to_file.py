import string

digits = [str(x) for x in string.digits]
digits = ''.join(digits)

# Constantes, chemins de fichiers
PATH = '/home/bastieng/cpac/annotation/projection_ar'
PATH2 = '/home/bastieng/cpac'
GOLD = [
    # '/doubleprojection.gold.ar.cupt'
    # '/auto/projection.auto.ar.cupt',
    # '/auto/doubleprojection.auto.ar.cupt'
    '/gold/doubleprojection.gold.ar.cupt',
    '/gold/doubleprojection.gold.GV.ar.cupt',
    '/gold/doubleprojection.gold.TED.ar.cupt',
    '/gold/doubleprojection.gold.UN.ar.cupt',
    '/gold/doubleprojection.gold.WM.ar.cupt'
]
TRAIN = '/train_corpus/train_coll_endv2.cupt'
# Variable de test
TEST = '/test.cupt'
TEST_OUT = '/test.out'

# Listes de collocations
coll1, coll2, coll3, coll4 = list(), list(), list(), list()
coll5, coll6, coll7, list_colls = list(), list(), list(), list()

for file in GOLD:
    with open(PATH + file, 'r', encoding='utf8') as f:
        print(f">>> Reading {PATH}{file}...")
        for line in f:
            line = line.lower().rstrip()
            if line.startswith('#'):
                continue
            elif len(line) < 2:
                if len(coll1) > 1:
                    list_colls.append(coll1)
                if len(coll2) > 1:
                    list_colls.append(coll2)
                if len(coll3) > 1:
                    list_colls.append(coll3)
                if len(coll4) > 1:
                    list_colls.append(coll4)
                if len(coll5) > 1:
                    list_colls.append(coll5)
                if len(coll6) > 1:
                    list_colls.append(coll6)
                if len(coll7) > 1:
                    list_colls.append(coll7)
                coll1, coll2, coll3, coll4 = list(), list(), list(), list()
                coll5, coll6, coll7 = list(), list(), list()
                continue
            else:
                linesplit = line.split('\t')
                annot = linesplit[10]
                idx = linesplit[0]
                lemma = linesplit[2]
                pos = linesplit[3]
                if ';' in annot:
                    annot = annot.split(';')
                    for i in range(len(annot)):
                        if '1' in annot[i]:
                            coll1.append((lemma, annot[i]))
                            # coll1.append((pos, annot[0]))
                        if '2' in annot[i]:
                            coll2.append((lemma, annot[i]))
                            # coll2.append((pos, annot[0]))
                        if '3' in annot[i]:
                            coll3.append((lemma, annot[i]))
                            # coll3.append((pos, annot[0]))
                        if '4' in annot[i]:
                            coll4.append((lemma, annot[i]))
                            # coll4.append((pos, annot[0]))
                        if '5' in annot[i]:
                            coll5.append((lemma, annot[i]))
                            # coll5.append((pos, annot[0]))
                        if '6' in annot[i]:
                            coll6.append((lemma, annot[i]))
                            # coll6.append((pos, annot[0]))
                        if '7' in annot[i]:
                            coll7.append((lemma, annot[i]))
                            # coll7.append((pos, annot[0]))

                    # if len(annot) == 3:
                    #     if '1' in annot[2]:
                    #         # coll1.append((lemma, annot[2]))
                    #         coll1.append((pos, annot[0]))
                    #     if '2' in annot[2]:
                    #         # coll2.append((lemma, annot[2]))
                    #         coll2.append((pos, annot[0]))
                    #     if '3' in annot[2]:
                    #         # coll3.append((lemma, annot[2]))
                    #         coll3.append((pos, annot[0]))
                    #     if '4' in annot[2]:
                    #         # coll4.append((lemma, annot[2]))
                    #         coll4.append((pos, annot[0]))
                    #     if '5' in annot[2]:
                    #         # coll5.append((lemma, annot[2]))
                    #         coll5.append((pos, annot[0]))
                    #     if '6' in annot[2]:
                    #         # coll6.append((lemma, annot[2]))
                    #         coll6.append((pos, annot[0]))
                    #     if '7' in annot[2]:
                    #         # coll7.append((lemma, annot[2]))
                    #         coll7.append((pos, annot[0]))
                else:
                    if annot[0] == '1':
                        coll1.append((lemma, annot))
                        # coll1.append((pos, annot[0]))
                    elif annot[0] == '2':
                        coll2.append((lemma, annot))
                        # coll2.append((pos, annot[0]))
                    elif annot[0] == '3':
                        coll3.append((lemma, annot))
                        # coll3.append((pos, annot[0]))
                    elif annot[0] == '4':
                        coll4.append((lemma, annot))
                        # coll4.append((pos, annot[0]))
                    elif annot[0] == '5':
                        coll5.append((lemma, annot))
                        # coll5.append((pos, annot[0]))
                    elif annot[0] == '6':
                        coll6.append((lemma, annot))
                        # coll6.append((pos, annot[0]))
                    elif annot[0] == '7':
                        coll7.append((lemma, annot))
                        # coll7.append((pos, annot[0]))

        print(len(list_colls))
        with open(PATH + file + ".out", 'w', encoding='utf8') as g:
            print(f">>> Writing in {PATH}{file}.pos.out...")
            for x in list_colls:
                if len(x) == 2:
                    coll = [x[0][0], x[1][0]]
                    g.write('|'.join(sorted(coll)) + '\n')
                    # print('|'.join(sorted(coll)))
                else:
                    coll = [x[0][0], x[1][0], x[2][0]]
                    g.write('|'.join(sorted(coll)) + '\n')
                    # print('|'.join(sorted(coll)))
            list_colls = list()
