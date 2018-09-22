print('Hello, Django girls!')

if 1>2:
    print('this works')
else:
    print('does not work')


def hi(name):
    print('hi, {}'.format(name))

hi('olympia')

girls = ['Andrea', 'Olympia', 'Kendall', 'Courtney']

for name in girls:
    hi(name)
    print('Next girl')

for i in range(1,6):
    print(i)
