def parse_line(line):
    halves = line.split(' (contains ')
    halves[0] = set(halves[0].split(' '))
    if len(halves) > 1:
        halves[1] = set(halves[1].rstrip(')').split(', '))
    else:
        halves[1] = set()
    return halves

with open("input/input21.txt") as f:
    data =  [parse_line(line) for line in f.read().split('\n')]

all_ingredients = set()     # All possible ingredients
all_allergens = set()       # All possible allergens
food_map = {}               # A Map from allergens to possibly related ingredients

for d in data:
    all_ingredients |= d[0]
    all_allergens |= d[1]

for allergen in all_allergens:
    food_map[allergen] = all_ingredients.copy()

for d in data:
    for allergen in d[1]:
        food_map[allergen] &= d[0]

inert_ingredients = all_ingredients.copy()  # set of ingredients with no allergens
for allergen, ingredients in food_map.items():
    inert_ingredients.difference_update(ingredients)

## Part 1 Answer
print("P1:", sum([len(d[0] & inert_ingredients) for d in data]))

for i in range(4):
    for allergen, ingredients in food_map.items():
        for allergen2, ingredients2 in food_map.items():
            if allergen != allergen2 and len(ingredients2) == 1:
                ingredients.difference_update(ingredients2)

## Part 2 Answer
keys = sorted(food_map.keys())
print("P2:", ",".join([food_map[key].copy().pop() for key in keys]))