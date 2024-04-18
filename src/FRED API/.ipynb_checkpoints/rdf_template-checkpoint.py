import fredlib
text = ['There is a cat on the mat', 'It is beautiful Sunday']

for sentence in text:
    g = fredlib.getFredGraph(sentence, 'dccde82f-f4e1-3021-811b-bd08eb420aa6', str(text.index(sentence))+'output.html')
    print (g)
