import sys
import random
from pyfiglet import Figlet

def main():
    # Parse command-line arguments
    if len(sys.argv) == 1:
        use_random_font = True
    elif len(sys.argv) == 3 and (sys.argv[1] == '-f' or sys.argv[1] == '--font'):
        use_random_font = False
        font_name = sys.argv[2]
        if font_name not in Figlet().getFonts():
            sys.exit("Invalid usage.")
    else:
        sys.exit("Invalid usage.")

    # Prompt the user for text
    user_input = input("Enter text: ")

    # Set the font
    if use_random_font:
        fonts = Figlet.getFonts()
        font_name = random.choice(fonts)

    # Create a Figlet instance and set the font
    figlet = Figlet(font=font_name)

    # Output the text in the desired font
    print(figlet.renderText(user_input))

if __name__ == "__main__":
    main()