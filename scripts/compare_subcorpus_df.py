import matplotlib.pyplot as plt
import pandas as pd


def unique_patterns(main_dict, out_list) -> list:
    """
    Cherche les patrons uniques d'une liste comparés à la liste des 3 autres
    corpus.
    :param main_dict: Liste (dictionnaire) principale
    :param out_list: Liste de comparaison
    :return: Liste de patrons uniques
    """
    uniq = list()
    for coll in main_dict.keys():
        if coll not in out_list:
            uniq.append((coll, main_dict.get(coll)))

    print(f'Longueur : {len(uniq)}')
    uniq.sort(key=lambda x: x[1], reverse=True)
    return uniq


PATH = '/home/bastieng/cpac/annotation/projection_ar/gold/listes_coll' \
       '/dataframes'
MAIN_df = pd.read_csv(f'{PATH}/extracted_coll.GOLD.ar.csv')
GV_df = pd.read_csv(f'{PATH}/extracted_coll.GOLD.GV.ar.csv')
TED_df = pd.read_csv(f'{PATH}/extracted_coll.GOLD.TED.ar.csv')
UN_df = pd.read_csv(f'{PATH}/extracted_coll.GOLD.UN.ar.csv')
WM_df = pd.read_csv(f'{PATH}/extracted_coll.GOLD.WM.ar.csv')

# Listes pour chaque corpus et ensemble de sous-corpus pour comparaison
lst_GV = [coll for coll in GV_df['Pattern']]
lst_TED = [coll for coll in TED_df['Pattern']]
lst_UN = [coll for coll in UN_df['Pattern']]
lst_WM = [coll for coll in WM_df['Pattern']]
lst_TUW = lst_TED + lst_UN + lst_WM
lst_GUW = lst_GV + lst_UN + lst_WM
lst_GTW = lst_GV + lst_TED + lst_WM
lst_GTU = lst_GV + lst_TED + lst_UN
# Dictionnaires pour chaque corpus (Coll + NB)
dict_GV = {coll: nb for coll, nb
           in zip(GV_df['Pattern'], GV_df['Occurrences'])}
dict_TED = {coll: nb for coll, nb
            in zip(TED_df['Pattern'], TED_df['Occurrences'])}
dict_UN = {coll: nb for coll, nb
           in zip(UN_df['Pattern'], UN_df['Occurrences'])}
dict_WM = {coll: nb for coll, nb
           in zip(WM_df['Pattern'], WM_df['Occurrences'])}
dict_GOLD = {coll: nb for coll, nb
             in zip(MAIN_df['Pattern'], MAIN_df['Occurrences'])}

uniq_GV = unique_patterns(dict_GV, lst_TUW)
uniq_TED = unique_patterns(dict_TED, lst_GUW)
uniq_UN = unique_patterns(dict_UN, lst_GTW)
uniq_WM = unique_patterns(dict_WM, lst_GTU)

uniq_corpora = [
    uniq_GV, uniq_TED, uniq_UN, uniq_WM
]
uniq_corpora_names = [
    "uniq_GV", "uniq_TED", "uniq_UN", "uniq_WM"
]

with open(f'{PATH[:-10]}uniq/uniq_GOLD.csv', 'w', encoding='utf8') as f:
    f.write("Pattern,Occurrences\n")
    for coll, occ in dict_GOLD.items():
        f.write(coll + ',' + str(occ) + '\n')

with open(f'{PATH[:-10]}uniq/uniq_GV.csv', 'w', encoding="utf8") as f:
    f.write("Pattern,Occurrences\n")
    for coll in uniq_corpora[0]:
        f.write(coll[0] + ',' + str(coll[1]) + '\n')

with open(f'{PATH[:-10]}uniq/uniq_TED.csv', 'w', encoding="utf8") as f:
    f.write("Pattern,Occurrences\n")
    for coll in uniq_corpora[1]:
        f.write(coll[0] + ',' + str(coll[1]) + '\n')

with open(f'{PATH[:-10]}uniq/uniq_UN.csv', 'w', encoding="utf8") as f:
    f.write("Pattern,Occurrences\n")
    for coll in uniq_corpora[2]:
        f.write(coll[0] + ',' + str(coll[1]) + '\n')

with open(f'{PATH[:-10]}uniq/uniq_WM.csv', 'w', encoding="utf8") as f:
    f.write("Pattern,Occurrences\n")
    for coll in uniq_corpora[3]:
        f.write(coll[0] + ',' + str(coll[1]) + '\n')
