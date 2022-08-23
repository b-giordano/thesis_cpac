import string

files = [
    # FR
    "/home/bastieng/cpac/annotation/gold/annotation.gold.GV.fr.cupt",
    "/home/bastieng/cpac/annotation/gold/annotation.gold.TED.fr.cupt",
    "/home/bastieng/cpac/annotation/gold/annotation.gold.UN.fr.cupt",
    "/home/bastieng/cpac/annotation/gold/annotation.gold.WM.fr.cupt",
    "/home/bastieng/cpac/annotation/gold/annotation.gold.fr.cupt",
    # EN
    "/home/bastieng/cpac/annotation/projection_en/gold/projection.gold.GV.en.cupt",
    "/home/bastieng/cpac/annotation/projection_en/gold/projection.gold.TED.en.cupt",
    "/home/bastieng/cpac/annotation/projection_en/gold/projection.gold.UN.en.cupt",
    "/home/bastieng/cpac/annotation/projection_en/gold/projection.gold.WM.en.cupt",
    "/home/bastieng/cpac/annotation/projection_en/gold/projection.gold.en.cupt",
    # AR
    "/home/bastieng/cpac/annotation/projection_ar/gold/doubleprojection.gold.GV.ar.cupt",
    "/home/bastieng/cpac/annotation/projection_ar/gold/doubleprojection.gold.TED.ar.cupt",
    "/home/bastieng/cpac/annotation/projection_ar/gold/doubleprojection.gold.UN.ar.cupt",
    "/home/bastieng/cpac/annotation/projection_ar/gold/doubleprojection.gold.WM.ar.cupt",
    "/home/bastieng/cpac/annotation/projection_ar/gold/doubleprojection.gold.ar.cupt"
]


def compute_average(xlist):
    return sum(xlist) / len(xlist)


def get_conll_sentences_annotations(xfile):
    conll_sentences = list()

    with open(xfile, "r", encoding="utf8") as f:
        lines = list()
        for i, line in enumerate(f):
            line = line.rstrip()
            if len(line) > 1 and line[0] in string.digits:
                if line[-1] != "*":
                    tabs = line.split("\t")
                    idx = tabs[0]
                    annot = tabs[10]
                    pos = tabs[3]
                    if pos != "ADP" and pos != "PRON":
                        lines.append((idx, annot))
                    else:
                        if len(lines) > 1:
                            new_idx = str(int(lines[-1][0]) - 1)
                            old_annot = lines[-1][1]
                            lines.pop(-1)
                            lines.append((new_idx, old_annot))
            else:
                if len(lines) > 0:
                    lines = [lines]
                    conll_sentences.append(lines)
                    lines.clear()

    return conll_sentences


def split_common_annot(xline):
    for elem in xline:
        if ";" in elem[1]:
            common = elem[1].split(";")
            for i in range(len(common)):
                xline.insert(xline.index(elem), (elem[0], common[i]))
            xline.pop(xline.index(elem))

    return xline


def get_max_n(xlist):
    max_n = 0
    for elem in xlist:
        if int(elem[1][0]) > max_n:
            max_n = int(elem[1][0])

    return max_n


def count_diff(xlist):
    maxn = get_max_n(xlist)
    differences = list()
    indexes = list()

    for i in range(maxn + 1):
        for elem in xlist:
            if int(elem[1][0]) == i + 1:
                indice = int(elem[0])
                indexes.append(indice)
                if len(indexes) == 2:
                    diff = indexes[1] - indexes[0]
                    differences.append(diff)
                    indexes.clear()

    return differences


def sort_list(tup):
    # reverse = None (Sorts in Ascending order)
    # key is set to sort using second element of
    # sublist lambda has been used
    tup.sort(key=lambda x: x[1][0])
    return tup


def get_min_max_avg_med_dist(xlist):
    min_dist = 999
    max_dist = 0

    for elem in xlist:
        if elem < min_dist:
            min_dist = elem
        if elem > max_dist:
            max_dist = elem

    avg_dist = round(sum(xlist) / len(xlist), 2)
    med_dist = sorted(xlist)[int((len(xlist) + 1) / 2)]

    return min_dist, max_dist, avg_dist, med_dist


def get_stats(xlist):
    occurrence = map(lambda occ: (occ, xlist.count(occ)), set(xlist))

    return [(item[0], item[1]) for item in occurrence]


if __name__ == "__main__":
    for file in files:
        diffs = list()
        conll = get_conll_sentences_annotations(file)
        annots = [sort_list(split_common_annot(c)) for c in conll[:-1]]

        for annot in annots:
            d = count_diff(annot)
            for di in d:
                diffs.append(di)

        print("***\n{}".format(file.split("/")[-1]))
        print(get_min_max_avg_med_dist(diffs))
        print(get_stats(diffs))
        print("***\n")