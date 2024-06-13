def mass_to_energy():
    #Speed of light in meters per second.
    speed_of_light = 3 * 10**8
    
    #Prompt user for mass in kilograms.
    mass = int(input("Enter the mass in kilograms: "))
    
    #Calculate the energy using E = mc^2.
    energy = mass * speed_of_light**2
    
    #Output the energy in Joules.
    print(f"The equivalent energy is {energy} Joules.")
    
    #Convert energy to scientific notation.
    exponent = 0
    while energy >= 10:
        energy /= 10
        exponent += 1
    
    #Convert back to integer format.
    new_figure = int(energy)
    result = f"{new_figure}e{exponent}"
    
    #Output the energy in scientific notation without trailing zeros.
    print(f"The equivalent energy is {result} Joules.")

mass_to_energy()