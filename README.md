# WebP Image Converter

This Python script converts all JPG and PNG files in a specified directory to WebP format. The output files are saved in a separate directory with the same file name and a .webp extension.

## Requirements

- Python 3.x
- PIL (Python Imaging Library)

## Installation

1. Install Python 3.x on your system.
2. Install PIL by running the following command in your terminal:

    ```bash
    pip install pillow
    ```

3. Download or clone this repository to your computer.

## Usage

- The output directory is created automatically if it doesn't exist. I left mine as an example.
- The script only converts files with a .jpg or .png extension. If you want to convert other file types, you'll need to modify the script.
- The quality level and compression type can be changed by modifying the `convert_to_webp` function in the script.

## Notes

This script has been tested on Windows 11.
