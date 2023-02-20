import re
from typing import Any

SIG_FIGS = float("inf")


def get_user_input(prompt: str) -> Any:
    global SIG_FIGS
    user_input = input(prompt)

    # Extract values in scientific notation
    scientific_notation_pattern = r"([-+]?\d*[.]?\d+)([eE][-+]?\d+)?"
    scientific_notations = re.findall(scientific_notation_pattern, user_input)
    print(scientific_notations)

    # Get number of significant figures for each value in scientific notation
    sig_figs = []
    for value, _ in scientific_notations:
        value = value.replace("-", "").replace("+", "")
        sig_figs.append(len(value.replace(".", "")))

    # Update SIG_FIGS to the lowest number of significant figures
    if sig_figs and SIG_FIGS > min(sig_figs):
        SIG_FIGS = min(sig_figs)

    try:
        return eval(user_input)
    except (ValueError, NameError, SyntaxError):
        return user_input


val1 = get_user_input("Enter a value:")
val2 = get_user_input("Enter another value:")

print(f"val1 = {val1}, val2 = {val2}, SIG_FIGS = {SIG_FIGS}")
