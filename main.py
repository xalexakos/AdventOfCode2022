from helper.parse_data import ParseData
from day3.solution import *

if __name__ == '__main__':
    input_data = ParseData('day3/input_data.txt').read()
    print(calculate_solution(input_data))
    print(calculate_solution_2(input_data))
