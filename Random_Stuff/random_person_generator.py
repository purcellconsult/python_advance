from random import choice

first_names = ['Jack', 'Sally', 'Mike', 'Jennifer', 'Kevin', 'Sue']
last_names = ['Johnson', 'Nguyen', 'Adams', 'Garcia', 'Abera']


def create_names():
    name = '{} {}'.format(choice(first_names), choice(last_names))
    print(name)


create_names()

