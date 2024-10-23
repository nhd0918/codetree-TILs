# mathValue, engValue 
mathValueA, engValueA = map(int, input().split())
mathValueB, engValueB = map(int, input().split())


if mathValueA > mathValueB:
    print('A')
elif mathValueA < mathValueB:
    print('B')
elif mathValueA == mathValueB:
    if engValueA > engValueB:
        print('A')
    elif engValueA < engValueB:
        print('B')