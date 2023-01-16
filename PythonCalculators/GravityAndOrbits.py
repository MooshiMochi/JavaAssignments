from math import floor, log10, sqrt

GRAVITATIONAL_FIELD_CONSTANT_G = 6.67e-11


class Answer:
    def __init__(self, answer=0):
        self.answer = answer

    def round_to_sig_figs(self, sig_figs):
        return round(self.answer, sig_figs - int(floor(log10(abs(self.answer)))) - 1)

    def to_standard_form(self, sig_figs: int = 4):
        return f"{self.answer:.{sig_figs}e}"


"""
Formulas:

GM/R = v^2
v = 2piR/T

GM/R = (2piR/T)^2
GMT^2 = 4pi^2R^3

"""

PI = 3.14159


class OrbitAndGravityRelationshipFormula:
    def __init__(
        self,
        mass: float = 0,
        radius: float = 0,
        velocity: float = 0,
        time_period: float = 0,
    ):
        self.mass = mass
        self.radius = radius
        self.velocity = velocity
        self.time_period = time_period

    def calculate_velocity(self):
        return Answer(2 * 3.14159 * self.radius / self.time_period)

    def calculate_time_period(self):
        if self.mass is not None and self.radius is not None:
            self.time_period = sqrt(
                (4 * PI**2 * self.radius**3)
                / (GRAVITATIONAL_FIELD_CONSTANT_G * self.mass)
            )
        elif self.velocity is not None and self.radius is not None:
            self.time_period = 2 * PI * self.radius / self.velocity

        else:
            return Answer(0)
        return Answer(self.time_period)

    def calculate_frequency(self):
        time_period = self.calculate_time_period()
        if time_period == 0:
            return Answer(0)
        return Answer(1 / self.calculate_time_period().answer)

    def calculate_radius(self):
        if self.velocity is not None and self.time_period is not None:
            self.radius = self.velocity * self.time_period / (2 * PI)
        elif self.mass is not None and self.time_period is not None:
            self.radius = sqrt(
                (GRAVITATIONAL_FIELD_CONSTANT_G * self.mass * self.time_period**2)
                / (4 * PI**2)
            )
        else:
            return Answer(0)

        return Answer(self.radius)

    def calculate_mass(self):
        if self.radius is not None and self.time_period is not None:
            return Answer(
                (4 * PI**2 * self.radius**3)
                / GRAVITATIONAL_FIELD_CONSTANT_G
                * self.time_period**2
            )
        elif self.velocity is not None and self.radius is not None:
            return Answer(
                self.velocity**2 * self.radius / GRAVITATIONAL_FIELD_CONSTANT_G
            )
        elif self.velocity is not None and self.time_period is not None:
            return Answer((self.velocity**2 * self.time_period**2) / (4 * PI**2))
        else:
            return Answer(0)


def handled_input(prompt: str, _type: object):
    try:
        result = input(prompt)
        if result == "":
            return None
        return _type(eval(result))
    except ValueError:
        return None


def main(sig_figs: int = 4):

    formulas: dict = {
        "Orbit And Gravity Relationship": {
            "1": "Mass",
            "2": "Radius",
            "3": "Velocity",
            "4": "Time Period",
            "5": "Frequency",
        },
    }

    category_keys: dict = {"1": "Orbit And Gravity Relationship"}

    print("What category would you like to use?")
    for key, value in category_keys.items():
        print(f"    {key}: {value}")

    category_choice = input("Enter the number of the category you would like to use: ")

    if category_choice == "1":

        formula_object = OrbitAndGravityRelationshipFormula()
        print("Please only fill the information you know.")
        formula_object.mass = handled_input("Enter the mass: ", float)
        formula_object.radius = handled_input("Enter the radius: ", float)
        formula_object.velocity = handled_input("Enter the velocity: ", float)
        formula_object.time_period = handled_input("Enter the time period: ", float)
        frequency = handled_input(
            "Enter the frequency (time for 1 revolution): ", float
        )
        if frequency:
            formula_object.time_period = 1 / frequency

        print("What formula would you like to use?")
        for key, value in formulas["Orbit And Gravity Relationship"].items():
            print(f"    {key}: {value}")

        formula_choice = input(
            "Enter the number of the formula you would like to use: "
        )

        if formula_choice == "1":
            print(
                f"The mass is {formula_object.calculate_mass().to_standard_form(sig_figs)}"
            )
        elif formula_choice == "2":
            print(
                f"The radius is {formula_object.calculate_radius().to_standard_form(sig_figs)}"
            )
        elif formula_choice == "3":
            print(
                f"The velocity is {formula_object.calculate_velocity().to_standard_form(sig_figs)}"
            )
        elif formula_choice == "4":
            print(
                f"The time period is {formula_object.calculate_time_period().to_standard_form(sig_figs)}"
            )
        elif formula_choice == "5":
            print(
                f"The frequency is {formula_object.calculate_frequency().to_standard_form(sig_figs)}"
            )
        else:
            print("Invalid formula choice.")


if __name__ == "__main__":
    main()

"""
Notes:

3.156e7 seconds in 1 year


m = 2.055e30 kg
r = 3e11
f = 




r = 2 * 1.5e11
m = 2.055e30

T = (4 * PI * r**3) / (G * m)
T = T / 3.156e7


"""
