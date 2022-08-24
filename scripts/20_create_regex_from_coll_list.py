import sys


def double_split(string):
    """
    Splits a line following this format: play|role,261
    :param string: the line
    :return: the collocation's components
    """
    first_split = string.split(",")
    collocation = first_split[0]
    second_split = collocation.split("|")
    return second_split


def create_regex_from_new_split(split):
    pattern = r"^(\d.+\t(term1)\t.+?\t)(\d(:COLL))$((\n.+?){1,10})(\t(term2)\t.+?\t)(\d)$"
    a = pattern.replace("term1", f"{split[0]}|{split[1]}").replace("term2", f"{split[0]}|{split[1]}")
    a_pattern = pattern.replace("term1", split[0]).replace("term2", split[1])
    b_pattern = pattern.replace("term1", split[1]).replace("term2", split[0])

    # return [a_pattern, b_pattern]
    return a


def create_regex_file_from_file(file_in, file_out):
    with open(file_in, "r", encoding="utf8") as f, \
         open(file_out, "w", encoding="utf8") as g:
        for line in f:
            line = line.rstrip()
            collocation = double_split(line)
            regex = create_regex_from_new_split(collocation)
            # g.write(regex[0] + "\n" + regex[1] + "\n")
            g.write(regex + "\n")


def example_regex_creation(fake_line):
    collocation = double_split(fake_line)
    regex = create_regex_from_new_split(collocation)
    return regex


if __name__ == "__main__":
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    create_regex_file_from_file(file1, file2)
    # example = "play|role,261"
    # res = example_regex_creation(example)
    # print(res)
