import matplotlib.pyplot as plt
import pandas as pd

PATH = '/home/bastieng/cpac/annotation/projection_ar'
PATH2 = '/home/bastieng/cpac/train_corpus'
EXTRACTED_COLL = [
    # '/gold/projection.gold.en.cupt.pos.out',
    # '/gold/projection.gold.GV.en.cupt.pos.out',
    # '/gold/projection.gold.TED.en.cupt.pos.out',
    # '/gold/projection.gold.UN.en.cupt.pos.out',
    # '/gold/projection.gold.WM.en.cupt.pos.out',
    # '/gold/listes_coll/projection.gold.en.cupt.pos.out',
    # '/gold/listes_coll/projection.gold.GV.en.cupt.pos.out',
    # '/gold/listes_coll/projection.gold.TED.en.cupt.pos.out',
    # '/gold/listes_coll/projection.gold.UN.en.cupt.pos.out',
    # '/gold/listes_coll/projection.gold.WM.en.cupt.pos.out'
    '/gold/listes_coll/extracted_coll.GOLD.ar.out',
    '/gold/listes_coll/extracted_coll.GOLD.GV.ar.out',
    '/gold/listes_coll/extracted_coll.GOLD.TED.ar.out',
    '/gold/listes_coll/extracted_coll.GOLD.UN.ar.out',
    '/gold/listes_coll/extracted_coll.GOLD.WM.ar.out'
    # '/projection.auto.ar.cupt.pos.out',
    # '/doubleprojection.auto.ar.cupt.pos.out'
]
TRAIN = '/extracted_coll.TRAIN.out'

# TEST = EXTRACTED_COLL[0]

for file in EXTRACTED_COLL:
    with open(PATH + file, 'r', encoding='utf8') as f:
        print(f">>> Reading {PATH}{file}...")
        dic_colls = dict()
        # Remplissage du dico de collocations + occurrences
        for line in f:
            if not line.rstrip() in dic_colls.keys():
                dic_colls[line.rstrip()] = 1
            else:
                dic_colls[line.rstrip()] += 1
        print(len(dic_colls))

    sorted_dic_colls = {k: v for k, v in sorted(dic_colls.items(),
                                                reverse=True,
                                                key=lambda item: item[1])}

    # Création du DF
    data = {'Pattern': [pattern for pattern in sorted_dic_colls.keys()],
            'Occurrences': [occ for occ in sorted_dic_colls.values()]}
    coll_df = pd.DataFrame(data)
    # print(coll_df.head(10))
    print(f">>> Saving dataframe into {PATH}{file}...")
    # Sauvegarde du DF
    coll_df.to_csv(f'{PATH}{file[:-3]}csv', index=False)
    # Création et sauvegarde des plots en PNG
    coll_df.head(10).plot(x='Pattern', y='Occurrences', kind='bar',
                          xlabel='Pattern', ylabel='Occurrences', legend=False,
                          colormap='Accent', rot=20, figsize=(15, 12),
                          fontsize=16)
    plt.savefig(f'{PATH}{file[:-3]}png')
    coll_df = pd.DataFrame()
