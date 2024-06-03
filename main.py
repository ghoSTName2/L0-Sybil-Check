
my_list = []

with open('initialList.txt', 'r') as file:
    content = file.read()
    lines = content.split('\n')
    for line in lines:
        my_list.append(line)

my_set = set(my_list)  # перетворення списку на множину
element_to_find = '0x8a2eb64b985acac92a726a8b17d9803339e4c04a'  # елемент, який шукаєте

if element_to_find in my_set:
    print("Елемент знайдено")
else:
    print("Елемент не знайдено")
