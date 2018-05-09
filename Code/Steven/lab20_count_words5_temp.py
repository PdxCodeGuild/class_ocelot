import string


def open_ebook_file():
    with open('clue_golden_coin.txt', 'r', encoding='utf-8') as f:
        ebook_contents = f.read()  # read the contents
        ebook_contents = ebook_contents.lower()
        ebook_contents = ebook_contents.replace('\n', ' ')

        cont_to_clean = ''
        for char_current in ebook_contents:
            if char_current in (string.ascii_lowercase + ' '):
                cont_to_clean += char_current
        cont_cleaned = cont_to_clean.split()
        print(cont_to_clean)
    return(cont_cleaned)

# def make_word_list():
#     return()

def make_word_pair_list():
    word_pair_list = []
    for i in range(len(c3) - 1):
        word_pair_list.append(c3[i] + ' ' + c3[i + 1])

    word_pair_dict = {}

    for word_pair in word_pair_list:
        if word_pair not in word_pair_dict:
            word_pair_dict[word_pair] = 1
        else:
            word_pair_dict[word_pair] += 1
    return(word_pair_dict)


def show_high_freq_items(d5):
    d5 = list(word_pair_dict.items())
    d5.sort(key=lambda tup: tup[1], reverse=True)
    for i in range(min(10, len(d5))):
        print(d5[i])
    return(d5)



while num_input != '':
    selection_in = int(input('Word freq counter: Enter 1 for single words, 2 for word pairs.\n Hit \'Enter\' again to quit>')

    book_text = open_ebook_file()

    if num_input == 1:
        make_word_pair_list(c3)
        show_most_used_words(d5)
    elif num_input == 2:
        make_word_pair_list(c3)
        show_most_used_words(d5)


    else:
        exit()


# c3 = open_ebook_file()
#
# c3 = open_ebook_file()
#
# c3 = open_ebook_file()

# print(c3)







