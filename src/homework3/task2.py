"""List practice
    1. Используйте генератор списков чтобы получить следующий:
        ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
    2. Используйте на предыдущий список slice чтобы получить следующий:
        ['ab', 'ad', 'bc'].
    3. Используйте генератор списков чтобы получить следующий:
        ['1a', '2a', '3a', '4a'].
    4. Одной строкой удалите элемент '2a' из прошлого списка, напечатайте его.
    5. Скопируйте список и добавьте в него элемент '2a' так,
        чтобы в исходном списке этого элемента не было.
"""


lst1 = [i + k for i in 'ab' for k in 'bcd']
print(lst1)

lst2 = lst1[::2]
print(lst2)

lst3 = [n + m for n in '1234' for m in 'a']
print(lst3)

print(lst3.pop(1))

lst4 = lst3[:]
lst4.insert(1, '2a')
print(lst3, lst4)
