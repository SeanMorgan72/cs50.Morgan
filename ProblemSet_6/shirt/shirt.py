import sys
import os
from PIL import Image, ImageOps

def main():
    # Check for correct number of command-line arguments
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Check if file extensions are valid
    valid_extensions = ('.jpg', '.jpeg', '.png')
    if not (input_file.lower().endswith(valid_extensions) and output_file.lower().endswith(valid_extensions)):
        sys.exit("Invalid ouput")

    # Check if input and output have the same extension
    if os.path.splitext(input_file)[1].lower() != os.path.splitext(output_file)[1].lower():
        sys.exit("Input and output have different extensions")

    # Check if input file exists
    if not os.path.isfile(input_file):
        sys.exit(f"Input does not exist")

    try:
        # Open the input image and shirt image
        input_image = Image.open(input_file)
        shirt_image = Image.open("shirt\shirt.png")

        # Resize and crop the input image to match the shirt image size
        input_image = ImageOps.fit(input_image, shirt_image.size)

        # Overlay the shirt image on the input image
        input_image.paste(shirt_image, shirt_image)

        # Save the result to the output file
        input_image.save(output_file)

    except Exception as e:
        sys.exit(f"An error occurred: {e}")

if __name__ == "__main__":
    main()