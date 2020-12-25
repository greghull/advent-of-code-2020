# Test Data
card_public_key = 5764801
door_public_key = 17807724

# My Data
card_public_key = 8184785
door_public_key = 5293040

def transform(subject_number, loop_size):
    value = 1
    for _ in range(loop_size):
        value *= subject_number
        value = value % 20201227

    return value

card_loop_size = 0
door_loop_size = 0

subject_number = 7
value = 1
loop_size = 1

while card_loop_size == 0 or door_loop_size == 0:
    value *= subject_number
    value = value % 20201227

    if value == card_public_key:
        card_loop_size = loop_size

    if value == door_public_key:
        door_loop_size = loop_size

    loop_size += 1

print("Card loop size:", card_loop_size)
print("Door loop size:", door_loop_size)
print("Enc key:", transform(card_public_key, door_loop_size))
print("Enc key:", transform(door_public_key, card_loop_size))

