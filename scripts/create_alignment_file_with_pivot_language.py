alignments_fr_en_wm = "../alignments/fr_en/WM.alignments.fr-en.txt"
alignments_en_ar_wm = "../alignments/en_ar/WM.alignments.en-ar.txt"
destination_folder = "../alignments/fr_ar/"

test_fr_en = open(alignments_fr_en_wm).readline().rstrip()
test_en_ar = open(alignments_en_ar_wm).readline().rstrip()


# Lire les fichiers ligne par ligne
# Split à la virgule pour avoir une liste d'alignements
# Chaque alignement, le comparer à tous les alignements de la 2e liste
# Si pas de match, on drop
# Si match, on récupère l'id du token fr et la forme et le score
# ainsi que l'id du token ar et la forme
# dans le même format {id_fr form_fr={id_ar form_ar=score}


def split_alignments_at_comma(xalign):
    """
    Splits alignment at comma
    :param xalign:
    :return: list
    """
    temp = xalign.split(", ")
    temp.pop(0)
    return temp


def get_second_language_idform(xalign):
    """
    Retrieves second language token's id and form
    :param xalign:
    :return: list
    """
    temp = xalign.replace("{", "").replace("=", "\t").replace("}", "")
    temp = temp.split("\t")
    token_id = temp[2]
    token_form = temp[3]
    return [token_id, token_form]


def who_said_lists(enriched_align) -> list:
    """
    Transforms enriched alignments in order to have a list of lists of lists...
    :param enriched_align: Enriched alignments
    :return: List of lists of lists of enriched alignments
    """
    new_align = list()
    temp = list()

    i = 1
    for align in enriched_align:
        if int(align[0]) == i:
            temp.append(align)
        else:
            i += 1
            new_align.append(temp)
            temp = list()
            temp.append(align)
    new_align.append(temp)

    return new_align


def get_first_language_idform(xalign):
    """
    Retrieves first (pivot) language token's id and form
    :param xalign:
    :return: list
    """
    temp = xalign.replace("{", "").replace("=", "\t").replace("}", "")
    temp = temp.split("\t")
    token_id = temp[0]
    token_form = temp[1]
    return [token_id, token_form]


def retransform_alignment(xalign):
    """
    Transforms alignement back to their original form, with new elements
    :param xalign:
    :return:
    """
    # goal: {idfr\tformfr={idar\tformar=1.0}
    # actual: ['25544', '26', 'quitter', '25', 'ترك']
    return "{}\t{}={{{}\t{}=1.0}}".format(xalign[1],
                                          xalign[2],
                                          xalign[3],
                                          xalign[4],)


def compare_alignments(file1, file2, file3):
    alignments_file1 = list()
    lst_of_lst_file1 = list()
    alignments_file2 = list()
    lst_of_lst_file2 = list()

    # On récupère tous les alignements
    with open(file1, "r", encoding="utf8") as f, \
         open(file2, "r", encoding="utf8") as g:
        for line in f:
            line = line.rstrip()
            alignments_file1.append(line)
        for line in g:
            line = line.rstrip()
            alignments_file2.append(line)

    # On les transforme en liste de liste
    for alignment in alignments_file1:
        lst_of_lst_file1.append(split_alignments_at_comma(alignment))

    for alignment in alignments_file2:
        lst_of_lst_file2.append(split_alignments_at_comma(alignment))

    fr_ar_alignments = list()
    # lst_of_lst_file1.pop(-1) when lengths are different

    # On compare chaque élément de la liste 1 avec tous les éléments de la
    # liste 2 pour pouvoir récupérer les alignements où l'anglais est commun
    for i in range(len(lst_of_lst_file1)):
        for alignment1 in lst_of_lst_file1[i]:
            en_id_form1 = get_first_language_idform(alignment1)
            for alignment2 in lst_of_lst_file2[i]:
                en_id_form2 = get_first_language_idform(alignment2)
                if en_id_form1 == en_id_form2:
                    fr_id_form = get_second_language_idform(alignment1)
                    ar_id_form = get_second_language_idform(alignment2)
                    new_align = fr_id_form + ar_id_form
                    new_align.insert(0, str(i + 1))
                    fr_ar_alignments.append(new_align)

    # à partir d'ici, on a une liste de listes avec
    # [id_phrase, id_fr, form_fr, id_ar, form_ar]

    new_fr_ar_alignments = who_said_lists(fr_ar_alignments)

    # with open(file3, "w", encoding="utf8") as f:
    #     # on transforme les alignements
    #     for j in range(len(lst_of_lst_file1)):
    #         # penser à remove le premier \n du fichier"
    #         f.write(f"\n{j+1}\t")
    #         if j % 1000 == 0:
    #             print("Line :: ", j)
    #         for align in fr_ar_alignments:
    #             if align[0] == str(j + 1):
    #                 xformed = retransform_alignment(align)
    #                 f.write(xformed + ", ")
    #                 fr_ar_alignments.pop(fr_ar_alignments.index(align))
    #             else:
    #                 pass
    #         j += 1

    with open(file3, "w", encoding="utf8") as f:
        for j in range(len(lst_of_lst_file1)):
            f.write(f"\n{j + 1}\t")
            if j % 1000 == 0:
                print("Line :: ", j)
            for al in new_fr_ar_alignments[j]:
                if len(al) > 1:
                    if al[0] == str(j + 1):
                        xformed = retransform_alignment(al)
                        f.write(xformed + ", ")
                else:
                    pass
            j += 1


compare_alignments(alignments_fr_en_wm, alignments_en_ar_wm,
                   destination_folder+"WM.alignments.fr-ar.txt")


