def divide_chunks(elements, n):
    for i in range(0, len(elements), n):
        yield elements[i:i + n]


def char_to_number(character):
    return ord(character) - (96 if character.islower() else 38)


def calculate_solution(input_data):
    priority_sum = 0
    for rs in input_data:
        first_part, second_part = rs[:len(rs)//2], rs[len(rs)//2:]
        common = ''.join(set(first_part).intersection(second_part))
        priority_sum += char_to_number(common)

    return priority_sum


def calculate_solution_2(input_data):
    priority_sum = 0
    for rs in divide_chunks(input_data, 3):
        common = ''.join(set.intersection(*map(set, rs)))
        priority_sum += char_to_number(common)

    return priority_sum
