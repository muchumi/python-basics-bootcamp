handle = open('details.txt')
for sentence in handle:
    sentence = sentence.rstrip()
    if sentence.startswith('Information Technology'):
        print(sentence)
   