from helper.parse_data import ParseData
from day4.solution import *

if __name__ == '__main__':
    input_data = ParseData('day4/input_data.txt').read()
    print(calculate_solution(input_data, calc_func=is_subset))
    print(calculate_solution(input_data, calc_func=overlaps))

