def calculate_expression(expression):
    # Split the input into components
    x, y, z = expression.split()
    
    # Convert x and z to integers
    x = int(x)
    z = int(z)
    
    # Perform the operation based on the operator
    match y:
        case '+':
            result = x + z
        case '-':
            result = x - z
        case '*':
            result = x * z
        case '/':
            result = x / z
        case _:
            raise ValueError("Invalid operator!")
    
    # Return the result formatted to one decimal place
    return f"{result:.1f}"

def main():
    # Prompt user for the input
    expression = input("Enter an arithmetic expression (x y z): ")
    
    try:
        # Calculate the result
        result = calculate_expression(expression)
        # Print the result
        print(result)
    except ValueError as e:
        print(e)

# Call the main function to execute the program
if __name__ == "__main__":
    main()
