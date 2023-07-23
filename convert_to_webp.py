import os
from PIL import Image


def convert_to_webp(input_path, output_path):
    with Image.open(input_path) as img:
        img.save(output_path, 'webp', quality=60, lossless=False)


def main():
    input_path = "C:\\Users\\nicks\\Downloads\\"
    output_path = "C:\\Users\\nicks\\Downloads\\webp\\"
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    for file in os.listdir(input_path):
        if file.endswith(".jpg") or file.endswith(".png"):
            filename = os.path.splitext(file)[0] + ".webp"
            convert_to_webp(input_path + file, output_path + filename)


if __name__ == "__main__":
    main()
