from math import floor, log10, sqrt

GRAVITATIONAL_FIELD_CONSTANT_G = 6.67e-11


class Answer:
    def __init__(self, answer=0):
        self.answer = answer

    def round_to_sig_figs(self, sig_figs):
        return round(self.answer, sig_figs - int(floor(log10(abs(self.answer)))) - 1)

    def to_standard_form(self, sig_figs: int = 4):
        return f"{self.answer:.{sig_figs}e}"


class GravitationalFieldStrengthFormula:
    def __init__(self, mass=0, distance=0, gravitationalFieldStrength=0):
        self.mass = mass
        self.distance = distance
        self.gravitationalFieldStrength = gravitationalFieldStrength

    def calculateGravitationalFieldStrength(self):
        self.gravitationalFieldStrength = (
            GRAVITATIONAL_FIELD_CONSTANT_G * self.mass
        ) / (self.distance * self.distance)
        return Answer(self.gravitationalFieldStrength)

    def calculateMass(self):
        self.mass = (
            self.gravitationalFieldStrength * self.distance * self.distance
        ) / GRAVITATIONAL_FIELD_CONSTANT_G
        return Answer(self.mass)

    def calculateDistance(self):
        self.distance = (
            self.gravitationalFieldStrength * self.mass
        ) / GRAVITATIONAL_FIELD_CONSTANT_G
        return Answer(self.distance)


class ForceOfAttractionFormula:
    def __init__(self, mass1=0, mass2=0, distance=0, forceOfAttraction=0):
        self.mass1 = mass1
        self.mass2 = mass2
        self.distance = distance
        self.forceOfAttraction = forceOfAttraction

    def calculateForceOfAttraction(self):
        self.forceOfAttraction = (
            GRAVITATIONAL_FIELD_CONSTANT_G * self.mass1 * self.mass2
        ) / (self.distance * self.distance)
        return Answer(self.forceOfAttraction)

    def calculateMass1(self):
        self.mass1 = (self.forceOfAttraction * self.distance * self.distance) / (
            GRAVITATIONAL_FIELD_CONSTANT_G * self.mass2
        )
        return Answer(self.mass1)

    def calculateMass2(self):
        self.mass2 = (self.forceOfAttraction * self.distance * self.distance) / (
            GRAVITATIONAL_FIELD_CONSTANT_G * self.mass1
        )
        return Answer(self.mass2)

    def calculateDistance(self):
        self.distance = (
            GRAVITATIONAL_FIELD_CONSTANT_G * self.mass1 * self.mass2
        ) / self.forceOfAttraction
        return Answer(self.distance)


class GravitationalEnergyFormula:
    def __init__(self, mass1=0, mass2=0, distance=0, gravitationalEnergy=0):
        self.mass1 = mass1
        self.mass2 = mass2
        self.distance = distance
        self.gravitationalEnergy = gravitationalEnergy

    def calculateGravitationalEnergy(self):
        self.gravitationalEnergy = (
            -GRAVITATIONAL_FIELD_CONSTANT_G * self.mass1 * self.mass2
        ) / self.distance
        return Answer(self.gravitationalEnergy)

    def calculateMass1(self):
        self.mass1 = (self.gravitationalEnergy * self.distance) / (
            -GRAVITATIONAL_FIELD_CONSTANT_G * self.mass2
        )
        return Answer(self.mass1)

    def calculateMass2(self):
        self.mass2 = (self.gravitationalEnergy * self.distance) / (
            -GRAVITATIONAL_FIELD_CONSTANT_G * self.mass1
        )
        return Answer(self.mass2)

    def calculateDistance(self):
        self.distance = (
            -GRAVITATIONAL_FIELD_CONSTANT_G * self.mass1 * self.mass2
        ) / self.gravitationalEnergy
        return Answer(self.distance)


class GravitationalPotentialFormula:
    def __init__(self, mass=0, height=0, gravitationalPotential=0):
        self.mass = mass
        self.height = height
        self.gravitationalPotential = gravitationalPotential

    def calculateGravitationalPotential(self):
        self.gravitationalPotential = (
            -GRAVITATIONAL_FIELD_CONSTANT_G * self.mass
        ) / self.height

        return Answer(self.gravitationalPotential)

    def calculateGravitationalPotentialEnergy(self):
        return Answer(self.gravitationalPotential * self.mass)

    def calculateMass(self):
        self.mass = (self.gravitationalPotential * self.height) / (
            -GRAVITATIONAL_FIELD_CONSTANT_G
        )
        return Answer(self.mass)

    def calculateHeight(self):
        self.height = (
            -GRAVITATIONAL_FIELD_CONSTANT_G * self.mass
        ) / self.gravitationalPotential
        return Answer(self.height)


class EscapeVelocityFormula:
    def __init__(self, mass=0, radius=0, escapeVelocity=0):
        self.mass = mass
        self.radius = radius
        self.escapeVelocity = escapeVelocity

    def calculateEscapeVelocity(self):
        self.escapeVelocity = sqrt(
            2 * GRAVITATIONAL_FIELD_CONSTANT_G * self.mass / self.radius
        )
        return Answer(self.escapeVelocity)

    def calculateMass(self):
        self.mass = (self.escapeVelocity * self.escapeVelocity * self.radius) / (
            2 * GRAVITATIONAL_FIELD_CONSTANT_G
        )
        return Answer(self.mass)

    def calculateRadius(self):
        self.radius = (self.escapeVelocity * self.escapeVelocity * self.radius) / (
            2 * GRAVITATIONAL_FIELD_CONSTANT_G
        )
        return Answer(self.radius)


def main(sig_figs: int = 4):
    formulas: dict = {
        "Gravitational Field Strength": {
            "1": "Gravitational Field Strength",
            "2": "Distance",
            "3": "Mass",
        },
        "Force of Attraction": {
            "1": "Mass 1",
            "2": "Mass 2",
            "3": "Distance",
            "4": "Force of Attraction",
        },
        "Gravitational Energy": {
            "1": "Mass 1",
            "2": "Mass 2",
            "3": "Distance",
            "4": "Gravitational Energy",
        },
        "Gravitational Potential": {
            "1": "Mass",
            "2": "Height",
            "3": "Gravitational Potential",
            "4": "Gravitational Potential Energy",
        },
        "Escape Velocity": {
            "1": "Mass",
            "2": "Radius",
            "3": "Escape Velocity",
        },
    }

    category_keys: dict = {
        "1": "Gravitational Field Strength",
        "2": "Force of Attraction",
        "3": "Gravitational Energy",
        "4": "Gravitational Potential",
        "5": "Escape Velocity",
    }

    print("What do you want to calculate?")
    print("    1. Gravitational Field Strength")
    print("    2. Force of Attraction")
    print("    3. Gravitational Energy")
    print("    4. Gravitational Potential")
    print("    5. Escape Velocity")

    chosen_category: int = int(input("Enter the number of the category: "))

    print(f"You chose {category_keys[str(chosen_category)]}.")

    print(f"What do you want to calculate?")
    for key, value in formulas[category_keys[str(chosen_category)]].items():
        print(f"    {key}. {value}")

    chosen_value_to_calculate: int = int(
        input("Enter the number of the value to calculate: ")
    )

    if chosen_category == 1:
        if chosen_value_to_calculate == 1:
            mass = float(eval(input("Enter the mass: ")))
            distance = float(eval(input("Enter the distance: ")))
            gravitationalFieldStrength = GravitationalFieldStrengthFormula(
                mass, distance
            ).calculateGravitationalFieldStrength()
            print(
                f"The gravitational field strength is {gravitationalFieldStrength.to_standard_form(sig_figs)} N/kg."
            )
        elif chosen_value_to_calculate == 2:
            mass = float(eval(input("Enter the mass: ")))
            gravitationalFieldStrength = float(
                eval(input("Enter the gravitational field strength: "))
            )
            distance = GravitationalFieldStrengthFormula(
                mass, gravitationalFieldStrength=gravitationalFieldStrength
            ).calculateDistance()
            print(f"The distance is {distance.to_standard_form(sig_figs)} m.")
        elif chosen_value_to_calculate == 3:
            distance = float(eval(input("Enter the distance: ")))
            gravitationalFieldStrength = float(
                eval(input("Enter the gravitational field strength: "))
            )
            mass = GravitationalFieldStrengthFormula(
                distance=distance, gravitationalFieldStrength=gravitationalFieldStrength
            ).calculateMass()
            print(f"The mass is {mass.to_standard_form(sig_figs)} kg.")

    elif chosen_category == 2:
        if chosen_value_to_calculate == 1:
            mass1 = float(eval(input("Enter the mass 1: ")))
            mass2 = float(eval(input("Enter the mass 2: ")))
            distance = float(eval(input("Enter the distance: ")))
            forceOfAttraction = ForceOfAttractionFormula(
                mass1, mass2, distance
            ).calculateForceOfAttraction()
            print(
                f"The force of attraction is {forceOfAttraction.to_standard_form(sig_figs)} N."
            )
        elif chosen_value_to_calculate == 2:
            mass1 = float(eval(input("Enter the mass 1: ")))
            forceOfAttraction = float(eval(input("Enter the force of attraction: ")))
            distance = float(eval(input("Enter the distance: ")))
            mass2 = ForceOfAttractionFormula(
                mass1, forceOfAttraction=forceOfAttraction, distance=distance
            ).calculateMass2()
            print(f"The mass 2 is {mass2.to_standard_form(sig_figs)} kg.")
        elif chosen_value_to_calculate == 3:
            mass1 = float(eval(input("Enter the mass 1: ")))
            mass2 = float(eval(input("Enter the mass 2: ")))
            forceOfAttraction = float(eval(input("Enter the force of attraction: ")))
            distance = ForceOfAttractionFormula(
                mass1, mass2, forceOfAttraction=forceOfAttraction
            ).calculateDistance()
            print(f"The distance is {distance.to_standard_form(sig_figs)} m.")
        elif chosen_value_to_calculate == 4:
            mass1 = float(eval(input("Enter the mass 1: ")))
            mass2 = float(eval(input("Enter the mass 2: ")))
            distance = float(eval(input("Enter the distance: ")))
            forceOfAttraction = ForceOfAttractionFormula(
                mass1, mass2, distance
            ).calculateForceOfAttraction()
            print(
                f"The force of attraction is {forceOfAttraction.to_standard_form(sig_figs)} N."
            )

    elif chosen_category == 3:
        if chosen_value_to_calculate == 1:
            mass2 = float(eval(input("Enter the mass 2: ")))
            distance = float(eval(input("Enter the distance: ")))
            gravitationalEnergy = float(eval(input("Enter the gravitational energy: ")))
            mass1 = GravitationalEnergyFormula(
                mass2=mass2, distance=distance, gravitationalEnergy=gravitationalEnergy
            ).calculateMass1()
            print(f"The mass 1 is {mass1.to_standard_form(sig_figs)} kg.")

        elif chosen_value_to_calculate == 2:
            mass1 = float(eval(input("Enter the mass 1: ")))
            distance = float(eval(input("Enter the distance: ")))
            gravitationalEnergy = float(eval(input("Enter the gravitational energy: ")))
            mass2 = GravitationalEnergyFormula(
                mass1, distance=distance, gravitationalEnergy=gravitationalEnergy
            ).calculateMass2()
            print(f"The mass 2 is {mass2.to_standard_form(sig_figs)} kg.")

        elif chosen_value_to_calculate == 3:
            mass1 = float(eval(input("Enter the mass 1: ")))
            mass2 = float(eval(input("Enter the mass 2: ")))
            gravitationalEnergy = float(eval(input("Enter the gravitational energy: ")))
            distance = GravitationalEnergyFormula(
                mass1, mass2, gravitationalEnergy=gravitationalEnergy
            ).calculateDistance()
            print(f"The distance is {distance.to_standard_form(sig_figs)} m.")

        elif chosen_value_to_calculate == 4:
            mass1 = float(eval(input("Enter the mass 1: ")))
            mass2 = float(eval(input("Enter the mass 2: ")))
            distance = float(eval(input("Enter the distance: ")))
            gravitationalEnergy = GravitationalEnergyFormula(
                mass1, mass2, distance
            ).calculateGravitationalEnergy()
            print(
                f"The gravitational energy is {gravitationalEnergy.to_standard_form(sig_figs)} J."
            )

    elif chosen_category == 4:
        if chosen_value_to_calculate == 1:
            height = float(eval(input("Enter the height: ")))
            gravitationalPotential = float(
                eval(input("Enter the gravitational potential: "))
            )
            mass = GravitationalPotentialFormula(
                height=height, gravitationalPotential=gravitationalPotential
            ).calculateMass()
            print(f"The mass is {mass.to_standard_form(sig_figs)} kg.")

        elif chosen_value_to_calculate == 2:
            mass = float(eval(input("Enter the mass: ")))
            gravitationalPotential = float(
                eval(input("Enter the gravitational potential: "))
            )
            height = GravitationalPotentialFormula(
                mass=mass, gravitationalPotential=gravitationalPotential
            ).calculateHeight()
            print(f"The height is {height.to_standard_form(sig_figs)} m.")

        elif chosen_value_to_calculate == 3:
            mass = float(eval(input("Enter the mass: ")))
            height = float(eval(input("Enter the height: ")))
            gravitationalPotential = GravitationalPotentialFormula(
                mass, height
            ).calculateGravitationalPotential()
            print(
                f"The gravitational potential is {gravitationalPotential.to_standard_form(sig_figs)} J/Kg."
            )

        elif chosen_value_to_calculate == 4:
            mass = float(eval(input("Enter the mass: ")))
            gravitationalPotential = float(
                eval(input("Enter the gravitational potential: "))
            )
            gravitationalPotentialEnergy = GravitationalPotentialFormula(
                mass, gravitationalPotential=gravitationalPotential
            ).calculateGravitationalPotentialEnergy()
            print(
                f"The gravitational potential energy is {gravitationalPotentialEnergy.to_standard_form(sig_figs)} J."
            )

    elif chosen_category == 5:
        if chosen_value_to_calculate == 1:
            radius = float(eval(input("Enter the radius: ")))
            escapeVelocity = float(eval(input("Enter the escape velocity: ")))
            mass = EscapeVelocityFormula(
                radius=radius, escapeVelocity=escapeVelocity
            ).calculateMass()
            print(f"The mass is {mass.to_standard_form(sig_figs)} kg.")

        elif chosen_value_to_calculate == 2:
            mass = float(eval(input("Enter the mass: ")))
            escapeVelocity = float(eval(input("Enter the escape velocity: ")))
            radius = EscapeVelocityFormula(
                mass=mass, escapeVelocity=escapeVelocity
            ).calculateRadius()
            print(f"The radius is {radius.to_standard_form(sig_figs)} m.")

        elif chosen_value_to_calculate == 3:
            mass = float(eval(input("Enter the mass: ")))
            radius = float(eval(input("Enter the radius: ")))
            escapeVelocity = EscapeVelocityFormula(
                mass=mass, radius=radius
            ).calculateEscapeVelocity()
            print(
                f"The escape velocity is {escapeVelocity.to_standard_form(sig_figs)} m/s."
            )

    else:

        print("Invalid category.")
        return

    print("Thank you for using this program.")


if __name__ == "__main__":

    GRAVITATIONAL_FIELD_CONSTANT_G = 6.674e-11

    main(4)


"""
Notes:

"""
