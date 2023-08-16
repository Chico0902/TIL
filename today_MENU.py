import random

Dinner_list = ['커리', '똠양꿍', '라멘', '초밥']
Dinner_list.extend(["회덮밥", "김치돈카츠나베"])
Dinner_list.remove('똠양꿍')
Today_Menu = random.choice(Dinner_list)

print(Today_Menu)