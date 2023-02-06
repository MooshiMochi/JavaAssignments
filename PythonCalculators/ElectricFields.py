import builtins
from math import floor, log10, sqrt

COULOMBS_CONSTANT_K = 8.99e9


def input(*args, **kwargs):
    user_input: str = builtins.input(*args, **kwargs)
    try:
        return eval(user_input)
    except (NameError, SyntaxError, ValueError):
        return user_input


class Answer:
    def __init__(self, answer=0):
        self.answer = answer

    def round_to_sig_figs(self, sig_figs):
        return round(self.answer, sig_figs - int(floor(log10(abs(self.answer)))) - 1)

    def to_standard_form(self, sig_figs: int = 4):
        return f"{self.answer:.{sig_figs}e}"


# E = F / q where F is the force and q is the charge
# E = V / d where V is the voltage and d is the distance
# E = kQ / r^2 where k is the Coulomb's constant, Q is the charge, and r is the distance from the center of the charge
# F = kq1q2 / r^2 where k is the Coulomb's constant, q1 and q2 are the charges, and r is the distance between the charges


class ElectricFieldWithForceEquation:
    def __init__(self, force: float = 0, charge: float = 0, field_strength: float = 0):
        self.force = force
        self.charge = charge
        self.field_strength = field_strength

    @staticmethod
    def show_equation():
        return "E = F / q where F is the force and q is the charge"

    def calculate_electric_field(self) -> Answer:
        return Answer(self.force / self.charge)

    def calculate_force(self) -> Answer:
        return Answer(self.charge * self.field_strength)

    def calculate_charge(self) -> Answer:
        return Answer(self.force / self.field_strength)


class ElectricFieldWithVoltageEquation:
    def __init__(
        self, voltage: float = 0, distance: float = 0, field_strength: float = 0
    ):
        self.voltage = voltage
        self.distance = distance
        self.field_strength = field_strength

    @staticmethod
    def show_equation():
        return "E = V / d where V is the voltage and d is the distance"

    def calculate_electric_field(self) -> Answer:
        return Answer(self.voltage / self.distance)

    def calculate_voltage(self) -> Answer:
        return Answer(self.distance * self.field_strength)

    def calculate_distance(self) -> Answer:
        return Answer(self.voltage / self.field_strength)


class ElectricFieldWithChargeAndDistanceEquation:
    def __init__(
        self, charge: float = 0, distance: float = 0, field_strength: float = 0
    ):
        self.charge = charge
        self.distance = distance
        self.field_strength = field_strength

    @staticmethod
    def show_equation():
        return "E = kQ / r^2 where k is the Coulomb's constant, Q is the charge, and r is the distance from the center of the charge"

    def calculate_electric_field(self) -> Answer:
        return Answer((COULOMBS_CONSTANT_K * self.charge) / self.distance**2)

    def calculate_charge(self) -> Answer:
        return Answer((self.field_strength * self.distance**2) / COULOMBS_CONSTANT_K)

    def calculate_distance(self) -> Answer:
        return Answer(sqrt((COULOMBS_CONSTANT_K * self.charge) / self.field_strength))


class ForceWith2ChargesEquation:
    def __init__(
        self,
        charge1: float = 0,
        charge2: float = 0,
        distance: float = 0,
        force: float = 0,
    ):
        self.charge1 = charge1
        self.charge2 = charge2
        self.distance = distance
        self.force = force

    @staticmethod
    def show_equation():
        return f"F = kq1q2 / r^2 where k is the Coulomb's constant, q1 and q2 are the charges, and r is the distance between the charges"

    def calculate_force(self) -> Answer:
        return Answer(
            (COULOMBS_CONSTANT_K * self.charge1 * self.charge2) / (self.distance**2)
        )

    def calculate_charge1(self) -> Answer:
        return Answer(
            (self.force * self.distance**2) / (COULOMBS_CONSTANT_K * self.charge2)
        )

    def calculate_charge2(self) -> Answer:
        return Answer(
            (self.force * self.distance**2) / (COULOMBS_CONSTANT_K * self.charge1)
        )

    def calculate_distance(self) -> Answer:
        return Answer(
            sqrt((COULOMBS_CONSTANT_K * self.charge1 * self.charge2) / self.force)
        )


# E = F/q
# E = V/d
# F/q = V/d
# F = qV/d


class ForceWithChargeVoltageAndDistanceEquation:
    def __init__(
        self,
        force: float = 0,
        voltage: float = 0,
        charge: float = 0,
        distance: float = 0,
    ):
        self.force = force
        self.charge = charge
        self.voltage = voltage
        self.distance = distance

    @staticmethod
    def show_equation():
        return "F = qV/d"

    def calculate_force(self) -> Answer:
        return Answer(self.charge * self.voltage / self.distance)

    def calculate_voltage(self) -> Answer:
        return Answer(self.force * self.distance / self.charge)

    def calculate_distance(self) -> Answer:
        return Answer(self.force * self.voltage / self.charge)

    def calculate_charge(self) -> Answer:
        return Answer(self.force * self.distance / self.voltage)


if __name__ == "__main__":

    while True:
        print()
        print("What equation do you want to use?")
        print("1. Electric Field with Force --> E = F / q")
        print("2. Electric Field with Voltage --> E = V / d")
        print("3. Electric Field with Charge and Distance --> E = kQ / r^2")
        print("4. Force with 2 Charges --> F = kq1q2 / r^2")
        print("5. Electric Field with Force and Voltage --> F = qV/d")

        choice = input("Enter your choice: ")

        if choice == 1:
            ElectricFieldWithForceEquation.show_equation()
            what_to_calculate = input("What do you want to calculate? (E, F, or q): ")
            if what_to_calculate.lower() == "e":
                force = float(input("Enter the force in N: "))
                charge = float(input("Enter the charge in C: "))

                answer = ElectricFieldWithForceEquation(
                    force=force, charge=charge
                ).calculate_electric_field()
                print(f"The electric field strength is {answer.to_standard_form()} N/C")

            elif what_to_calculate.lower() == "f":
                electric_field = float(input("Enter the electric field in N/C: "))
                charge = float(input("Enter the charge in C: "))

                answer = ElectricFieldWithForceEquation(
                    field_strength=electric_field, charge=charge
                ).calculate_force()
                print(f"The force is {answer.to_standard_form()} N")

            elif what_to_calculate.lower() == "q":
                electric_field = float(input("Enter the electric field in N/C: "))
                force = float(input("Enter the force in N: "))

                answer = ElectricFieldWithForceEquation(
                    field_strength=electric_field, force=force
                ).calculate_charge()
                print(f"The charge is {answer.to_standard_form()} C")

        elif choice == 2:
            ElectricFieldWithVoltageEquation.show_equation()
            what_to_calculate = input("What do you want to calculate? (E, V, or d): ")
            if what_to_calculate.lower() == "e":
                voltage = float(input("Enter the voltage in V: "))
                distance = float(input("Enter the distance in m: "))

                answer = ElectricFieldWithVoltageEquation(
                    voltage=voltage, distance=distance
                ).calculate_electric_field()
                print(f"The electric field is {answer.to_standard_form()} V/m")

            elif what_to_calculate.lower() == "v":
                electric_field = float(input("Enter the electric field in V/m: "))
                distance = float(input("Enter the distance in m: "))

                answer = ElectricFieldWithVoltageEquation(
                    field_strength=electric_field, distance=distance
                ).calculate_voltage()
                print(f"The voltage is {answer.to_standard_form()} V")

            elif what_to_calculate.lower() == "d":
                electric_field = float(input("Enter the electric field in V/m: "))
                voltage = float(input("Enter the voltage in V: "))

                answer = ElectricFieldWithVoltageEquation(
                    field_strength=electric_field, voltage=voltage
                ).calculate_distance()
                print(f"The distance is {answer.to_standard_form()} m")

        elif choice == 3:
            ElectricFieldWithChargeAndDistanceEquation.show_equation()
            what_to_calculate = input("What do you want to calculate? (E, Q, or d): ")
            if what_to_calculate.lower() == "e":
                charge = float(input("Enter the charge in C: "))
                distance = float(input("Enter the distance in m: "))

                answer = ElectricFieldWithChargeAndDistanceEquation(
                    charge=charge, distance=distance
                ).calculate_electric_field()
                print(f"The electric field strength is {answer.to_standard_form()} N/C")

            elif what_to_calculate.lower() == "q":
                electric_field = float(input("Enter the electric field in N/C: "))
                distance = float(input("Enter the distance in m: "))

                answer = ElectricFieldWithChargeAndDistanceEquation(
                    field_strength=electric_field, distance=distance
                ).calculate_charge()
                print(f"The charge is {answer.to_standard_form()} C")

            elif what_to_calculate.lower() == "d":
                electric_field = float(input("Enter the electric field in N/C: "))
                charge = float(input("Enter the charge in C: "))

                answer = ElectricFieldWithChargeAndDistanceEquation(
                    field_strength=electric_field, charge=charge
                ).calculate_distance()
                print(f"The distance is {answer.to_standard_form()} m")

        elif choice == 4:
            ForceWith2ChargesEquation.show_equation()
            what_to_calculate = input(
                "What do you want to calculate? (F, q1, q2, or d): "
            )
            if what_to_calculate.lower() == "f":
                charge1 = float(input("Enter the first charge in C: "))
                charge2 = float(input("Enter the second charge in C: "))
                distance = float(input("Enter the distance in m: "))

                answer = ForceWith2ChargesEquation(
                    charge1=charge1, charge2=charge2, distance=distance
                ).calculate_force()
                print(f"The force is {answer.to_standard_form()} N")

            elif what_to_calculate.lower() == "q1":
                force = float(input("Enter the force in N: "))
                charge2 = float(input("Enter the second charge in C: "))
                distance = float(input("Enter the distance in m: "))

                answer = ForceWith2ChargesEquation(
                    force=force, charge2=charge2, distance=distance
                ).calculate_charge1()
                print(f"The first charge is {answer.to_standard_form()} C")

            elif what_to_calculate.lower() == "q2":
                force = float(input("Enter the force in N: "))
                charge1 = float(input("Enter the first charge in C: "))
                distance = float(input("Enter the distance in m: "))

                answer = ForceWith2ChargesEquation(
                    force=force, charge1=charge1, distance=distance
                ).calculate_charge2()
                print(f"The second charge is {answer.to_standard_form()} C")

            elif what_to_calculate.lower() == "d":
                force = float(input("Enter the force in N: "))
                charge1 = float(input("Enter the first charge in C: "))
                charge2 = float(input("Enter the second charge in C: "))

                answer = ForceWith2ChargesEquation(
                    force=force, charge1=charge1, charge2=charge2
                ).calculate_distance()
                print(f"The distance is {answer.to_standard_form()} m")

        elif choice == 5:
            ForceWithChargeVoltageAndDistanceEquation.show_equation()
            what_to_calculate = input("What do you want to calculate? (F, q, V or d): ")
            if what_to_calculate.lower() == "f":
                charge = float(input("Enter the charge in C: "))
                distance = float(input("Enter the distance in m: "))
                voltage = float(input("Enter the voltage in V: "))

                answer = ForceWithChargeVoltageAndDistanceEquation(
                    charge=charge, distance=distance, voltage=voltage
                ).calculate_force()
                print(f"The force is {answer.to_standard_form()} N")

            elif what_to_calculate.lower() == "q":
                force = float(input("Enter the force in N: "))
                distance = float(input("Enter the distance in m: "))
                voltage = float(input("Enter the voltage in V: "))

                answer = ForceWithChargeVoltageAndDistanceEquation(
                    force=force, distance=distance, voltage=voltage
                ).calculate_charge()
                print(f"The charge is {answer.to_standard_form()} C")

            elif what_to_calculate.lower() == "v":
                force = float(input("Enter the force in N: "))
                charge = float(input("Enter the charge in C: "))
                distance = float(input("Enter the distance in m: "))

                answer = ForceWithChargeVoltageAndDistanceEquation(
                    force=force, charge=charge, distance=distance
                ).calculate_voltage()
                print(f"The voltage is {answer.to_standard_form()} V")

            elif what_to_calculate.lower() == "d":
                force = float(input("Enter the force in N: "))
                charge = float(input("Enter the charge in C: "))
                voltage = float(input("Enter the voltage in V: "))

                answer = ForceWithChargeVoltageAndDistanceEquation(
                    force=force, charge=charge, voltage=voltage
                ).calculate_distance()
                print(f"The distance is {answer.to_standard_form()} m")

        else:
            print("Invalid choice")
            print()
            continue
