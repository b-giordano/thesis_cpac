import sys
import datetime
import string


def conllu2cupt(plain_txt, conll_file, cupt):
    """
    Reads conll file and transforms it into a valid cupt
    file. Replace second-to-last column, adds asterisks
    @ 11th column, adds source_id and text.
    :param plain_txt: Plain text to get source_id and text
    :param conll_file: CoNLL file to transform
    :param cupt: Output cupt file
    """

    x = datetime.datetime.now()
    print(f"\n>>> Beginning: {x.strftime('%c')}")

    with open(plain_txt, 'r', encoding='utf8') as f:
        print(f"\t*** Creating list of sentences ***")
        sents = [line for line in f if len(line) > 1]

    # From CoNLL standard to CoNLL-U cupt input format
    with open(conll_file, 'r', encoding='utf8') as g, \
            open(cupt, 'w', encoding='utf8') as h:

        # Messages for the user
        print(f"\t*** Reading {conll_file} ***")
        print(f"\t*** Adding asterisks in 11th column of {cupt} ***")

        # First line of file
        h.write("# global.columns = ID FORM LEMMA UPOS XPOS FEATS HEAD "
                "DEPREL DEPS MISC PARSEME:MWE\n")

        # These lines both appear before each sentence; here's the 1st
        h.write(f"# source_sent_id = {plain_txt}::1\n")
        i = 0
        h.write(f"# text = {sents[i]}")

        # Writing CoNLL-U file
        # digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        for line in g:
            # Adds a tab and an asterisk at the end of each empty line
            if line[0] in string.digits:
                tabs = line.split('\t')
                line = tabs[0] + '\t' + tabs[1] + '\t' + tabs[2] \
                       + '\t' + tabs[3] + '\t' + tabs[4] + '\t' \
                       + tabs[5] + '\t' + tabs[6] + '\t' + tabs[7] \
                       + '\t' + tabs[8] + '\t_\t*\n'
                h.write(line)
            # Breaks out of the loop when finished
            elif i == len(sents) - 1:
                break
            # Adds empty line + source + sentence text
            else:
                i += 1
                h.write(line)
                h.write(f"# source_sent_id = {plain_txt}::{i + 1}\n")
                h.write(f"# text = {sents[i]}")
                if i % 500 == 0:
                    print(f"\t*** Parsing sentence {i} ***")

    print(f"\n>>> Done writing in {cupt}!")
    y = datetime.datetime.now()
    print(f">>> End: {x.strftime('%c')}")
    z = y - x
    print(f">>> Total duration: {z}.")


if __name__ == '__main__':
    f1 = sys.argv[1]
    f2 = sys.argv[2]
    f3 = sys.argv[3]
    conllu2cupt(f1, f2, f3)
