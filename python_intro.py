if 3 > 2:
    print('It works!')

if 5 > 2:
    print('5 is indeed greater than 2')
else:
    print('5 is not greater than 2')

name = 'Sonja'
if name == 'Ola':
    print('Hey Ola!')
elif name == 'Sonja':
    print('Hey Sonja!')
else:
    print('Hey anonymous!')

# Change the volume if it's too loud or too quiet
volume = 10
if volume < 20 or volume > 80:
    volume = 50
    print("That's better!")

def hi():
    print('Hi there!')
    print('How are you?')

hi()

def greeting(name):
    if name == 'Ola':
        print('Hi Ola!')
    elif name == 'Sonja':
        print('Hi Sonja!')
    else:
        print('Hi ' + name + '!')

greeting("Jackie")

girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']

def sayhi(name):
    print('Hi ' + name + '!')

for name in girls:
    sayhi(name)
    print('Next girl')

for i in range(1, 6):
    print(i)