def is_subset(array_1, array_2):
    return set(array_1).issubset(set(array_2)) or set(array_2).issubset(set(array_1))


def overlaps(array_1, array_2):
    return max(array_1.start, array_2.start) < min(array_1.stop, array_2.stop)


def get_range(array):
    r = []
    for i, s in enumerate(array):
        r.append(int(s) if i == 0 else int(s) + 1)
    return range(*r)


def calculate_solution(input_data, calc_func):
    solution = 0
    for tasks in input_data:
        sections = tasks.split(',')
        task_range = [s.split('-') for s in sections]
        if calc_func(get_range(task_range[0]), get_range(task_range[1])):
            solution += 1

    return solution
