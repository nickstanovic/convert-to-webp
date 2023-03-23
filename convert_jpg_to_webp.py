#!/usr/bin/env python
import os
from gimpfu import *

def convert_jpg_to_webp(input_path, output_path, quality=90, lossless=False):
    image = pdb.gimp_file_load(input_path, input_path)
    drawable = pdb.gimp_image_get_active_layer(image)

    # Set the WebP save parameters
    preset = 4  # Default preset
    alpha_quality = 0
    animation = False
    minimize_size = False
    keyframe_distance = 0
    kmin = 0
    kmax = 0
    filter_strength = 0

    # Save as WebP
    pdb.file_webp_save(
        image,
        drawable,
        output_path,
        output_path,
        quality,
        alpha_quality,
        lossless,
        animation,
        preset,
        keyframe_distance,
        kmin,
        kmax,
        filter_strength
    )

    # Clean up
    pdb.gimp_image_delete(image)

def main():
    current_directory = os.getcwd()

    for filename in os.listdir(current_directory):
        if filename.lower().endswith(".jpg"):
            input_path = os.path.join(current_directory, filename)
            output_path = os.path.join(current_directory, os.path.splitext(filename)[0] + ".webp")
            convert_jpg_to_webp(input_path, output_path)

if __name__ == "__main__":
    main()

