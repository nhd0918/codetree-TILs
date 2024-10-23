# mathValue, engValue 
mathValueA, engValueA = map(int, input().split())
mathValueB, engValueB = map(int, input().split())

print('A' if (mathValueA > mathValueB) or (mathValueA == mathValueB and engValueA > engValueB) else 'B')