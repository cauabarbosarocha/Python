# isinstance - para saber se o obejeto é de determinado tipo
lista = [
    'JI', 3, 3.6, True, [0, 1, 3], (9, 0),
    {0,1}, {'nome': 'Heloisa'}
]

for item in lista:
    if isinstance(item, set):
        item.add(5)
        print('SET')
        print(item, isinstance(item, set))
    elif isinstance(item, str):
        print('STR')
        print(item.lower())
    elif isinstance(item, (int, float)):
        print('NUM')
        print(item * 98)
    else:
        print('OUTROS')
        print(item)
