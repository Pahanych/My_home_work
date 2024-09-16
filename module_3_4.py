def single_root_words(root_word, *other_words):
    same_words = []
    root_word_1 = root_word.lower()
    for j in other_words:
        other_words_1 = j.lower()
        if root_word_1 in other_words_1 or other_words_1 in root_word_1:
            same_words.append(j)
    print(same_words)




single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
