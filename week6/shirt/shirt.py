import sys
import os
from PIL import Image, ImageOps


def main():
    if len(sys.argv) < 3:
        sys.exit('Too few command-line arguments')
    elif len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')
    else:
        image_format = ['.jpg', '.jpeg', '.png']
        input_image = os.path.splitext(sys.argv[1])
        output_image = os.path.splitext(sys.argv[2])

        if output_image[1].lower() not in image_format:
            sys.exit('Invalid Output')
        elif input_image[1].lower() != output_image[1].lower():
            sys.exit('Input and output have different extensions!')
        else:
            edit_photo(sys.argv[1], sys.argv[2])


def edit_photo(input_image, output_image):
    try:
        shirt = Image.open('shirt.png')
        with Image.open(input_image) as inp:
            input_cropped = ImageOps.fit(inp, shirt.size)
            input_cropped.paste(shirt, mask=shirt)
            input_cropped.save(output_image)
    except FileNotFoundError:
        sys.exit('Input does not exist!')


if __name__ == '__main__':
    main()
