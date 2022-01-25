import random

name = input("What\'s your name: ")
question = input('Please ask a yes or no question: ')
answer = ''
rng = random.randint(1, 10)

if name != '':
    print(name + ' asks the question: ' + question)
else:
    print('Question: '+question)

#print(rng)
if question == '':
    print('Magic 8 balls need a question to work')
else:
    if rng == 1:
        answer = 'Yes - definately.'
    elif rng == 2:
        answer = 'It is decidedly so.'
    elif rng == 3:
        answer = 'Without a doubt.'
    elif rng == 4:
        answer = 'Reply hazy, try again.'
    elif rng == 5:
        answer = 'Ask again later.'
    elif rng == 6:
        answer = 'Better not tell you now.'
    elif rng == 7:
        answer = 'My sources say no.'
    elif rng == 8:
        answer = 'Outlook not so good.'
    elif rng == 9:
        answer = 'Very doubtful.'
    elif rng == 10:
        answer = 'Nope.'
    else:
        print('error')
    print('Magic 8-Ball\'s answer: [' +answer+']')


