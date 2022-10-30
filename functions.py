def print_greeting():
    '''
    print 'Hello!' text
    :return:
    '''
    print('hello!')


print_greeting()
help(print_greeting)


def print_greeting_with_name(name):
    '''
    print 'Hello! , <name>' text
    :return:
    '''
    print('hello, ' + name + '!')


print_greeting_with_name('Vitalii')
help(print_greeting_with_name)


def sums(x=0, y=0):
    '''

    :param x:
    :param y:
    :return: sum of 2 addends
    '''
    return x + y


print(sums(3, 44))
help(sums)


def is_str_in_text(string, text):
    return string.upper() in text.upper()


print(is_str_in_text('hello', 'i said him Hello'))
