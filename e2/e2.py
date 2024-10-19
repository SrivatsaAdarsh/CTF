import random

def get_base_flag_part(index):
    if index == 0:
        return 'f' if random.choice([True, False]) else 'F'
    elif index == 1:
        return 'l' if random.randint(0, 1) == 0 else 'L'
    elif index == 2:
        if random.choice([True, False]):
            return 'a'
        else:
            return chr(ord('a') + random.randint(0, 1))
    elif index == 3:
        return 'g' if index % 2 == 0 else 'G'

    if index == (4 * 4) // 4:  # Simplified version of 4
        return "no"[1]
    
    elif index == (1 + (6 * 2) / 3):  # index == 5
        return 'q' if random.choice([True, False]) else 'w'

    elif index == (5 + (3 - 2)):  # Simplified version of index == 6
        choice = random.choice([1, 3])
        if choice == 1:
            return chr(((ord('3') * 2) // 3) + 1)  # Returns '#'
        else:
            return chr(((ord('2') * 2) // 2) + 2)  # Returns '4'

    elif index == (7 * (2 // 2)):  # Overcomplicated check for index == 7
        if ((index) * 2 - 2) % 4 == 0:  # Obfuscated check
            return str((int('10') // 10) + 0)  # Returns '1'
        else:
            return str((int('10') // 10) + 1)  # Returns '2'

    elif index == (2 ** 3):  # Index = 8
        return chr((ord('4') * 2) + 4)  # Returns 'l'

    elif index == (3 ** 3 // 3):  # index == 9
        choice = random.choice([1, 0])
        if choice == 0:
            return chr(((ord('6') * 2) + 6) - 2)  # Return 'p'
        else:
            return chr(((ord('5') * 2) + 3))  # Return 'm'

    elif index == ((10 ** 2) // 10):  # index == 10
        return chr(113)  # Returns 'q'

    else:
        return sum([pow(2, 3), abs(-8), len("hi")]) - 10