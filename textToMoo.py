def letter_converter(y):
    for i in range(0, len(sentence[y])):
        for x in range(0, ord(word[i])):
            print("MoO", end='');
        print('Moo'+'moO', end='');


sentence = input("enter your words to moo\n").split()
for j in range(0, len(sentence)):
    word = sentence[j];
    letter_converter(j);
    print('MoO' * 32, end='');
    print('Moo' + 'moO', end='');
