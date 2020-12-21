def read(filename):
    data = []
    with open(filename) as f:
        lines = f.read().split('\n')

    for line in lines:
        halves = line.split(' (contains ')
        halves[0] = set(halves[0].split(' '))
        if len(halves) > 1:
            halves[1] = set(halves[1].rstrip(')').split(', '))
        else:
            halves[1] = set()
        data.append(halves)

    return data

data = read("input/input21.txt")

all_ingredients = set()
all_allergens = set()
food_map = {}
for d in data:
    all_ingredients |= d[0]
    all_allergens |= d[1]

for allergen in all_allergens:
    food_map[allergen] = all_ingredients.copy()

for d in data:
    for allergen in d[1]:
        food_map[allergen] &= d[0]

inert_ingredients = all_ingredients.copy()

for allergen, ingredients in food_map.items():
    inert_ingredients.difference_update(ingredients)

## Part 1 Answer
print(sum([len(d[0] & inert_ingredients) for d in data]))

for i in range(4):
    for allergen, ingredients in food_map.items():
        for allergen2, ingredients2 in food_map.items():
            if allergen != allergen2 and len(ingredients2) == 1:
                ingredients.difference_update(ingredients2)


keys = list(food_map.keys())
keys.sort()
print(keys)
## Part 2 Answer
print(",".join([food_map[key].copy().pop() for key in keys]))