# this program takes all .txt files from my_file list and return column of N sorted most_common words
from collections import Counter
import sys
import os, random


# n - number of words which we want have
def input_number():
    if len(sys.argv) == 2:
        if sys.argv[1].isdigit():
            return int(sys.argv[1])
        else:
            print("wrong number of words")
            exit(1)
    # if no command line argument then type by hand
    else:
        n = input("Please inter number of words N: ")
        if n.isdigit():
            return int(n)
        else:
            print("wrong number of words")
            exit(1)


# clear text from big letters and punctuation
def clear_words(text: str) -> object:
    just_words = []
    for word in text.split():
        clear_word = ""
        for letter in word:
            if letter.isalpha():
                clear_word += letter.lower()
        if clear_word == "":
            continue
        else:
            just_words.append(clear_word)
    # print(just_words)
    return just_words


# find files.txt in folder
def make_long_pure_text():
    word_list = []
    my_files = filter(lambda x: x.endswith('.txt'), os.listdir(str(os.getcwd()) + '/output/'))
    # open txt file
    for i in my_files:
        # rand = str(random.randint(0, 10000))
        # in case i want to randomly rename file, but i don't need it here
        # os.rename('/home/misha/PycharmProjects/Words/output/' + str(i), '/home/misha/PycharmProjects/Words/output/' + rand + '.txt')
        # very nice solving encoder utf8 problem
        with open(str(os.getcwd()) + '/output/' + str(i), encoding='utf8', errors='ignore') as f:
            # make string from whole text
            fst = str(f.read())
            word_list.extend(clear_words(fst))
    return word_list


# without converting to dict
# my_count = Counter(word_list).most_common(input_number())
# def result():
#     for i in range(len(my_count)):
#         print(my_count[i][0], my_count[i][1])


def result_dic_and_print(N):
    mydic = dict(Counter(make_long_pure_text()).most_common(N))
    for k, v in mydic.items():
        print(k, v)
    return mydic


# result_dic_and_print(input_number())


# create result folder if not exist
def make_mcw():
    if not os.path.exists(str(os.getcwd()) + '/result'):
        os.mkdir(str(os.getcwd()) + '/result')
    # create new file and upload words
    new = open('/home/misha/PycharmProjects/Words/result/most_common.txt', 'w')
    for key in result_dic_and_print(input_number()).keys():
        new.write(key + '\n')
    new.close()


def main():
    make_mcw()


if __name__ == "__main__":
    main()
