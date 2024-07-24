def main():
    while True:
        fraction = input("Enter the fuel amount (X/Y): ")
        percentage = get_fuelAmt(fraction)
        if percentage is not None:
            display(percentage)
            break

def get_fuelAmt(fraction):
    try:
        x,y = fraction.split("/")
        x = int(x)
        y = int(y)
        
        if x > y or y == 0:
            raise ValueError
        
        return (x/y)*100
    
    except(ValueError, ZeroDivisionError):
        return None

def display(percentage):
    if percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(f"{round(percentage)}%")

main()