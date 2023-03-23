import os
from PIL import Image


def convert_jpg_to_webp(input_path, output_path):
    with Image.open(input_path) as img:
        img.save(output_path, 'webp', quality=60, lossless=False)


def main():
    input_path = "C:\\Users\\nicks\\Downloads\\"
    output_path = "C:\\Users\\nicks\\Downloads\\webp\\"
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    for file in os.listdir(input_path):
        if file.endswith(".jpg"):
            filename = os.path.splitext(file)[0] + ".webp"
            convert_jpg_to_webp(input_path + file, output_path + filename)


if __name__ == "__main__":
    main()
