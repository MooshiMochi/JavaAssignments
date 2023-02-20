"""
Orbit and Gravity Calculator

Formulae from:

GM/R = v^2
v = 2piR/T

GM/R = (2piR/T)^2
GMT^2 = 4pi^2R^3

"""


import math
import re
from typing import Any, List, Union

SIG_FIGS = float(
    "inf"
)  # set to a number to round to that number of significant figures
GET_SIG_FIGS_FROM_USER = False


class Equation:
    def __init__(
        self,
        equation_name: str,
        variables_and_units: dict[str, str],
        equations: dict[str, str],
    ):
        self.equation_name = equation_name
        self.variables_and_units = variables_and_units
        self.equations = equations

    def solve(
        self, variable_values: dict[str, Union[float, str]], solve_for: str
    ) -> dict[str, Union[float, str]]:
        global GET_SIG_FIGS_FROM_USER

        if solve_for not in self.variables_and_units:
            print(f"Error: {solve_for} is not a variable in {self.equation_name}")
            return variable_values

        GET_SIG_FIGS_FROM_USER = True

        for variable, unit in self.variables_and_units.items():
            if variable == solve_for:
                continue
            if variable not in variable_values:
                value = get_user_input(f"Enter the value of {variable} in {unit}: ")
                if value is not None:
                    variable_values[variable] = float(value)
            if variable not in variable_values:
                print(f"Error: {variable} value is required to solve for {solve_for}")
                return variable_values

        try:
            result = eval(self.equations[solve_for], {"math": math, **variable_values})
            variable_values[solve_for] = result
            print(
                f"{solve_for} = {result:.{SIG_FIGS}g} {self.variables_and_units[solve_for]}"
            )
        except (NameError, ZeroDivisionError, SyntaxError):
            print(f"Error: Could not solve for {solve_for}")

        return variable_values


def get_user_input(prompt: str) -> Any:
    global SIG_FIGS
    user_input = input(prompt)

    # Extract values in scientific notation
    scientific_notation_pattern = r"([-+]?\d*[.]?\d+)([eE][-+]?\d+)?"
    scientific_notations = re.findall(scientific_notation_pattern, user_input)

    # Get number of significant figures for each value in scientific notation
    sig_figs = []
    for value, _ in scientific_notations:
        value = value.replace("-", "").replace("+", "")
        sig_figs.append(len(value.replace(".", "")))

    # Update SIG_FIGS to the lowest number of significant figures
    if sig_figs and SIG_FIGS > min(sig_figs) and GET_SIG_FIGS_FROM_USER:
        SIG_FIGS = min(sig_figs)

    try:
        return eval(user_input)
    except (ValueError, NameError, SyntaxError):
        return user_input


equations: List[Equation] = [
    Equation(
        "R = GM/v²",
        {"R": "meters (m)", "M": "kg", "v": "m/s"},
        {
            "R": "(6.674e-11)M/v**2",
            "M": "R*v**2/(6.674e-11)",
            "v": "math.sqrt((6.674e-11)M/R)",
        },
    ),
    Equation(
        "v = 2πR/T",
        {"v": "m/s", "R": "meters (m)", "T": "seconds (s)"},
        {"v": "2*math.pi*R/T", "R": "v*T/(2*math.pi)", "T": "2*math.pi*R/v"},
    ),
    Equation(
        "R = GMT²/(2π)²",
        {"R": "meters (m)", "M": "kg", "T": "seconds (s)"},
        {
            "R": "((6.674e-11)*M*T**2)/(4*math.pi**2)",
            "M": "(4*math.pi**2*R*T**2)/((6.674e-11)*T**2)",
            "T": "math.sqrt((4*math.pi**2*R)/((6.674e-11)*M))",
        },
    ),
    Equation(
        "GMT² = 4π²R³",
        {"R": "meters (m)", "M": "kg", "T": "seconds (s)"},
        {
            "R": "((4*math.pi**2*T**2)/((6.674e-11)*M))**(1/3)",
            "M": "(4*math.pi**2*R**3)/(T**2*(6.674e-11))",
            "T": "math.sqrt((4*math.pi**2*R**3)/((6.674e-11)*M))",
        },
    ),
]

while True:
    print("\nSelect an equation to use:")
    SIG_FIGS = float("inf")
    GET_SIG_FIGS_FROM_USER = False

    for i, equation in enumerate(equations):
        print(f"{i+1}: {equation.equation_name}")
    print("0: Exit")
    equation_choice: int = get_user_input("Enter the index of the equation: ")

    if equation_choice == 0:
        break
    elif equation_choice not in range(1, len(equations) + 1):
        print("Invalid choice. Please select an equation from the list.")
        continue

    selected_equation: Equation = equations[equation_choice - 1]

    print("\nSelect a variable to calculate:")
    for variable in selected_equation.variables_and_units:
        print(variable)
    solve_for: str = get_user_input("Enter the variable you want to solve for: ")

    variable_values: dict[str, Union[float, str]] = {}
    variable_values = selected_equation.solve(variable_values, solve_for)

    input("Press Enter to continue...")
    print("\033c", end="")  # clear console
