# _*_ coding: utf-8 _*_
__author__ = 'Yang Haibo'
__date__ = '2020/6/18 9:48'


def shift_char(c):
    if c.islower():
        return c.upper()
    elif c.isupper():
        return c.lower()
    else:
        return c


def shift_text(t):
    return ''.join([shift_char(c) for c in list(t)])


if __name__ == '__main__':
    import string
    t = string.printable
    print(t)
    r = shift_text(t)
    print(r)
