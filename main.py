# COS101 PROJECT.
# five(5) physics operations that can be called using its assigned function/variable

# function 1:efficiency
def calculate_efficiency():
    """this calculates efficiency as a percentage."""

    try:  # this attempts to take input and perform the calculations.
        work_output = float(input("enter work output (J): "))
        work_input = float(input("enter work input (J): "))
        efficiency = (work_output / work_input) * 100
        print(f"Efficiency:{efficiency:.2f}%")  # display the result rounded to two(2) decimal places
    except ValueError:  # this handles invalid input like non-numeric value
        print("please enter numeric values only.")


# function 2: gravitational_force
def calculate_gravitational_force():
    """this calculates gravitational force between two masses."""

    try:  # this is a code block that raises an exception for invalid inputs
        g = 6.67430e-11  # gravitational constant in m^3 kg^-1 s^-2
        mass1 = float(input("Enter the mass of the first object (kg):"))
        mass2 = float(input("Enter the mass of the second object (kg):"))
        distance = float(input("Enter the distance between the objects (m):"))
        if distance == 0:
            print("distance cannot be zero.")
        else:
            gravitational_force = g * (mass1 * mass2) / (distance ** 2)
        print(f"Gravitational force:{gravitational_force:.2e} N")  # e is a scientific notation for large/small numbers.
    except ValueError:  # this is the code block that executes if any exception or error occurs
        print("enter only numeric values please.")


# function 3: power
def calculate_power():
    """this calculates power output."""

    work = float(input("Enter work done (J): "))
    time = float(input("Enter time (s): "))
    if time != 0:  # this helps to check time is not equal to zero to avoid division by zero error
        power = work / time
        print(f"Power: {power:.2f} W")  # rounded to two(2) decimal places
    else:
        print("Time cannot be equal to zero.")


# function 4: Momentum
def calculate_momentum():
    """this calculates the momentum."""

    try:
        its_mass = float(input("Enter the mass(kg): "))
        its_velocity = float(input("Enter the velocity (m/s): "))
        momentum = its_mass * its_velocity  # momentum formula p = mv
        print(f"Momentum: {momentum:.2f} kg.m/s")  # this is rounded to two(2) decimal places
    except ValueError:
        print("please enter valid numeric values.")  # this helps to handle non-numeric inputs to avoid crashing.


# function 5: Kinetic Energy
def calculate_kinetic_energy():
    """calculates kinetic energy of an object using integer inputs."""

    try:
        the_mass = int(input("Enter mass(kg): "))  # Enter mass in kilograms, using integers only
        the_vel = int(input("Enter velocity (m/s): "))  # Enter velocity in m/s, using integers also
        kinetic_energy = (1 / 2) * the_mass * (the_vel ** 2)  # kinetic energy formula (KE = 1/2 * m * v^2)
        print(f"Kinetic Energy:{kinetic_energy:.2f} J")  # outputs the result in joules(J)
    except ValueError:
        print("please enter valid integers.")  # this handles non-numeric integers input perfectly


# THIS IS THE MAIN MENU TO CALL ALL FUNCTIONS
def main():  # this helps to keep the program running until user decides to quit(LOOPS).
    while True:  # this displays the main menu to the user with options to choose.
        print("Choose a physics operation:")
        print("a. calculate Efficiency")  # displays option 'a' to calculate efficiency
        print("b. calculate Gravitational Force")  # option 'b' to calculate  gravitational force
        print("c. calculate Power")  # option 'c' to  calculate power
        print("d. calculate Momentum")  # option 'd' used to calculate momentum
        print("e. calculate Kinetic Energy")  # option 'e' to calculate kinetic energy
        print("q. quit program")  # option 'q' to quit the loop

        # this menu prompts the user to enter a choice

        choice = input(" kindly input your desired choice: ").lower()
        # .lower() helps convert the choice input to lower case for consistency

        if choice == "a":
            calculate_efficiency()
        elif choice == "b":
            calculate_gravitational_force()
        elif choice == "c":
            calculate_power()
        elif choice == "d":
            calculate_momentum()
        elif choice == "e":
            calculate_kinetic_energy()
        elif choice == "q":
            print("YOU ARE EXITING THE PROGRAM.")  # this displays an exit message if user chooses "q"
        else:
            print("YOUR CHOICE IS INVALID,TRY AGAIN!.")  # this handles any invalid input.


#  THE MENU BELOW STARTS THE PROGRAM.

if __name__ == "__main__":
    main()