sentence = (input("Enter a sentence: "))

ifnot = sentence.find('not')
ifpoor = sentence.find('poor')
good = len("good")


if ifpoor > ifnot and ifnot > 0:
    new_sentence = sentence.replace("not", "good")
    length = ifnot + good
    print(new_sentence[0:length])
else:
    print(sentence)