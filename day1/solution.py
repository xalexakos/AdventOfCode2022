def calculate_solution(input_data, max_number_count=1):
    max_calories = []
    current_calories = 0

    for index, calories in enumerate(input_data):
        if calories == '':
            max_calories.append(current_calories)
            current_calories = 0
        else:
            current_calories += int(calories)

        if index == len(input_data) - 1:
            max_calories.append(current_calories)

    return sum(sorted(max_calories, reverse=True)[:max_number_count])
