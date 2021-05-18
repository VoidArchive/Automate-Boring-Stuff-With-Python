
spam = ['apples', 'bananas', 'tofu', 'cats']


def Cooma(a_list):
    return '{0} and {1}'.format(', '.join(a_list[:-1]), a_list[-1])


Cooma(spam[:5])
