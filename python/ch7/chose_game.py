"""
chose which game
"""


def chose(p):
    p = float(p)
    game1 = p
    game2 = 3 * p ** 2 * (1 - p) + p ** 3
    if game1 < game2:
        return '2'
    else:
        return '1'


def main():
    print chose(.1)
    print chose(.5)
    print chose(.6)
    print chose(.9)


if __name__ == '__main__':
    main()
