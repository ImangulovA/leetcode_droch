s1 = 0
s2 = 0

prod = True

import numpy as np
import re
from pulp import LpProblem, LpMinimize, LpVariable, lpSum, value, LpStatus
from itertools import islice

def group_strings(lst, n=4):
    return [lst[i:i+n] for i in range(0, len(lst), n)]

def extract_values(input_text):
    # Define regex patterns for extracting values
    button_a_pattern = r"Button A: X\+(\d+), Y\+(\d+)"
    button_b_pattern = r"Button B: X\+(\d+), Y\+(\d+)"
    prize_pattern = r"Prize: X=(\d+), Y=(\d+)"

    # Extract values using regex
    button_a_match = re.search(button_a_pattern, input_text)
    button_b_match = re.search(button_b_pattern, input_text)
    prize_match = re.search(prize_pattern, input_text)

    if not (button_a_match and button_b_match and prize_match):
        raise ValueError("Input text does not match the expected format.")

    # Parse extracted values
    button_a_x = int(button_a_match.group(1))
    button_a_y = int(button_a_match.group(2))
    button_b_x = int(button_b_match.group(1))
    button_b_y = int(button_b_match.group(2))
    prize_x = int(prize_match.group(1))
    prize_y = int(prize_match.group(2))

    # Store the results in a dictionary
    variables = {
        "ax": button_a_x,
        "ay": button_a_y,
        "bx": button_b_x,
        "by": button_b_y,
        "cx": prize_x,
        "cy": prize_y,
    }

    return variables


def solve_large_numbers(num_1, num_2, num_3, num_4, num_5, num_6):
    # Coefficient matrix for A and B
    coeff_matrix = np.array([[num_1, num_2],
                              [num_4, num_5]], dtype=np.float64)

    # Constants vector
    constants = np.array([10000000000000+num_3, 10000000000000+num_6], dtype=np.float64)

    # Solve the system of linear equations
    try:
        solution = np.linalg.solve(coeff_matrix, constants)
        A, B = solution
        tolerance = 1e-4
        # Check if the solution is close to integers
        if abs(A - round(A)) < tolerance and abs(B - round(B)) < tolerance:
            A, B = round(A), round(B)
            return {
                "A": A,
                "B": B,
                "Objective": 3 * A + B
            }
        else:
            return {
                "A": A,
                "B": B,
                "Message": "Solution is not an integer. Consider rounding or reformulating the problem."
            }
    except np.linalg.LinAlgError as e:
        return {"Error": f"Linear system cannot be solved: {str(e)}"}

def optimize_integer_variables(num_1, num_2, num_3, num_4, num_5, num_6):
    # Define the problem
    problem = LpProblem("Optimize_A_B", LpMinimize)

    # Define variables (A and B must be integers and less than 100)
    A = LpVariable("A", lowBound=0, cat="Continuous")
    B = LpVariable("B", lowBound=0, cat="Continuous")

    # Objective function: minimize 3*A + B
    problem += 3 * A + B, "Objective"

    # Constraints
    problem += A * num_1 + B * num_2 == num_3, "EqualityConstraint1"
    problem += A * num_4 + B * num_5 == (num_6), "EqualityConstraint2"

    # Solve the problem
    status = problem.solve()

    # Check if a solution exists
    if LpStatus[status] == "Optimal":
        return {
            "A": int(value(A)),
            "B": int(value(B)),
            "Objective": int(value(3 * A + B))
        }
    else:
        return {"Error": "No integer solution exists"}

if prod:
    with open('C:/Users/Amal Imangulov/Downloads/input_13.txt', 'r') as f:
        lines = f.readlines()
else:
    lines = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279""".split("""
""")

groups = group_strings(lines, 4)

for g in groups:
   l = ' '.join(g)
   v = extract_values(l)
   print(v['ax'], v['bx'], v['cx'], v['ay'], v['by'], v['cy'])
#   res = (optimize_integer_variables(v['ax'], v['bx'], v['cx'], v['ay'], v['by'], v['cy']))
   res = (solve_large_numbers(v['ax'], v['bx'], v['cx'], v['ay'], v['by'], v['cy']))

   try:
       print(res)
       s1 += res['Objective']
   except:
       pass
print(s1)
print(s2)
