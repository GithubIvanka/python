

def single_root_words(root_word, *other_words):
    root_word = root_word.lower()
    some_words = []
    for i in range(len(other_words)):
        word = str(other_words[i]).lower()
        if word.find(root_word) != -1 or root_word.find(word) != -1:
            some_words.append(other_words[i])
    return some_words



result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(result1)
print(result2)