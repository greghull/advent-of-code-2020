from itertools import count

# Test Data
card_public_key = 5764801
door_public_key = 17807724

# My Data
card_public_key = 8184785
door_public_key = 5293040

door_loop_size = 0
subject_number = 7
value = 1

for i in count(1):
    value = (value * subject_number) % 20201227
    
    if value == door_public_key:
        door_loop_size = i
        break

print("Door loop size:", door_loop_size)
print("Enc key:", pow(card_public_key, door_loop_size, 20201227))

