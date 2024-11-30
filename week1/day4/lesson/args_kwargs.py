def my_pets(*args):
    print(args)
    total_pets = len(args)
    return total_pets

print(my_pets('cat', 'dog','bird','fish'))


def user_info(**kwargs):
    for keyword in kwargs.keys():
        if keyword == 'address':
            print(f'Nice {keyword}')


user_info(name = 'Juliana', address = 'Ramat Gan', email = 'ju@gmail.com')
