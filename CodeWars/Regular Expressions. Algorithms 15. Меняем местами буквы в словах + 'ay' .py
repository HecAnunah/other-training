# Переместите первую букву каждого слова в конце его, затем добавьте «AY» в конце слова.
# Оставьте отметки пунктуации нетронутыми.

# Examples
# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !

def pig_it(text):
    text_list = text.split() #['Pig', 'latin', 'is', 'cool']
    spec_keys = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    changed_lst = []
    for word in text_list:
        if word not in spec_keys:
            change_word = word[1:] + word[0] + 'ay'
            changed_lst.append(change_word)
        else:
            changed_lst.append(word)
    return ' '.join(changed_lst)

# def pig_it(text):
#     lst = text.split()
#     return ' '.join([word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])

# def pig_it(text):
#     return " ".join(x[1:] + x[0] + "ay" if x.isalnum() else x for x in text.split())

text = 'Hello world !'
test = pig_it(text)
print(test)
