from helper.parse_data import ParseData
from day1.solution import calculate_solution

if __name__ == '__main__':
    input_data = ParseData('day1/input_data.txt').read()
    print(calculate_solution(input_data, 1))
    print(calculate_solution(input_data, 3))
