# Напишите функцию (F): на вход список имен и целое число N; на выходе список длины N случайных имен из первого списка
# (могут повторяться, можно взять значения: количество имен 20, N = 100, рекомендуется использовать функцию random);

from random import choices


def list_name(names, N):

    return choices(names, k=N)


result_list = list_name(
    ['Ольга', 'Катерина', 'Лилия', 'Алсу', 'Эльвира', 'Александра', 'Мирослава', 'Раиля', 'Венера', 'Галия', 'Анжелика',
     'Рамиля', 'Алина', 'Жанна', 'Елена', 'Клава', 'Вероника', 'Олеся', 'Ирина', 'Татьяна','Эльвира'], 100)

print(result_list)

#2. Напишите функцию вывода самого частого имени из списка на выходе функции F;
names=['Ольга', 'Катерина', 'Лилия', 'Алсу', 'Эльвира', 'Александра', 'Мирослава', 'Раиля', 'Венера', 'Галия', 'Анжелика',
     'Рамиля', 'Алина', 'Жанна', 'Елена', 'Клава', 'Вероника', 'Олеся', 'Ирина', 'Татьяна','Эльвира']
def frequent_name(list_f):
    text_dict = {}
    for b in list_f:
        text_dict[b] = list_f.count(b)
    print(text_dict)
    list_f1 = list(text_dict.items())
    list_f1.sort(key=lambda i: i[1])
    print(list_f1)
    list_f1.reverse()
    return print(list_f1[:1])
frequent_name(names)


#Напишите функцию вывода самой редкой буквы, с которого начинаются имена в списке на выходе функции F.



letters = []
for word in names:
    letters+= word[0]
print(letters)
letters_dict = {}

for let in letters:
    letters_dict[let] = letters.count(let)
letters_dict1= list(letters_dict.items())
letters_dict1.sort(key=lambda i: i[1])
a= int(list(letters_dict1)[0][1])
new_dict = {}
for key, value in letters_dict.items():
    if value <= a:
     new_dict[key] = value

print(list(new_dict))


