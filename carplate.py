import random
import string
import time

def plateWChecksum():

    print('Welcome to car plate generator.')
    platelist = []

    all_alphabets = list(string.ascii_uppercase)
    all_alphabets.remove('O')
    all_alphabets.remove('I')
    edited_alphabets = all_alphabets
    edited_alphabets.remove('Y')
    edited_alphabets
    edited_no_y = edited_alphabets

    first_letter = 'S'
    second_letter = random.choice(['B','C','D','F',
                                    'G','J','K','L'])
    if second_letter == 'L' or second_letter == 'K':
        third_letter = random.choice(edited_no_y)
    else:
        third_letter = random.choice(edited_alphabets)

    digits = random.randint(1,9999)

    plate = first_letter + second_letter + third_letter + ' ' + str(digits)

    alphabets, plate_numbers = plate.split()

    numbers = []
    for ab in alphabets:
        number = ord(ab) - 64
        numbers.append(number)

    if len(numbers) == 3:
        numbers.pop(0)

    elif len(numbers) == 1:
        numbers.insert(0,0)

    plate_num_list = list(map(int, plate_numbers))
    numbers.extend(plate_num_list)

    numbers = [x * (9*4*5*4*3*2) for x in numbers]
    total = sum(numbers)
    remainder = total % 19

    checksumList = ['A', 'Z', 'Y', 'X', 'U', 'T', 'S', 'R', 'P', 'M', 'L', 'K', 'J', 'H', 'G', 'E', 'D', 'C', 'B']
    plate = plate + ' ' + checksumList[remainder]

    print(plate)
    time.sleep(3)
    return plate

plateWChecksum()
