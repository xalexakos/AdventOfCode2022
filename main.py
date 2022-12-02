from helper.parse_data import ParseData
from day2.solution import *

if __name__ == '__main__':
    input_data = ParseData('day2/input_data.txt').read()
    print(calculate_solution(input_data, PROBLEM_1_POINTS))
    print(calculate_solution(input_data, PROBLEM_2_POINTS))
