import sys
import os
import datetime
import stanza
from stanza.utils.conll import CoNLL


def add_linebreak(plain_txt):
    """
    Adds a line break to avoid weird segmentation by stanza.
    :param plain_txt: Plain text source corpus
    """
    with open(plain_txt, 'r', encoding='utf8') as f, \
            open(f'dub_{plain_txt}', 'w', encoding='utf8') as g:
        for line in f:
            line = line + '\n'
            g.write(line)


def plaincorpus2conll(lang, plain_txt, conll_file):
    """
    Takes a plain corpus in a given language and transforms it into
    a CoNLL file.
    :param lang: Language (fr, en, ar)
    :param plain_txt: Plain text source corpus
    :param conll_file: Output CoNLL file
    """
    PATH = '/home/bastieng/cpac/tri_texts/'
    x = datetime.datetime.now()
    # From plain corpus to CoNLL standard format
    # tokenize_no_ssplit doesn't split sentences automatically
    # but rather keeps the original segmentation.
    # However, double \n\n are mandatory in original file
    nlp = stanza.Pipeline(lang=lang.lower(),
                          tokenize_no_ssplit=True)
    print(f"\n>>> Beginning: {x.strftime('%c')}\n")
    # plain_txt = mieux si c'est un texte tokénisé, NOPE, mauvaise idée
    with open(f'{plain_txt}', 'r', encoding='utf8') as f:
        print(f"\t*** [{lang.upper()}] Reading {plain_txt} ***")
        filenames = []
        for i, line in enumerate(f):
            # if i < 23976:
            #     continue
            # Trouver une soluce pour WM (23k déjà fait)
            doc = nlp(line.rstrip())
            CoNLL.write_doc2conll(doc, f'{i + 1}_{conll_file}')
            filenames.append(f'{i + 1}_{conll_file}')

        print(f"\t*** Merging all files into {conll_file} ***")
        with open(conll_file, 'w', encoding='utf8') as e:
            for fn in filenames:
                with open(fn, 'r', encoding='utf8') as g:
                    content = g.read()
                    content = content.replace('\n\n\n', '\n')
                    e.write(content)
                os.remove(PATH + fn)

    # os.remove(PATH + f'dub_{plain_txt}')

    print(f"\n>>> Done writing in {conll_file}!")
    y = datetime.datetime.now()
    print(f">>> End: {x.strftime('%c')}")
    z = y - x
    print(f">>> Total duration: {z}.")


if __name__ == '__main__':
    lg = sys.argv[1]
    f1 = sys.argv[2]
    f2 = sys.argv[3]
    # add_linebreak(f1)
    plaincorpus2conll(lg, f1, f2)
