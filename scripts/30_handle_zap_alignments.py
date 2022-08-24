import sys
from datetime import datetime
import re
import string


def reformat_zap_alignments(alignments) -> list:
    """
    Reformats ZAP alignments in order to obtain temporary annotation-less
    alignments following this format:
    [[id_sentence, id_token_en, form_token_en, id_token_fr, form_token_fr,
    score], ...]
    :param alignments: ZAP format alignments
    :return: reformatted alignments
    """
    reformatted_alignments = alignments.replace(",", "").replace("{", "") \
        .replace("}", "").replace("\t", ",").replace("=", ",").split(" ")
    reformatted_alignments = [x.split(",") for x in reformatted_alignments]
    id_phrase = reformatted_alignments[0][0]
    reformatted_alignments[0].pop(0)
    for elem in reformatted_alignments:
        elem.insert(0, id_phrase)
    return reformatted_alignments


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


def get_and_transform_alignments_from_file(zap_file) -> list:
    """
    Reads and reformat ZAP alignments from file
    :param zap_file: ZAP file with alignments
    :return: list of reformatted alignments
    """
    reformatted_alignments = list()
    with open(zap_file, 'r', encoding='utf8') as f:
        for line in f:
            line = line.rstrip()
            reformatted_alignment = reformat_zap_alignments(line)
            reformatted_alignments.append(reformatted_alignment)

    return reformatted_alignments


def get_sentence_idtoken_form(reformatted_alignment, lang) -> list:
    """
    Returns a triple with the sentence's id, the token's id, and the
    token's form for a given alignment
    :param reformatted_alignment: List of lists with alignments
    :param lang: French or English
    :return: List with 3 pieces of info
    """
    if len(reformatted_alignment) == 2:  # ['id_phrase', 'EMPTY']
        pass
    else:
        triple = list()
        sentence = reformatted_alignment[0]
        triple.append(sentence)
        if lang == "ar":
            id_token = reformatted_alignment[3]
            form = reformatted_alignment[4]
            triple.append(id_token)
            triple.append(form)
        elif lang == "fr":
            id_token = reformatted_alignment[1]
            form = reformatted_alignment[2]
            triple.append(id_token)
            triple.append(form)
        return triple


def enrich_alignments_with_annotation(gold_file,
                                      reformatted_alignments) -> list:
    """
    Enrich alignments with gold annotation from source corpus
    :param gold_file: source gold annotated corpus
    :param reformatted_alignments: reformatted alignments
    :return: new list of enriched alignments
    """
    enriched_alignments = list()
    # Lecture du fichier
    with open(gold_file, 'r', encoding='utf8') as f:
        for line in f:
            line = line.rstrip()
            if line.startswith("# global.columns") \
                    or line.startswith("# text") \
                    or len(line) < 1:
                continue
            # Récupération de l'id de la phrase
            elif line.startswith("# source"):
                pattern = re.search("::\\d+", line)
                match = pattern.group()
                id_phrase = match[2:]
            # Pour les lignes commençant par un numéro (tokens)
            elif line[0] in string.digits:
                tabs = line.split("\t")
                id_token = tabs[0]
                form_token = tabs[1]
                annotation = tabs[10]
                # if annotation == "*":
                #     continue
                # else:
                # On récupère le triple gold si annotation présente
                triple_gold = [id_phrase, id_token, form_token]
                # On compare avec les triples dans les alignements
                # correspondants à l'id de la phrase
                for alignment in reformatted_alignments[
                    int(id_phrase) - 1]:
                    triple_alignment = get_sentence_idtoken_form(alignment,
                                                                 "fr")
                    # Si ça matche, on enrichit l'alignement et on l'ajoute
                    # à notre liste d'alignements enrichis (on ne conserve
                    # que ceux-là
                    if triple_alignment == triple_gold:
                        enriched = alignment
                        enriched.append(annotation)
                        enriched_alignments.append(enriched)

    # On asserte que tous les alignements sont bel et bien enrichis (len == 7)
    # Inutile de faire ça, rend les choses plus compliquées pour itérer sur
    # le texte anglais avec les id des phrases où il n'y a pas d'annotations
    # remove_alignment_without_annotation(enriched_alignments)

    modified_and_enriched = who_said_lists(enriched_alignments)
    print(f"Length of enriched alignments: {len(modified_and_enriched)}")
    # print(modified_and_enriched)
    return modified_and_enriched


def enrich_target_corpus(empty_corpus, out_corpus, enriched_align):
    """
        Takes enriched alignments as input, compares with empty CUPT file,
        and project annotations in a new CUPT file
        :param empty_corpus: empty CUPT file
        :param out_corpus: new target CUPT file
        :param enriched_align: enriched alignments
        :return:
        """
    print("Started enriching target corpus...")
    enriched_aligns = enriched_align
    with open(empty_corpus, 'r', encoding='utf8') as f, \
            open(out_corpus, 'w', encoding='utf8') as g:
        for line in f:
            line = line.rstrip()
            if line.startswith("# global.columns") \
                    or line.startswith("# text") \
                    or len(line) < 1:
                g.write(line + "\n")
            if line.startswith("# source"):
                pattern = re.search("::\\d+", line)
                match = pattern.group()
                id_phrase = match[2:]
                g.write(line + "\n")
                if int(id_phrase) % 2500 == 0:
                    print(f"Currently at line {id_phrase}...")
            if len(line) > 1 and line[0] in string.digits:
                tabs = line.split("\t")
                id_token = tabs[0]
                form_token = tabs[1]
                triple_gold = [id_phrase, id_token, form_token]
                matched = ""
                for alignment in enriched_aligns[int(id_phrase) - 1]:
                    # print(alignment)
                    annotation = alignment[-1]
                    triple_align = get_sentence_idtoken_form(alignment,
                                                             "ar")
                    if triple_gold == triple_align and annotation == "*":
                        matched = line + "\n"
                        # g.write(line + "\n")
                        break
                    elif triple_gold == triple_align and annotation != "*":
                        line = line.replace("\t*", f"\t{annotation}")
                        matched = line + "\n"
                        # g.write(line + "\n")
                        break
                    else:
                        matched = line + "\n"
                g.write(matched)

    print("Finished enriching target corpus!")


def project_annotations(alignments_file,
                        gold_annotations,
                        empty_target_corpus,
                        new_corpus_with_projected_annotations):
    """
    Project annotations from gold annotated file to empty target corpus.
    :param alignments_file: original file with ZAP alignments
    :param gold_annotations: annotated CUPT corpus with gold annotations
    :param empty_target_corpus: empty CUPT target corpus
    :param new_corpus_with_projected_annotations: output corpus with projected
    annotations
    :return:
    """
    # Reformat alignments to work with
    print("Formatting alignments...")
    reformatted_alignments = \
        get_and_transform_alignments_from_file(alignments_file)
    print("Done!")
    # Enrich alignments with annotations from gold file
    print("Enriching alignments...")
    enriched_alignments = enrich_alignments_with_annotation(
        gold_annotations, reformatted_alignments)
    print("Done!")
    # Project annotations into target corpus
    enrich_target_corpus(empty_target_corpus,
                         new_corpus_with_projected_annotations,
                         enriched_alignments)


if __name__ == '__main__':
    tic = datetime.now()
    # PATH = "/home/bastieng/cpac"
    align_file = sys.argv[1]
    gold_annot = sys.argv[2]
    empty_target = sys.argv[3]
    new_target = sys.argv[4]
    project_annotations(align_file,
                        gold_annot,
                        empty_target,
                        new_target)
    tac = datetime.now()
    time_elapsed = tac - tic
    print(time_elapsed)
